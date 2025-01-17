import json
import traceback
from contextlib import contextmanager
from logging import getLogger
from urllib.parse import urlparse

import pyarrow as pa
import pyarrow.parquet as pq
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder

from data_model.models import Cache
from scorer.export_utils import (
    export_data_for_model,
    get_pa_schema,
    upload_to_s3,
)

log = getLogger(__name__)


def get_parquet_writer(output_file):
    @contextmanager
    def writer_context_manager(model):
        schema = get_pa_schema(model)
        try:
            with pq.ParquetWriter(output_file, schema) as writer:

                class WriterWrappe:
                    def __init__(self, writer):
                        self.writer = writer

                    def write_batch(self, data):
                        batch = pa.RecordBatch.from_pylist(data, schema=schema)
                        self.writer.write_batch(batch)

                yield WriterWrappe(writer)
        finally:
            pass

    return writer_context_manager


def get_jsonl_writer(output_file):
    @contextmanager
    def eth_stamp_writer_context_manager(queryset):
        try:
            with open(output_file, "w", encoding="utf-8") as file:

                class WriterWrappe:
                    def __init__(self, file):
                        self.file = file

                    def write_batch(self, data):
                        for d in data:
                            try:
                                value = d["value"]
                                address = d["key_1"].lower()
                                model = d["key_0"].lower()
                                self.file.write(
                                    json.dumps(
                                        d,
                                        cls=DjangoJSONEncoder,
                                    )
                                    + "\n"
                                )
                            except Exception:
                                log.error(
                                    f"Error when writing record '{d}'", exc_info=True
                                )

                yield WriterWrappe(file)
        finally:
            pass

    return eth_stamp_writer_context_manager


class Command(BaseCommand):
    help = "Export eth-model score to jsonl"

    def add_arguments(self, parser):
        parser.add_argument(
            "--batch-size",
            type=int,
            default=1000,
            help="""Size of record batches.
            If present, this will read the records in batches. The result list is ordered by pk (id), to get
            to the next batch we query by id__gt=last_id.
            """,
        )
        parser.add_argument(
            "--s3-uri", type=str, help="The S3 URI target location for the files"
        )
        parser.add_argument(
            "--data-model",
            type=str,
            help="""The name of the prediction data model for which to export data.

For example:
    - predict - for eth model v1
    - predict_eth_v2 - for eth model v1
    - predict_zksync - for zksync model
    - predict_zksync_v2 - for zksync model v2
""",
        )

        parser.add_argument("--filename", type=str, help="The output filename")
        parser.add_argument(
            "--s3-extra-args",
            type=str,
            help="""JSON object, that contains extra args for the files uploaded to S3.
            This will be passed in as the `ExtraArgs` parameter to boto3's upload_file method.""",
        )
        parser.add_argument(
            "--format",
            type=str,
            choices=["jsonl", "parquet"],
            help="The output format",
            default="jsonl",
        )

    def handle(self, *args, **options):
        batch_size = options["batch_size"]
        s3_uri = options["s3_uri"]
        filename = options["filename"]
        format = options["format"]
        data_model_names = (
            [n.strip() for n in options["data_model"].split(",")]
            if options["data_model"]
            else None
        )

        extra_args = (
            json.loads(options["s3_extra_args"]) if options["s3_extra_args"] else None
        )

        self.stdout.write(f"EXPORT - s3_uri      : '{s3_uri}'")
        self.stdout.write(f"EXPORT - batch_size  : '{batch_size}'")
        self.stdout.write(f"EXPORT - filename    : '{filename}'")

        parsed_uri = urlparse(s3_uri)
        s3_bucket_name = parsed_uri.netloc
        s3_folder = parsed_uri.path.strip("/")
        query = Cache.objects.all()
        if data_model_names:
            query = query.filter(key_0__in=data_model_names)

        try:
            export_data_for_model(
                query,
                "id",
                batch_size,
                get_parquet_writer(filename)
                if format == "parquet"
                else get_jsonl_writer(filename),
                jsonfields_as_str=(format == "parquet"),
            )

            self.stdout.write(
                self.style.SUCCESS(f"EXPORT - Data exported to '{filename}'")
            )

            upload_to_s3(filename, s3_folder, s3_bucket_name, extra_args)

            self.stdout.write(
                self.style.SUCCESS(
                    f"EXPORT - Data uploaded to '{s3_bucket_name}/{s3_folder}/{filename}'"
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"EXPORT - Error when exporting data '{e}'")
            )
            self.stdout.write(self.style.ERROR(traceback.format_exc()))

"""Ceramic Cache API"""

from typing import List, Any
from django.conf import settings
from ninja import Router, Schema
from ninja.security import APIKeyHeader
from .exceptions import InvalidDeleteCacheRequestException
from datetime import datetime

from .models import CeramicCache

router = Router()


def get_utc_time():
    return datetime.utcnow()


class CacheStampPayload(Schema):
    address: str
    provider: str
    stamp: Any


class DeleteStampPayload(Schema):
    address: str
    provider: str


class DeleteStampResponse(Schema):
    address: str
    provider: str
    status: str


class CachedStampResponse(Schema):
    address: str
    provider: str
    stamp: Any


class GetStampResponse(Schema):
    success: bool
    stamps: List[CachedStampResponse]


@router.post(
    "stamp",
    response={201: CachedStampResponse},
)
def cache_stamp(_, payload: CacheStampPayload):
    try:
        stamp, created = CeramicCache.objects.update_or_create(
            address=payload.address,
            provider=payload.provider,
            defaults=dict(
                stamp=payload.stamp,
                deleted_at=None,
            ),
        )
        return stamp
    except Exception as e:
        raise e


@router.delete(
    "stamp",
    response=DeleteStampResponse,
)
def soft_delete_stamp(_, payload: DeleteStampPayload):
    try:
        stamp = CeramicCache.objects.get(
            address=payload.address,
            provider=payload.provider,
        )
        stamp.deleted_at = get_utc_time()
        stamp.save()

        return DeleteStampResponse(
            address=stamp.address,
            provider=stamp.provider,
            status="deleted",
        )
    except Exception as e:
        raise InvalidDeleteCacheRequestException()


@router.get(
    "stamp",
    response=GetStampResponse,
)
def get_stamps(_, address):
    try:
        stamps = CeramicCache.objects.filter(deleted_at=None, address=address)
        return GetStampResponse(
            success=True,
            stamps=[
                CachedStampResponse(
                    address=stamp.address, provider=stamp.provider, stamp=stamp.stamp
                )
                for stamp in stamps
            ],
        )
    except Exception as e:
        raise e

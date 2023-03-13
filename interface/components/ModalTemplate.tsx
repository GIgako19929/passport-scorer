// --- React components/methods
import React from "react";

// --- Style/UI Components
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Button,
} from "@chakra-ui/react";

type ModalProps = {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  size?: {};
  children?: React.ReactNode;
};

const ModalTemplate = ({
  isOpen,
  onClose,
  size,
  title,
  children,
}: ModalProps): JSX.Element => {
  return (
    <>
      <Modal isOpen={isOpen} size={size} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{title}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>{children}</ModalBody>
        </ModalContent>
      </Modal>
    </>
  );
};

export default ModalTemplate;

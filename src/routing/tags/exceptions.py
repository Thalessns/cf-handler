"""Exceptions for tag-related operations."""
from fastapi import status

from src.app.exceptions import CustomException


class TagNotFoundException(CustomException):
    """Exception raised when a tag is not found."""

    STATUS_CODE: int = status.HTTP_404_NOT_FOUND
    DETAIL: str = "Tag with id '{id}' was not found."


class TagAlreadyExistsException(CustomException):
    """Exception raised when a tag already exists."""

    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    DETAIL: str = "Tag with id '{id}' already exists."

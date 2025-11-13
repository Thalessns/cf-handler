"""Exceptions related to music operations."""

from fastapi import status

from src.app.exceptions import CustomException


class MusicNotFoundException(CustomException):
    """Exception raised when a music entry is not found."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Music with ID {music_id} not found."


class MusicAlreadyExistsException(CustomException):
    """Exception raised when a music entry already exists."""

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Music with name '{name}' already exists."

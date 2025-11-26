"""Exceptions related to routine operations."""

from fastapi import status

from src.app.exceptions import CustomException


class TagRoutineAlreadyExistsException(CustomException):
    """Exception raised when a routine for a tag already exists."""

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "A routine for tag ID {tag_id} already exists."


class RoutineNotFoundException(CustomException):
    """Exception raised when a routine entry is not found."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Routine with ID {routine_id} not found."


class TagHasNoRoutinesException(CustomException):
    """Exception raised when a tag has no associated routines."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Tag with ID {tag_id} has no associated routines."

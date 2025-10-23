"""Custom exceptions for the application."""
from fastapi import HTTPException, status


class CustomException(HTTPException):
    """Base class for custom exceptions."""

    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    DETAIL: str = "A custom exception occurred."

    def __init__(self, **kwargs):
        """Initialize the custom exception with predefined status code 
        and detail."""
        super().__init__(
            status_code=self.STATUS_CODE, 
            detail=self.DETAIL.format(**kwargs)
        )

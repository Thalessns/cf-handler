"""Schemas for tag-related operations."""
from pydantic import BaseModel


class TagRequest(BaseModel):
    """Schema for tag creation or update requests."""

    id: str


class TagResponse(BaseModel):
    """Schema for tag response."""

    id: str
    key: str
    first_use: str
    last_use: str | None

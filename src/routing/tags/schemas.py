"""Schemas for tag-related operations."""
from pydantic import BaseModel


class TagRequest(BaseModel):
    """Schema for tag creation or update requests."""

    tag_id: str
    name: str
    led_color: str | None = None
    music_id: int | None = None


class TagResponse(TagRequest):
    """Schema for tag response."""

    first_use: str
    last_use: str | None

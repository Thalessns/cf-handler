"""Schemas for music operations."""

from pydantic import BaseModel


class MusicRequest(BaseModel):
    """Schema for music request data."""

    name: str
    content: str


class Music(BaseModel):
    """Schema for music data."""

    music_id: int
    name: str
    content: str

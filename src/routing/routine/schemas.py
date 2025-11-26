"""Schemas for routine operations."""

from pydantic import BaseModel, field_validator
from typing import Literal


class RoutineRequest(BaseModel):
    """Schema for routine request."""

    tag_id: str
    start_time: str
    end_time: str
    weekday: Literal[
        "segunda-feira", 
        "terça-feira", 
        "quarta-feira", 
        "quinta-feira", 
        "sexta-feira", 
        "sabado", 
        "domingo"
    ]

    @field_validator("start_time", "end_time", mode="before")
    def validate_time_format(cls, value: str) -> str:
        """Validate that the time is in HH:MM format."""
        if len(value) != 5 or value[2] != ':' or not value.replace(':', '').isdigit():
            raise ValueError("Time must be in HH:MM format")
        hours, minutes = map(int, value.split(':'))
        if not (0 <= hours < 24) or not (0 <= minutes < 60):
            raise ValueError("Invalid time value")
        return value.lower()

    @field_validator("weekday", mode="before")
    def validate_weekday(cls, value: str) -> str:
        """Validate that the weekday is one of the allowed values."""
        return value.strip().lower()


class RoutineResponse(RoutineRequest):
    """Schema for routine response."""

    routine_id: int

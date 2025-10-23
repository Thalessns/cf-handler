"""Utility functions for tag management."""

from datetime import datetime


class TagUtils:
    """Utility functions for tag management."""

    @staticmethod
    def get_timestamp() -> str:
        """Get the current timestamp in ISO format.

        Returns:
            str: The current timestamp.
        """
        return datetime.now().isoformat()

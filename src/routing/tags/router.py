"""Roter for tag-related endpoints."""
from fastapi import APIRouter, status

from src.routing.tags.schemas import TagRequest, TagResponse
from src.routing.tags.service import tag_service

tag_router = APIRouter()
prefix = "/tag"


@tag_router.post(prefix+"/handle", status_code=status.HTTP_201_CREATED)
async def handle_tag(tag: TagRequest) -> None:
    """Endpoint to create or update a tag history.

    Args:
        tag (TagRequest): The tag data to create or retrieve.
    """
    await tag_service.handle_tag(tag)


@tag_router.post(prefix, status_code=status.HTTP_201_CREATED)
async def create_tag(new_tag: TagRequest) -> None:
    """Endpoint to create a new tag.

    Args:
        new_tag (TagRequest): The tag data to create.
    """
    await tag_service.create_tag(new_tag)


@tag_router.get(prefix)
async def get_tag(id: str) -> TagResponse:
    """Endpoint to retrieve a tag by its ID.

    Args:
        id (str): The ID of the tag to retrieve.

    Returns:
        TagResponse: The retrieved tag data.
    """
    return await tag_service.get_tag_by_id(id)


@tag_router.get(prefix+"/history")
async def get_tag_history(id: str) -> list[dict]:
    """Endpoint to retrieve the history of a tag by its ID.

    Args:
        id (str): The ID of the tag whose history to retrieve.

    Returns:
        list: The history of the tag.
    """
    return await tag_service.get_tag_history(id)

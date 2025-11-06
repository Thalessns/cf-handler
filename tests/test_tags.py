"""Tests for tags service."""

import pytest
from fastapi import status

from httpx import AsyncClient

from src.routing.tags.exceptions import (
    TagAlreadyExistsException,
    TagNotFoundException
)


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_handle_tag_request(client: AsyncClient):
    """Test handling a tag request."""

    tag_data = {"id": "test-tag-id"}
    response = await client.post("/tag/handle", json=tag_data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_create_tag(client: AsyncClient):
    """Test creating a new tag."""

    tag_data = {"id": "new-tag-id"}
    response = await client.post("/tag", json=tag_data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_tag_already_exists(client: AsyncClient):
    """Test handling an existing tag request."""

    tag_data = {"id": "existing-tag-id"}
    # First, create the tag
    await client.post("/tag", json=tag_data)
    # Now, we cant get the exception
    response = await client.post("/tag", json=tag_data)
    assert response.status_code == TagAlreadyExistsException.STATUS_CODE
    assert response.json().get("detail") == TagAlreadyExistsException.DETAIL.format(id="existing-tag-id")


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_get_tag(client: AsyncClient):
    """Test retrieving a tag by ID."""

    tag_id = "new-tag-id"
    response = await client.get(f"/tag?id={tag_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("id") == tag_id


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_get_tag_not_found(client: AsyncClient):
    """Test retrieving a non-existent tag."""

    tag_id = "non-existent-tag-id"
    response = await client.get(f"/tag?id={tag_id}")
    assert response.status_code == TagNotFoundException.STATUS_CODE
    assert response.json().get("detail") == TagNotFoundException.DETAIL.format(id=tag_id)

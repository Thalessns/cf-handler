"""Router for music operations."""

from fastapi import APIRouter, status

from src.routing.music.schemas import Music, MusicRequest
from src.routing.music.service import music_service

music_router = APIRouter()
prefix = "/music"


@music_router.post(prefix, status_code=status.HTTP_201_CREATED)
async def create_music(music_data: MusicRequest) -> None:
    """Endpoint to create a new music entry.

    Args:
        music_data (MusicRequest): The music data to create.

    Returns:
        Music: The created music data.
    """
    return await music_service.create_music(music_data)


@music_router.get(prefix + "s")
async def get_all_musics() -> list[Music]:
    """Endpoint to retrieve all music entries.

    Returns:
        list[Music]: A list of all music data.
    """
    return await music_service.get_all_musics()

@music_router.get(prefix)
async def get_music(music_id: int) -> Music:
    """Endpoint to retrieve music by its ID.

    Args:
        music_id (int): The ID of the music to retrieve.

    Returns:
        Music: The retrieved music data.
    """
    return await music_service.get_music_by_id(music_id)

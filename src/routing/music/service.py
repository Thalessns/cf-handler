"""Service moduele for music operations."""

from sqlalchemy.exc import IntegrityError

from src.database.database import Database
from src.database.tables import music_table
from src.routing.music.exceptions import (
    MusicAlreadyExistsException,
    MusicNotFoundException
)
from src.routing.music.schemas import (
    Music,
    MusicRequest
)


class MusicService:
    """Service class for music operations.""" 

    @classmethod
    async def create_music(cls, music_data: MusicRequest) -> None:
        """Create a new music entry.

        Args:
            music_data (MusicRequest): The music data to create.
        """
        try:
            music_query = music_table.insert().values(
                name=music_data.name,
                content=music_data.content
            ).returning(
                music_table.c.name,
                music_table.c.content
            )
            await Database.execute(music_query)
        except IntegrityError as e:
            raise MusicAlreadyExistsException(name=music_data.name) from e
    
    @classmethod
    async def get_all_musics(cls) -> list[Music]:
        """Retrieve all music entries.

        Returns:
            list[Music]: A list of all music data.
        """
        music_query = music_table.select()
        results = await Database.fetch_all(music_query)
        return [
            Music(
                music_id=record.music_id,
                name=record.name,
                content=record.content
            ) for record in results
        ]

    @classmethod
    async def get_music_by_id(cls, music_id: int) -> Music:
        """Retrieve music by its ID.

        Args:
            music_id (int): The ID of the music to retrieve.

        Raises:
            Exception: If the music with the given ID is not found.
        """
        music_query = music_table.select().where(
            music_table.c.music_id == music_id
        )
        result = await Database.fetch_one(music_query)
        if not result:
            raise MusicNotFoundException(music_id=music_id)
        return Music(
            music_id=result.music_id,
            name=result.name,
            content=result.content
        )


music_service = MusicService()

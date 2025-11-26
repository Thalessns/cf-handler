"""Service related to routine operations."""

from src.database.database import Database
from src.database.tables import routine_table
from src.routing.routine.schemas import RoutineRequest, RoutineResponse
from src.routing.routine.exceptions import RoutineNotFoundException, TagRoutineAlreadyExistsException


class RoutineService:
    """Service class for routine operations."""

    @classmethod
    async def create_routine(cls, routine: RoutineRequest) -> None:
        """Create a new routine in the database.
        
        Args:
            routine (RoutineRequest): The routine data to be created.
        """
        if await cls.tag_routine_exists(routine.tag_id):
            raise TagRoutineAlreadyExistsException(tag_id=routine.tag_id)
        query = routine_table.insert().values(
            tag_id=routine.tag_id,
            start_time=routine.start_time,
            end_time=routine.end_time,
            weekday=routine.weekday
        )
        await Database.execute(query)

    @classmethod
    async def get_routine_by_tag(cls, tag_id: str) -> RoutineResponse:
        """Retrieve all routines associated with a specific tag ID.

        Args:
            tag_id (str): The tag ID to filter routines.

        Returns:
            RoutineResponse: A routine associated with the tag ID.

        Raises:
            RoutineNotFoundException: If no routines are found for the given tag ID.
        """
        query = routine_table.select().where(routine_table.c.tag_id == tag_id)
        result = await Database.fetch_one(query)
        if not result:
            raise RoutineNotFoundException(routine_id=tag_id)
        return RoutineResponse(**result)

    @classmethod
    async def tag_routine_exists(cls, tag_id: str) -> bool:
        """Check if any routine exists for a given tag ID.

        Args:
            tag_id (str): The tag ID to check.

        Returns:
            bool: True if at least one routine exists for the tag ID, False otherwise.
        """
        query = routine_table.select().where(routine_table.c.tag_id == tag_id)
        result = await Database.fetch_one(query)
        return result is not None


routine_service = RoutineService()

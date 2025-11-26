"""Router for routine-related operations."""

from fastapi import APIRouter, status

from src.routing.routine.schemas import RoutineRequest, RoutineResponse
from src.routing.routine.service import RoutineService

prefix = "/routine"
routine_router = APIRouter()


@routine_router.post(prefix, status_code=status.HTTP_201_CREATED)
async def create_routine(routine: RoutineRequest) -> None:
    """Create a new routine.
    
    Args:
        routine (RoutineRequest): The routine data to create.
    """
    await RoutineService.create_routine(routine)


@routine_router.get(prefix, response_model=RoutineResponse)
async def get_routines_by_tag(tag_id: str) -> RoutineResponse:
    """Get routines by tag.
    
    Args:
        tag_id (str): The tag to filter routines by.
    
    Returns:
        list[RoutineResponse]: A list of routines with the specified tag.
    """
    return await RoutineService.get_routine_by_tag(tag_id)

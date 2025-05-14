"""Module to handle subject endpoint responses"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlmodel import Session

from aind_labtracks_service_server.handler import SessionHandler
from aind_labtracks_service_server.models import HealthCheck, Subject
from aind_labtracks_service_server.session import get_session

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/subject/{subject_id}",
    response_model=List[Subject],
)
async def get_subject(
    subject_id: str = Path(..., examples=["632269"]),
    session: Session = Depends(get_session),
):
    """
    ## Subject metadata
    Retrieves subject information from LabTracks.
    """
    lab_tracks_subjects = SessionHandler(session=session).get_subject_view(
        subject_id=subject_id
    )
    if len(lab_tracks_subjects) == 0:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return lab_tracks_subjects

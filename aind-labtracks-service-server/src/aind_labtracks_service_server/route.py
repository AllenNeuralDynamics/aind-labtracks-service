"""Module to handle subject endpoint responses"""

from typing import List

from fastapi import APIRouter, Depends, Path, status
from sqlmodel import Session

from aind_labtracks_service_server.handler import SessionHandler
from aind_labtracks_service_server.models import (
    HealthCheck,
    Subject,
    Task,
)
from aind_labtracks_service_server.session import get_session

router = APIRouter()


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
    operation_id="get_health",
)
def get_health() -> HealthCheck:
    """
    Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/subject/{subject_id}",
    response_model=List[Subject],
    operation_id="get_subject",
)
def get_subject(
    subject_id: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample subject ID",
                "description": "Example subject ID for LabTracks",
                "value": "632269",
            }
        },
    ),
    session: Session = Depends(get_session),
):
    """
    ## Subject metadata
    Retrieves subject information from LabTracks.
    """
    lab_tracks_subjects = SessionHandler(session=session).get_subject_view(
        subject_id=subject_id
    )
    return lab_tracks_subjects


@router.get(
    "/subject_by_protocol_number/{protocol_number}",
    response_model=List[Subject],
    operation_id="get_subject_by_protocol_number",
)
def get_subject_by_protocol_number(
    protocol_number: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A protocol number",
                "description": "Example protocol number to use.",
                "value": "0401",
            }
        },
    ),
    session: Session = Depends(get_session),
):
    """
    ## Subject metadata
    Retrieves subject information from LabTracks.
    """
    lab_tracks_subjects = SessionHandler(
        session=session
    ).get_subject_view_by_protocol(protocol_number=protocol_number)
    return lab_tracks_subjects


@router.get(
    "/tasks/{subject_id}", response_model=List[Task], operation_id="get_tasks"
)
def get_tasks(
    subject_id: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample subject ID",
                "description": "Example subject ID for LabTracks",
                "value": "632269",
            }
        },
    ),
    session: Session = Depends(get_session),
):
    """
    ## Task metadata
    Retrieves Task information from LabTracks.
    """
    lab_tracks_tasks = SessionHandler(session=session).get_task_view(
        subject_id=subject_id
    )
    return lab_tracks_tasks

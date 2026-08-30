"""Starts and runs a FastAPI Server"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from aind_labtracks_service_server import __version__ as service_version
from aind_labtracks_service_server.route import router

log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=log_level)

description = """
## aind-labtracks-service

Service to fetch data from LabTracks.

"""

# noinspection PyTypeChecker
app = FastAPI(
    title="aind-labtracks-service",
    description=description,
    summary="Serves data from LabTracks.",
    version=service_version,
)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(router)

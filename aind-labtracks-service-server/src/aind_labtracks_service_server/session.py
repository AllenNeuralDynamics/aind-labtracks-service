"""Module to handle LabTracks database session"""

from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine

from aind_labtracks_service_server.configs import Settings

# Settings will be pulled from env
settings = Settings()

engine = create_engine(url=settings.db_connection_str)

session_local = sessionmaker(
    bind=engine, class_=Session, expire_on_commit=False
)


def get_session():
    """
    Yield a session object. This will automatically close the session when
    finished.
    """
    session = session_local()
    try:
        yield session
    finally:
        session.close()

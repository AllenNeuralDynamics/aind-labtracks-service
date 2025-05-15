"""Set up fixtures to be used across all test modules."""

import json
import os
from datetime import datetime
from decimal import Decimal
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

from aind_labtracks_service_server.main import app
from aind_labtracks_service_server.models import (
    AcucProtocol,
    AnimalsCommon,
    Groups,
    MouseCustomClass,
    Procedure,
    Species,
    Subject,
    TaskSet,
    TaskSetObject,
    TaskType,
)
from aind_labtracks_service_server.session import get_session as get_lb_session

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


@pytest.fixture(scope="module")
def test_labtracks_subject():
    """A common lab_tracks subject pulled from their db"""
    return Subject(
        id=Decimal("632269.0000000000"),
        class_values=MouseCustomClass(
            reserved_by="Person A",
            reserved_date="2022-07-14T00:00:00-07:00",
            reason=None,
            solution="1xPBS",
            full_genotype="Pvalb-IRES-Cre/wt;RCL-somBiPoles_mCerulean-WPRE/wt",
            phenotype=(
                "P19: TSTW. Small body, large head, slightly dehydrated. "
                "3.78g. P22: 5.59g. P26: 8.18g. Normal body proportions. "
            ),
        ),
        sex="F",
        birth_date=datetime(2022, 5, 1, 0, 0),
        species_name="mouse",
        cage_id=Decimal("-99999999999999.0000000000"),
        room_id=Decimal("-99999999999999.0000000000"),
        paternal_id=Decimal("623236.0000000000"),
        paternal_class_values=MouseCustomClass(
            reserved_by="Person One ",
            reserved_date="2022-11-01T00:00:00",
            reason="eu-retire",
            solution=None,
            full_genotype="RCL-somBiPoles_mCerulean-WPRE/wt",
            phenotype="P87: F.G. P133: Barberer. ",
        ),
        maternal_id=Decimal("615310.0000000000"),
        maternal_class_values=MouseCustomClass(
            reserved_by="Person One ",
            reserved_date="2022-08-03T00:00:00",
            reason="Eu-retire",
            solution=None,
            full_genotype="Pvalb-IRES-Cre/wt",
            phenotype="P100: F.G.",
        ),
        group_name="Exp-ND-01-001-2109",
        group_description="BALB/c",
    )


@pytest.fixture(scope="module")
def test_labtracks_procedure():
    """A common lab_tracks subject pulled from their db"""
    return Procedure(
        id=Decimal("2356051.0000000000"),
        type_name="Tattoo/Tail Tip",
        date_start=datetime(2022, 5, 10, 14, 9, 22, 157000),
        date_end=datetime(2022, 5, 10, 14, 39, 22, 157000),
        investigator_id=Decimal("30046.0000000000"),
        task_object=Decimal("632269.0000000000"),
        protocol_number="2116",
        protocol_title="Mouse Breeding",
        task_status="F",
        task_description=(
            "If pups are added to litter,"
            " adjust all tasks associated with the litter."
        ),
    )


@pytest.fixture(scope="session")
def get_labtracks_session():
    """Generate a sqlite database to query lab_tracks data."""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        echo=True,
    )
    SQLModel.metadata.create_all(engine)
    session_local = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    session = session_local()
    # Load sqlite db with test data
    with open(RESOURCES_DIR / "test_db.json", "r") as f:
        test_db = json.load(f)
    for ac_row in test_db["animals_common"]:
        ac = AnimalsCommon.model_validate(ac_row)
        session.add(ac)
    for g_row in test_db["groups"]:
        g = Groups.model_validate(g_row)
        session.add(g)
    for s_row in test_db["species"]:
        s = Species.model_validate(s_row)
        session.add(s)
    for ts_row in test_db["task_set"]:
        ts = TaskSet.model_validate(ts_row)
        session.add(ts)
    for tso_row in test_db["task_set_object"]:
        tso = TaskSetObject.model_validate(tso_row)
        session.add(tso)
    for tt_row in test_db["task_type"]:
        tt = TaskType.model_validate(tt_row)
        session.add(tt)
    for ap_row in test_db["acuc_protocol"]:
        ap = AcucProtocol.model_validate(ap_row)
        session.add(ap)
    session.commit()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture(scope="session")
def client(get_labtracks_session):
    """Override a dependency required by the FastAPI app."""

    def override_get_session():
        """Override standard session with the one for tests."""
        yield get_labtracks_session

    app.dependency_overrides[get_lb_session] = override_get_session
    FastAPICache.init(InMemoryBackend())
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
    app.dependency_overrides.clear()

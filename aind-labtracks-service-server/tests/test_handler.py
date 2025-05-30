"""Tests for handler module"""

import pytest

from aind_labtracks_service_server.handler import SessionHandler


class TestHandler:
    """Test SessionHandler"""

    def test_constructor(self, get_labtracks_session):
        """Tests class can be constructed."""
        session_handler = SessionHandler(get_labtracks_session)
        assert session_handler is not None

    def test_get_subject_value(
        self, get_labtracks_session, test_labtracks_subject
    ):
        """Tests subject view is returned correctly."""
        session_handler = SessionHandler(get_labtracks_session)
        subject = session_handler.get_subject_view(subject_id="632269")
        assert test_labtracks_subject == subject[0]

    def test_get_task_value(self, get_labtracks_session, test_labtracks_task):
        """Tests task view is returned correctly."""
        session_handler = SessionHandler(get_labtracks_session)
        tasks = session_handler.get_task_view(subject_id="632269")
        assert test_labtracks_task == tasks[0]


if __name__ == "__main__":
    pytest.main([__file__])

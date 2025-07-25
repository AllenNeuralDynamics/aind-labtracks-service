"""Test routes"""

from unittest.mock import patch

import pytest


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]


class TestSubjectRoute:
    """Test subject responses."""

    def test_get_200_subject(
        self, client, get_labtracks_session, test_labtracks_subject
    ):
        """Tests a good response"""
        response = client.get("/subject/632269")
        assert 200 == response.status_code
        assert [
            test_labtracks_subject.model_dump(mode="json")
        ] == response.json()

    def test_500_internal_server_error(
        self, client, get_labtracks_session, caplog
    ):
        """Tests an internal server error response"""

        with patch(
            "aind_labtracks_service_server.handler.SessionHandler"
            ".get_subject_view",
            side_effect=Exception("Something went wrong"),
        ):
            response = client.get("/subject/1234")

        assert 500 == response.status_code


class TestTasksRoute:
    """Test tasks responses."""

    def test_get_200_tasks(
        self, client, get_labtracks_session, test_labtracks_task
    ):
        """Tests a good response"""
        response = client.get("/tasks/632269")
        assert 200 == response.status_code
        assert [test_labtracks_task.model_dump(mode="json")] == response.json()

    def test_500_internal_server_error(
        self, client, get_labtracks_session, caplog
    ):
        """Tests an internal server error response"""

        with patch(
            "aind_labtracks_service_server.handler.SessionHandler"
            ".get_task_view",
            side_effect=Exception("Something went wrong"),
        ):
            response = client.get("/tasks/1234")

        assert 500 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])

"""Module to test main app"""

import pytest


class TestMain:
    """Tests app endpoints"""

    def test_get_healthcheck(self, client):
        """Tests healthcheck"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    def test_get_subject(self, client, get_labtracks_session):
        """Tests subject"""
        response = client.get("/subject/632269")
        assert 200 == response.status_code


if __name__ == "__main__":
    pytest.main([__file__])

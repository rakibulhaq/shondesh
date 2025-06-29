import pytest
from shondesh.formatters.slack_message_formatter import (
    SlackMessageFormatter as SlackFormatter,
)


@pytest.fixture
def slack_data():
    return {
        "message": "Test message",
        "severity": "info",
        "extra": {"foo": "bar"},
        "timestamp": "2023-10-01T12:00:00Z",
    }


def test_slack_formatter_basic(slack_data):
    formatter = SlackFormatter()
    formatted = formatter.format(slack_data)
    assert isinstance(formatted, list)
    assert formatted
    assert any(field["title"] == "message" for key, field in enumerate(formatted))


def test_slack_formatter_severity(slack_data):
    formatter = SlackFormatter()
    slack_data["severity"] = "critical"
    formatted = formatter.format(slack_data)
    assert "danger" in str(formatted).lower() or "critical" in str(formatted).lower()


def test_slack_formatter_extra_fields(slack_data):
    formatter = SlackFormatter()
    formatted = formatter.format(slack_data)
    assert formatted
    assert any(field["title"] == "extra" for key, field in enumerate(formatted))
    assert any(field["value"] == "{'foo': 'bar'}" for field in formatted)

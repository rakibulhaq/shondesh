import pytest
from shondesh.channels.slack import Slack
from shondesh.utils.constants import Severity


@pytest.fixture
def slack_config():
    return {
        "channel": "#alerts",
        "username": "AlertBot",
        "icon_emoji": ":robot_face:",
        "webhook_url": "https://hooks.slack.com/services/test",
        "mention_users": ["@user1", "@user2"],
    }


@pytest.fixture
def slack_channel(slack_config):
    return Slack(config=slack_config)


@pytest.mark.asyncio
async def test_send_success(mocker, slack_channel):
    mocker.patch.object(
        slack_channel, "send", mocker.AsyncMock(return_value={"ok": True})
    )

    data = {"severity": Severity.INFO, "message": "Test"}
    result = await slack_channel.send(data)
    assert result.get("ok") is True
    slack_channel.send.assert_awaited_once_with(data)


@pytest.mark.asyncio
async def test_send_failure_status(mocker, slack_channel):
    mocker.patch.object(
        slack_channel, "send", mocker.AsyncMock(return_value={"ok": False})
    )

    data = {"severity": Severity.INFO, "message": "Test"}
    result = await slack_channel.send(data)
    assert result.get("ok") is False


@pytest.mark.asyncio
async def test_send_exception(mocker, slack_channel):
    mock_session = mocker.MagicMock()
    mock_session.__aenter__.side_effect = Exception("Connection error")
    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    data = {"severity": Severity.INFO, "message": "Test"}
    result = await slack_channel.send(data)
    assert result is False

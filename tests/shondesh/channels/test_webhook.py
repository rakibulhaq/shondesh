import pytest
from shondesh.channels.webhook import Webhook


@pytest.fixture
def webhook_config():
    return {
        "url": "https://example.com/webhook",
        "method": "POST",
        "headers": {"Authorization": "Bearer testtoken"},
        "retry_count": 1,
    }


@pytest.fixture
def webhook_channel(webhook_config):
    return Webhook(config=webhook_config)


@pytest.mark.asyncio
async def test_send_success(mocker, webhook_channel):
    mock_response = mocker.MagicMock()
    mock_response.status = 200
    mock_request = mocker.AsyncMock(return_value=mock_response)
    mock_session = mocker.MagicMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.request = mock_request
    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    data = {"message": "Test"}
    result = await webhook_channel.send(data)
    assert result is True
    mock_request.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_failure_status(mocker, webhook_channel):
    mock_response = mocker.MagicMock()
    mock_response.status = 500
    mock_request = mocker.AsyncMock(return_value=mock_response)
    mock_session = mocker.MagicMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.request = mock_request
    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    data = {"message": "Test"}
    result = await webhook_channel.send(data)
    assert result is False


@pytest.mark.asyncio
async def test_send_exception(mocker, webhook_channel):
    mock_session = mocker.MagicMock()
    mock_session.__aenter__.side_effect = Exception("Connection error")
    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    data = {"message": "Test"}
    result = await webhook_channel.send(data)
    assert result is False


@pytest.mark.asyncio
async def test_send_env_header(monkeypatch, webhook_config, mocker):
    webhook_config["headers"] = {"Authorization": "${WEBHOOK_TOKEN}"}
    monkeypatch.setenv("WEBHOOK_TOKEN", "envtoken")
    channel = Webhook(config=webhook_config)

    mock_response = mocker.MagicMock()
    mock_response.status = 200
    mock_request = mocker.AsyncMock(return_value=mock_response)
    mock_session = mocker.MagicMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.request = mock_request
    mocker.patch("aiohttp.ClientSession", return_value=mock_session)

    data = {"message": "Test"}
    result = await channel.send(data)
    assert result is True
    _, kwargs = mock_request.call_args
    assert kwargs["headers"]["Authorization"] == "envtoken"

import pytest
from shondesh.channels.telegram import Telegram


@pytest.fixture
def telegram_channel():
    # Replace with actual config or use mock values
    config = {
        "token": "dummy-token",
        "chat_id": "dummy-chat-id",
        "webhook_url": "https://dummy-webhook-url",
    }
    return Telegram(config)


def test_telegram_initialization(telegram_channel):
    assert telegram_channel is not None
    assert isinstance(telegram_channel, Telegram)
    assert telegram_channel.config is not None
    assert "token" in telegram_channel.config
    assert "chat_id" in telegram_channel.config
    assert "webhook_url" in telegram_channel.config


def test_telegram_initialization_missing_config():
    with pytest.raises(ValueError):
        Telegram(config={})  # Should raise an error due to missing token and chat_id


def test_raises_value_error_when_chat_id_is_missing():
    config = {"webhook_url": "https://example.com/telegram"}
    with pytest.raises(
        ValueError, match="Telegram chat ID is required in the configuration."
    ):
        Telegram(config=config)


def test_does_not_raise_error_when_chat_id_is_present():
    config = {"webhook_url": "https://example.com/telegram", "chat_id": "12345"}
    channel = Telegram(config=config)
    assert channel.config["chat_id"] == "12345"


def test_telegram_properties(telegram_channel):
    assert telegram_channel is not None
    assert telegram_channel.config is not None
    assert "token" in telegram_channel.config
    assert "chat_id" in telegram_channel.config


@pytest.mark.asyncio
async def test_telegram_send_message(mocker, telegram_channel):
    message = {"msg": "Test message", "severity": "info"}
    mocker.patch.object(telegram_channel, "send", return_value={"ok": True})
    response = await telegram_channel.send(message)
    assert response is not None
    assert response.get("ok") is True


@pytest.mark.asyncio
async def test_telegram_send_message_failure(mocker, telegram_channel):
    message = {"msg": "Test message", "severity": "info"}
    mocker.patch.object(telegram_channel, "send", return_value={"ok": False})
    response = await telegram_channel.send(message)
    assert response is not None
    assert response.get("ok") is False


@pytest.mark.asyncio
async def test_telegram_send_message_exception(mocker, telegram_channel):
    message = {"msg": "Test message", "severity": "info"}
    mocker.patch.object(
        telegram_channel, "send", side_effect=Exception("Network error")
    )
    with pytest.raises(Exception):
        await telegram_channel.send(message)

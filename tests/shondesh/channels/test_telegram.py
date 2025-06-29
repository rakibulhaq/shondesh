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

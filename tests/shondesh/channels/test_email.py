import pytest
from shondesh.channels.email import Email


@pytest.fixture
def email_config():
    return {
        "from_address": "sender@example.com",
        "recipients": ["recipient@example.com"],
        "subject_template": "Test Subject",
        "password": "testpassword",
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "username": "user@example.com",
    }


@pytest.fixture
def email_channel(email_config):
    return Email(config=email_config)


def test_email_properties(email_channel, email_config):
    assert email_channel.config == email_config


@pytest.mark.asyncio
async def test_send_success(mocker, email_channel):
    mock_smtp = mocker.patch("smtplib.SMTP", autospec=True)
    data = {"key": "value"}
    result = await email_channel.send(data)
    assert result
    mock_smtp.assert_called_with(
        email_channel.config["smtp_server"], email_channel.config["smtp_port"]
    )
    instance = mock_smtp.return_value
    instance.starttls.assert_called_once()
    instance.login.assert_called_once_with(
        email_channel.config["username"], email_channel.config["password"]
    )
    instance.sendmail.assert_called_once()
    instance.quit.assert_called_once()


@pytest.mark.asyncio
async def test_send_env_password(mocker, email_channel, email_config, monkeypatch):
    email_channel.config["password"] = "${EMAIL_PASSWORD}"
    monkeypatch.setenv("EMAIL_PASSWORD", "envpassword")
    mock_smtp = mocker.patch("smtplib.SMTP", autospec=True)
    data = {"key": "value"}
    result = await email_channel.send(data)
    assert result
    instance = mock_smtp.return_value
    instance.login.assert_called_once_with(
        email_channel.config["username"], "envpassword"
    )


@pytest.mark.asyncio
async def test_send_failure(mocker, email_channel):
    mocker.patch("smtplib.SMTP", side_effect=Exception("SMTP error"))
    data = {"key": "value"}
    result = await email_channel.send(data)
    assert result is False

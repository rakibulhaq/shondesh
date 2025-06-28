import pytest
from shondesh import ShondeshFactory


@pytest.mark.parametrize(
    "channel_type,patch_path",
    [
        ("email", "shondesh.channels.Email"),
        ("telegram", "shondesh.channels.Telegram"),
        ("slack", "shondesh.channels.Slack"),
        ("webhook", "shondesh.channels.Webhook"),
    ],
)
def test_create_channel_supported_types(mocker, channel_type, patch_path):
    mock_class = mocker.patch(patch_path, autospec=True)
    instance = mock_class.return_value
    result = ShondeshFactory.create_channel(channel_type, config={"key": "value"})
    mock_class.assert_called_once_with(config={"key": "value"})
    assert result == instance


def test_create_channel_unsupported_type():
    with pytest.raises(ValueError, match="Unsupported channel type"):
        ShondeshFactory.create_channel("unknown")

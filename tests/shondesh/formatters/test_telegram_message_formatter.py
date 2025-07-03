from shondesh.formatters.telegram_message_formatter import TelegramMessageFormatter


def test_returns_empty_string_when_message_is_none():
    formatter = TelegramMessageFormatter()
    assert formatter.format(None) == ""


def test_returns_empty_string_when_message_is_empty():
    formatter = TelegramMessageFormatter()
    assert formatter.format({}) == ""


def test_formats_message_with_special_characters_correctly():
    formatter = TelegramMessageFormatter()
    message = {"text": "Hello *world* _test_ [link](url)"}
    formatted_message = formatter.format(message)
    assert (
        "<b>text</b>: Hello \\*world\\* \\_test\\_ \\[link\\](url)" in formatted_message
    )


def test_escapes_html_characters_in_message():
    formatter = TelegramMessageFormatter()
    message = {"text": "<script>alert('XSS')</script>"}
    formatted_message = formatter.format(message)
    assert "&lt;script&gt;alert('XSS')&lt;/script&gt;" in formatted_message


def test_formats_message_with_multiple_keys_correctly():
    formatter = TelegramMessageFormatter()
    message = {"title": "Notification", "body": "This is a *test*"}
    formatted_message = formatter.format(message)
    assert "<b>title</b>: Notification" in formatted_message
    assert "<b>body</b>: This is a \\*test\\*" in formatted_message

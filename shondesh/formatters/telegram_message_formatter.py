from shondesh.formatters.base_formatter import Formatter


class TelegramMessageFormatter(Formatter):
    """
    A class to format messages for Telegram.
    """

    def format(self, message: dict) -> str:
        """
        Format the message for Telegram.

        Args:
            message (str): The message to format.

        Returns:
            str: The formatted message.
        """
        if not message:
            return ""

        for key, value in message.items():
            if isinstance(value, str):
                # Escape special characters for Telegram
                value = (
                    value.replace("_", "\\_")
                    .replace("*", "\\*")
                    .replace("[", "\\[")
                    .replace("]", "\\]")
                    .replace("`", "\\`")
                    .replace("~", "\\~")
                    .replace(">", "&gt;")
                    .replace("<", "&lt;")
                )
            message[key] = str(value)
        # Join the message parts with double newlines for better readability
        message = "\n".join(f"<b>{key}</b>: {value}" for key, value in message.items())
        # Wrap the message in a code block for Telegram
        message = f"<pre>{message}</pre>"

        return message

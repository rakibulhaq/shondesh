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

        formatted_message = {}

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
            formatted_message[key] = str(value)
        # Join the message parts with double newlines for better readability
        final_message = "\n".join(f"<b>{key}</b>: {value}" for key, value in formatted_message.items())
        # Wrap the message in a code block for Telegram
        final_message = f"<pre>{final_message}</pre>"

        return final_message

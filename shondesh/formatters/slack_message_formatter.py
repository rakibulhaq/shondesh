class SlackMessageFormatter:

    def format(self, message: dict) -> list:
        """
        Format the message for Slack.
        """
        if not message:
            return []

        # Escape special characters for Slack

        attachment_fields = []
        # Format the message with a code block
        for key, value in message.items():
            if isinstance(value, str):
                value = (
                    value.replace("`", "\\`").replace("*", "\\*").replace("_", "\\_")
                )
            attachment_fields.append({"title": key, "value": str(value), "short": True})

        return attachment_fields

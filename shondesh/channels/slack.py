from shondesh.channels.base import Channel, logger
from shondesh.formatters.base_formatter import Formatter
from shondesh.formatters.slack_message_formatter import SlackMessageFormatter
from shondesh.utils.constants import Severity


class Slack(Channel):
    """Slack alert channel implementation"""

    def __init__(self, config: dict, formatter: Formatter = SlackMessageFormatter()):
        super().__init__(config=config, formatter=formatter)

    async def send(self, data: dict) -> bool:
        import aiohttp

        try:
            severity = data.get("severity", Severity.INFO)
            payload = {
                "channel": self.config["channel"],
                "username": self.config["username"],
                "icon_emoji": self.config["icon_emoji"],
                "text": f"🚨 *{severity.value.upper()}*",
                "attachments": [
                    {
                        "color": (
                            "danger" if severity == Severity.CRITICAL else "warning"
                        ),
                        "fields": self.formatter.format(data) if self.formatter else [],
                    }
                ],
            }

            # Add mentions if configured
            if "mention_users" in self.config:
                payload["text"] = (
                    f"{' '.join(self.config['mention_users'])} {payload['text']}"
                )

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.config["webhook_url"], json=payload
                ) as response:
                    return response.status == 200
        except Exception as e:
            logger.error(f"Failed to send Slack alert: {e}")
            return False

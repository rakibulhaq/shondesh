from shondesh.channels.base import Channel, logger
from shondesh.formatters.base_formatter import Formatter
from shondesh.formatters.dict_table_formatter import DictTableFormatter


class Telegram(Channel):
    """Telegram alert channel implementation"""

    def __init__(self, config: dict, formatter: Formatter = DictTableFormatter()):
        super().__init__(config=config, formatter=formatter)
        self.config = config
        self.formatter = formatter

        if not self.config.get("webhook_url"):
            raise ValueError("Telegram webhook URL is required in the configuration.")
        if not self.config.get("chat_id"):
            raise ValueError("Telegram chat ID is required in the configuration.")

    async def send(self, data: dict) -> bool:
        import aiohttp

        try:
            payload = {
                "chat_id": self.config["chat_id"],
                "text": self.formatter.format(data),
                "parse_mode": "Markdown",
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.config["webhook_url"], json=payload
                ) as response:
                    return response.status == 200
        except Exception as e:
            logger.error(f"Failed to send Telegram alert: {e}")
            return False

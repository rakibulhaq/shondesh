import asyncio
import os

from shondesh.channels.base import Channel, logger
from shondesh.formatters.base_formatter import Formatter
from shondesh.formatters.dict_table_formatter import DictTableFormatter


class Webhook(Channel):
    """Webhook alert notifier implementation"""

    def __init__(self, config: dict, formatter: Formatter = DictTableFormatter()):
        super().__init__(config=config, formatter=formatter)
        self.config = config
        self.formatter = formatter

        if not self.config.get("url"):
            raise ValueError("Webhook URL is required in the configuration.")
        if not self.config.get("method"):
            self.config["method"] = "POST"

    async def send(self, data: dict) -> bool:
        import aiohttp

        try:
            headers = self.config.get("headers", {})
            # Replace environment variables in headers
            for key, value in headers.items():
                if (
                    isinstance(value, str)
                    and value.startswith("${")
                    and value.endswith("}")
                ):
                    env_var = value[2:-1]
                    headers[key] = os.getenv(env_var, value)

            payload = self.formatter.format(data)

            async with aiohttp.ClientSession() as session:
                for attempt in range(self.config.get("retry_count", 1)):
                    try:
                        response = await session.request(
                            self.config.get("method", "POST"),
                            self.config["url"],
                            json=payload,
                            headers=headers,
                        )
                        async with response:
                            if response.status < 400:
                                return True
                    except Exception as e:
                        if attempt == self.config.get("retry_count", 1) - 1:
                            raise e
                        await asyncio.sleep(1)

            return False
        except Exception as e:
            logger.error(f"Failed to send webhook alert: {e}")
            return False

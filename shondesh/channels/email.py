import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from shondesh.channels.base import Channel, logger
from shondesh.formatters.base_formatter import Formatter
from shondesh.formatters.dict_table_formatter import DictTableFormatter


class Email(Channel):
    """Email alert notifier implementation"""

    def __init__(
        self, config: dict = None, formatter: Formatter = DictTableFormatter()
    ):
        super().__init__(config=config, formatter=formatter)
        self.config = config
        self.formatter = formatter

    async def send(self, data: dict) -> bool:
        try:
            msg = MIMEMultipart()
            msg["From"] = self.config["from_address"]
            msg["To"] = ", ".join(self.config["recipients"])
            msg["Subject"] = self.config["subject_template"]

            body = self.formatter.format(data)

            msg.attach(MIMEText(body, "plain"))

            password = self.config["password"]
            if password.startswith("${") and password.endswith("}"):
                env_var = password[2:-1]
                password = os.getenv(env_var, password)

            server = smtplib.SMTP(self.config["smtp_server"], self.config["smtp_port"])
            server.starttls()
            server.login(self.config["username"], password)
            text = msg.as_string()
            server.sendmail(
                self.config["from_address"], self.config["recipients"], text
            )
            server.quit()

            return True
        except Exception as e:
            logger.error(f"Failed to send email alert: {e}")
            return False

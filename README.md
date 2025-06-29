# Shondesh

![Shondesh Logo](assets/shondesh.png)
[![PyPI version](https://badge.fury.io/py/shondesh.svg)](https://badge.fury.io/py/shondesh)
[![Python versions](https://img.shields.io/pypi/pyversions/shondesh.svg)](https://pypi.org/project/shondesh/)
[![Coverage Status](https://codecov.io/gh/rakibulhaq/shondesh/branch/main/graph/badge.svg)](https://codecov.io/gh/rakibulhaq/shondesh)
[![Snyk](https://snyk.io/test/github/rakibulhaq/shondesh/badge.svg)](https://snyk.io/test/github/rakibulhaq/shondesh)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/shondesh.svg?label=PyPI%20downloads)](https://pypistats.org/packages/shondesh)

"সন্দেশ" (pronounced shôndesh) in Bengali means news, message, or a type of sweet.

Shondesh is a Python package that provides a unified API for sending notifications across multiple channels. 

It supports Email, Telegram, Slack, and Webhook channels, allowing you to easily send messages without worrying about the underlying implementation details.

## Features

- Unified API for sending notifications  
- Pluggable channel support \(Email, Telegram, Slack, Webhook\)  
- Easy configuration and extension  

## Installation

```bash
pip install shondesh
```

or with Poetry:

```bash
poetry add shondesh
```

## Usage

```python
# Slack Example
from shondesh.channels.channel_factory import ChannelFactory

slack_channel = ChannelFactory.create_channel(
    "slack",
    webhook_url="https://hooks.slack.com/services/your/slack/webhook",
    channel="#general"
)
slack_channel.send("Hello from Shondesh!", username="Notifier")

# Telegram Example
telegram_channel = ChannelFactory.create_channel(
    "telegram",
    webhook_url="https://api.telegram.org/bot<token>/sendMessage",
    chat_id="123456789"
)
telegram_channel.send("Hello Telegram user!")

# Webhook Example
webhook_channel = ChannelFactory.create_channel(
    "webhook",
    url="https://example.com/webhook",
    method="POST",
    headers={"Authorization": "Bearer yourtoken"}
)
webhook_channel.send({"event": "deploy", "status": "success"})

# Email Example
email_channel = ChannelFactory.create_channel(
    "email",
    smtp_server="smtp.example.com",
    smtp_port=587,
    username="your@email.com",
    password="yourpassword"
)
email_channel.send(
    "Hello Email user!",
    to="recipient@example.com",
    subject="Notification from Shondesh"
)
```

## Configuration

Configuration can be provided via environment variables or directly as arguments to channel constructors.

## Supported Channels

- Email  
- Telegram  
- Slack  
- Webhook  

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

1. Fork the repository  
2. Create your feature branch \(`git checkout -b feature/fooBar`\)  
3. Commit your changes \(`git commit -am 'Add some fooBar'`\)  
4. Push to the branch \(`git push origin feature/fooBar`\)  
5. Create a new Pull Request  

## License

This project is licensed under the MIT License.

## Contact

For questions or support, open an issue on [GitHub](https://github.com/rakibulhaq/shondesh).
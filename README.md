# Shondesh

![Shondesh Logo](assets/shondesh.png)
[![PyPI version](https://badge.fury.io/py/shondesh.svg)](https://badge.fury.io/py/shondesh)
[![Coverage Status](https://codecov.io/gh/rakibulhaq/shondesh/branch/main/graph/badge.svg)](https://codecov.io/gh/rakibulhaq/shondesh)
[![Snyk](https://snyk.io/test/github/rakibulhaq/shondesh/badge.svg)](https://snyk.io/test/github/rakibulhaq/shondesh)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/shondesh.svg?label=PyPI%20downloads)](https://pypistats.org/packages/shondesh)

Send notifications via multiple channels \(Email, Telegram, Slack, Webhook\).

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
from shondesh.channels.channel_factory import ChannelFactory

channel = ChannelFactory.create_channel("email", smtp_server="smtp.example.com")
channel.send("Hello, world!", to="user@example.com")
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
```
This matches the badge and logo style used in `escalite`. Adjust badge URLs or logo path as needed.
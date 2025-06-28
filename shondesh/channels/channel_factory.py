class ChannelFactory:
    """
    Factory class to create channel instances based on the channel type.
    """

    @staticmethod
    def create_channel(channel_type, **kwargs):
        """
        Create a notifier instance based on the notifier type.

        :param channel_type: The type of notifier to create.
        :param kwargs: Additional parameters for the notifier.
        :return: An instance of the specified notifier.
        """
        from shondesh.channels import (
            Email,
            Telegram,
            Slack,
            Webhook,
        )

        channels = {
            "email": Email,
            "telegram": Telegram,
            "slack": Slack,
            "webhook": Webhook,
        }

        if channel_type not in channels:
            raise ValueError(f"Unsupported channel type: {channel_type}")

        return channels[channel_type](**kwargs)

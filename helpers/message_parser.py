"""
Parses messages from the client and returns the appropriate response
"""
from helpers.custom_logger import CustomLogger

class MessageParser:
    """
    Parse raw messages received from the client
    """

    def __init__(self):
        self.logger = CustomLogger(self.__class__.__name__)
        self.keys = [
            'PING',
            "KEY",
            "MOUSE",
            "MEDIA",
            "CLICK",
            "SITE",
            "POWER",
            "LAUNCHAPP",
        ]

    @staticmethod
    def extract_key(message):
        """
        Returns the key of the message
        Parameters:
            message: the message to be parsed (PING:hello)
        Returns:
            key: the key of the message (PING)
        """
        return message.split(':')[0]

    @staticmethod
    def extract_value(message):
        """
        Returns the value of the message
        Parameters:
            message: the message to be parsed (PING:hello)
        Returns:
            value: the value of the message (hello)
        """
        return message.split(':')[1]

    def validate_key(self, key):
        """
        validates the key by checking if it is in the list of keys
        """
        return key in self.keys

    def parse(self, message):
        """
        Parses the message and returns a tuple of the key and value
        Parameters:
            message: the message to be parsed (PING:hello)
        Returns:
            key: the key of the message (PING)
        """
        if len(message.split(':')) == 2:
            key = self.extract_key(message)
            value = self.extract_value(message)
            if self.validate_key(key):
                return key, value

            self.logger.debug(f"Invalid key: {key}")
            raise ValueError(f"Invalid key: {key}")
        self.logger.debug(f"Invalid message: {message}")
        raise ValueError(f"Invalid data received: {message}")

    def extract_x_y(self, value):
        """
        Returns the x and y coordinates of the mouse
        Parameters:
            value: the value of the message (-13.0@0.0)
        Returns:
            x: the x coordinate (-13.0, 0.0)
        """
        if '@' in value:
            mouse_x, mouse_y = value.split('@')
            return mouse_x, mouse_y
        self.logger.info(f"Invalid data received: {value}")
        raise ValueError(f"Invalid data received: {value}")

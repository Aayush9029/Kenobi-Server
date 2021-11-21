"""
File that contains the CustomLogger class.
"""

import logging
from os import path, makedirs


class CustomLogger:
    """
    Custom logger for the application.
    """

    def __init__(self, name, debug=False):
        """
        Initialize the logger
        """
        self.initialize_logger(name, debug)

    def initialize_logger(self, name, debug=False):
        """
        Initialize the logger
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        # Save the log file as a .log file in the logs directory
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        # Store logs in user's home directory in .kenobi/logs
        try:
            self.logger.addHandler(logging.FileHandler(
                f"{path.expanduser('~')}/.kenobi/logs/{name}.log", "a"))
            self.logger.info(f"Logger initialized for {name}")
        except FileNotFoundError:
            # make the logs directory if it doesn't exist
            try:
                makedirs(f"{path.expanduser('~')}/.kenobi/logs")
                self.logger.addHandler(logging.FileHandler(
                    f"{path.expanduser('~')}/.kenobi/logs/{name}.log", "a"))
                self.logger.info(f"Logger folder initialized for file {name}")
            except FileExistsError:
                self.logger.error(
                    "Logger could not be initialized. Logs directory not found.")
            except PermissionError:
                self.logger.error(
                    "Logger could not be initialized. Permission denied.")
        except PermissionError:
            self.logger.error(
                "Logger could not be initialized. Permission denied.")
        except Exception as e:
            self.logger.error(
                "Logger could not be initialized. An unknown error occurred.")
            self.logger.error(e)

    def info(self, message):
        """
        log an info message
        """
        self.logger.info(message)

    def error(self, message):
        """
        log an error message
        """
        self.logger.error(message)

    def warning(self, message):
        """
        log a warning message
        """
        self.logger.warning(message)

    def debug(self, message):
        """
        log a debug message
        """
        self.logger.debug(message)

    def critical(self, message):
        """
        log a critical message
        """
        self.logger.critical(message)

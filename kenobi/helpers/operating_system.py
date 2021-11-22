""""
Find out what operating system is running.
"""

import platform

from helpers.custom_logger import CustomLogger


class OperatingSystem:
    """
    Find out what operating system is running.
    """

    def __init__(self) -> None:
        self.logger = CustomLogger(self.__class__.__name__)
        self.platform = platform.system()
        self.is_supported_os()

    def __str__(self) -> str:
        """
        Returns the operating system name as a string.
        instead of Object Address
        """
        return self.platform

    def is_supported_os(self):
        """
        Check if the operating system is any OS.
        """
        if not self.platform in ("Linux", "Windows", "Darwin"):
            self.logger.error("Operating system is not supported.")

    def is_mac(self) -> bool:
        """
        Check if the operating system is Mac.
        """
        return self.platform == "Darwin"

    def is_windows(self) -> bool:
        """
        Check if the operating system is Windows.
        """
        return self.platform == "Windows"

    def is_linux(self) -> bool:
        """
        Check if the operating system is Linux.
        """
        return self.platform == "Linux"

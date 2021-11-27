"""
Main application file with the main function.
And argument parser.
"""
import asyncio
from argparse import ArgumentParser
from os import path
from shutil import rmtree

from helpers import websocket_server


class Kenobi:
    """
    Class Main which contains the main function.
    And argument parser.
    """

    def __init__(self) -> None:
        """
        Initialize the main class.
        """
        self.debug = False
        self.background = True
        self.logs = False
        self.main()

    @staticmethod
    def parser():
        """
        Parse the arguments.
        Arguments:
            Delete logs: (action delete logs)
                -l, --logs
        """
        parser = ArgumentParser(description="Kenobi Server")
        # add --background and --debug flags default to False
        parser.add_argument("-l", "--logs", action="store_true",
                            default=False, help="Delete logs")
        return parser.parse_args()

    @staticmethod
    def delete_logs():
        """
        Delete logs folder
        """
        print("Deleting logs...")
        # Logs are stored in ~/.kenobi/logs
        # Delete logs folder entirely
        rmtree(path.expanduser("~/.kenobi/logs"))
        print("Done!")

    def main(self):
        """
        Main function.
        """
        args = self.parser()
        self.logs = args.logs

        if self.logs:
            self.delete_logs()
            return
        print("Starting kenobi...")
        websocket_server.WebsocketServer(debug=self.debug)
        asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    Kenobi()

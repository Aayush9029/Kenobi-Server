"""
Webserver for the the client to connect to
"""

import asyncio

import websockets

from .custom_logger import CustomLogger
from .emulator import Emulator
from .local_ip import get_local_ip, get_pairing_code
from .message_parser import MessageParser as mp

HOST = "0.0.0.0"
PORT = 9999


class WebsocketServer:
    """
    Class for handling the websocket server and executing the commands
    """

    def __init__(self, debug: bool = False) -> None:
        self.parser = mp()
        self.emulator = Emulator()
        self.logger = CustomLogger(self.__class__.__name__, debug)
        # Server settings (constants)
        # Client Info
        self.connected_ip = None
        self.connected_port = None
        # Start server
        self.logger.warning(f"websocket initialized @ {get_local_ip()}:9999")
        self.logger.warning(f"\nYour pairing code is {get_pairing_code()}\n")
        asyncio.get_event_loop().run_until_complete(self.start())

    async def start(self) -> None:
        """
        Start the websocket server and listen for connections
        """
        self.logger.info(
            f"Starting websocket server @ {HOST}:{PORT}")
        self.server = await websockets.serve(self.handler, HOST, PORT)

    async def handler(self, websocket) -> None:
        """
        Handle the websocket connection, and receive messages
        """
        self.connected_ip = websocket.remote_address[0]
        self.connected_port = websocket.remote_address[1]
        self.logger.warning(
            f"Client connected @ {self.connected_ip}:{self.connected_port}")

        while True:
            try:
                message = await websocket.recv()
                try:
                    key, value = self.parser.parse(message)
                    print(f"Parsed: {key}:{value}")
                    if key == "LAUNCHAPP":
                        self.emulator.launch_app(value)
                    elif key == "PING":
                        self.emulator.ping(value)
                    elif key == "SITE":
                        self.emulator.launch_site(value)
                    elif key == "POWER":
                        self.emulator.power_option(value)
                    elif key in ("MEDIA", "KEY"):
                        self.emulator.emulate_key(value)
                    else:
                        self.logger.info(f"Invalid key: {key}")
                except ValueError as error:
                    self.logger.info(f"Invalid message: {error}")

            except websockets.exceptions.ConnectionClosed:
                self.logger.warning(
                    f"Client disconnected @ {self.connected_ip}:{self.connected_port}")
                self.connected_ip = None
                self.connected_port = None
                break


if __name__ == "__main__":
    server = WebsocketServer()
    asyncio.get_event_loop().run_forever()

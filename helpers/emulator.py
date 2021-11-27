"""
File containing class which represents the emulator.
Controlling media, open apps and links, playing audio, etc is done here.
"""
import webbrowser
from subprocess import run
from os import system

from playsound import playsound
from pynput.keyboard import Controller, Key

from .operating_system import OperatingSystem
from .custom_logger import CustomLogger


class Emulator:
    """
    Class which emulates a key presses, controls media playback
    """

    def __init__(self):
        """
        Initialize the key controller
        And valid key dictionaries
        """
        self.logger = CustomLogger(self.__class__.__name__)
        self.operating_system = OperatingSystem()
        self.keyboard = Controller()

        self.valid_direction_keys = {
            "left": Key.left,
            "right": Key.right,
            "up": Key.up,
            "down": Key.down,
            "space": Key.space,
            "tab": Key.tab,
            "return": Key.enter,
            "escape": Key.esc,
        }

        self.valid_media_keys = {
            "playpause": Key.media_play_pause,
            "next": Key.media_next,
            "previous": Key.media_previous,
            "mute": Key.media_volume_mute,
            "volumeup": Key.media_volume_up,
            "volumedown": Key.media_volume_down
        }

    def emulate_key(self, received_key: str):
        """
        Check if the key is valid, and if so
        Emulate the key using the keyboard controller
        """

        if received_key in self.valid_direction_keys:
            self.keyboard.press(self.valid_direction_keys[received_key])
        else:
            self.logger.info(f"Invalid key {received_key}")

        if received_key in self.valid_media_keys:
            if self.operating_system.platform == "Darwin":
                self.hid_post_aux_key(received_key)
                return
            self.keyboard.press(self.valid_media_keys[received_key])
        else:
            self.logger.info(f"Invalid key {received_key}")

    def hid_post_aux_key(self, key):
        """
        hid post aux key emulation for macOS
        Pynput is not working on macOS so we use this workaround
        """
        import Quartz
        # NSEvent.h
        NSSystemDefined = 14

        # hidsystem/ev_keymap.h
        sound_up_key = 0
        sound_down_key = 1
        play_key = 16
        next_key = 17
        previous_key = 18
        mute_key = 7

        supportedcmds = {
            'playpause': play_key,
            'next': next_key,
            'previous': previous_key,
            'volumeup': sound_up_key,
            'volumedown': sound_down_key,
            'mute': mute_key
        }
        if key in supportedcmds:
            key = supportedcmds[key]
        else:
            self.logger.error(f"Invalid key {key}")
            return

        def do_key(down):
            """
            Handles the key press (keydown or keyup)
            """
            event = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                NSSystemDefined,  # type
                (0, 0),  # location
                0xa00 if down else 0xb00,  # flags
                0,  # timestamp
                0,  # window
                0,  # ctx
                8,  # subtype
                (key << 16) | ((0xa if down else 0xb) << 8),  # data1
                -1  # data2
            )

            c_event = event.CGEvent()
            Quartz.CGEventPost(0, c_event)
        do_key(True)
        do_key(False)

    def launch_app(self, app: str):
        """
        Launch the app using the system command
        """
        if app.endswith(".com"):
            self.launch_site(url=app)
        else:
            # TEST Launch apps for other OSs
            launch_args = {
                'Linux': ['xdg-open'],
                'Windows': ['start'],
                'Darwin': ['open', '-a']
            }

            try:
                run(launch_args[self.operating_system.platform] + [app])
            except KeyError:
                print(f"Invalid OS \"{self.operating_system}\"")

    @staticmethod
    def ping(value):
        """
        Play the ping sound ping_sound.wav
        """
        if value == "hello":
            # add hello.wav file and play it
            playsound("assets/ping_sound.wav")
        elif value == "ping":
            playsound("assets/ping_sound.wav")
        else:
            print(f"Invalid ping option {value}")

    @staticmethod
    def launch_site(url):
        """
        Launch the site using the system command
        """
        webbrowser.open_new(url=f"https://{url}")

    def power_option(self, value):
        """
        Emulate the power option
        """
        if value == "shutdown":
            self.shutdown()
        elif value == "logout":
            self.logout()
        elif value == "restart":
            self.restart()
        elif value == "sleep":
            self.sleep()
        else:
            print(f"Invalid power option {value}")

    # power options child functions
    def shutdown(self):
        """
        Shutdown the computer depending on the OS
        """
        if self.operating_system.platform == "Linux":
            system("shutdown -h now")
        elif self.operating_system.platform == "Windows":
            system("shutdown -s")
        elif self.operating_system.platform == "Darwin":
            system("shutdown -h now")

    def logout(self):
        """
        Logout of the current session
        """
        if self.operating_system.platform == "Linux":
            system("gnome-session-quit --force")
        elif self.operating_system.platform == "Windows":
            system("shutdown -l")
        elif self.operating_system.platform == "Darwin":
            system("shutdown -l")

    def restart(self):
        """
        Restart the computer
        """
        if self.operating_system.platform == "Linux":
            system("shutdown -r now")
        elif self.operating_system.platform == "Windows":
            system("shutdown -r")
        elif self.operating_system.platform == "Darwin":
            system("shutdown -r now")

    def sleep(self):
        """
        Sleep the computer
        """
        if self.operating_system.platform == "Linux":
            system("systemctl suspend")
        elif self.operating_system.platform == "Windows":
            system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif self.operating_system.platform == "Darwin":
            system("pmset sleepnow")

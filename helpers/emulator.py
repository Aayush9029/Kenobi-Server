"""
Key emulating class
"""
from os import system

from playsound import playsound
from pynput.keyboard import Controller, Key

from helpers.operating_system import OperatingSystem


class Emulator:
    """
    Class which emulates a key presses, controls media playback
    """
    def __init__(self):
        """
        Initialize the key controller
        And valid key dictionaries
        """
        self.operating_system = OperatingSystem()
        self.keyboard = Controller()
        self.vaildKeys = {
            "left": Key.left,
            "right": Key.right,
            "up": Key.up,
            "down": Key.down,
            "space": Key.space,
            "tab": Key.tab,
            "return": Key.enter,
            "escape": Key.esc,
            "playpause": Key.media_play_pause,
            "next": Key.media_next,
            "previous": Key.media_previous,
            "mute": Key.media_volume_mute,
            "volumeup": Key.media_volume_up,
            "volumedown": Key.media_volume_down
        }
    
    def emulate_key(self, recievedKey: str):
        """
        Check if the key is valid, and if so
        Emulate the key using the keyboard controller
        """
        if recievedKey in self.vaildKeys:
            self.keyboard.press(self.vaildKeys[recievedKey])
        else:
            # TODO: Add error handling
            print(f"Invalid key to emulate {recievedKey}")

    def launch_app(self, app: str):
        # TODO: Launch apps for other OSs
        """
        Launch the app using the system command
        """
        if self.operating_system == "linux":
            system(f"xdg-open {app}")
        elif self.operating_system == "windows":
            system(f"start {app}")
        elif self.operating_system == "mac":
            system(f"open -a {app}")

    def ping(self, value):
        """
        Play the ping sound ping_sound.wav
        """
        if value == "hello":
            # TODO: add hello.wav file and play it
            playsound("ping_sound.wav")
        elif value == "ping":
            playsound("ping_sound.wav")
        else:
            print(f"Invalid ping option {value}")
        
    def launch_site(self, url):
        """
        Launch the site using the system command
        """
        if self.operating_system == "linux":
            system(f"xdg-open {url}")
        elif self.operating_system == "windows":
            system(f"start {url}")
        elif self.operating_system == "mac":
            system(f"open -a {url}")
    
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
        if self.operating_system == "linux":
            system("shutdown -h now")
        elif self.operating_system == "windows":
            system("shutdown -s")
        elif self.operating_system == "mac":
            system("shutdown -h now")
    
    def logout(self):
        """
        Logout of the current session
        """
        if self.operating_system == "linux":
            system("gnome-session-quit --force")
        elif self.operating_system == "windows":
            system("shutdown -l")
        elif self.operating_system == "mac":
            system("shutdown -l")
    
    def restart(self):
        """
        Restart the computer
        """
        if self.operating_system == "linux":
            system("shutdown -r now")
        elif self.operating_system == "windows":
            system("shutdown -r")
        elif self.operating_system == "mac":
            system("shutdown -r now")

    def sleep(self):
        """
        Sleep the computer
        """
        if self.operating_system == "linux":
            system("systemctl suspend")
        elif self.operating_system == "windows":
            system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif self.operating_system == "mac":
            system("pmset sleepnow")
        
if __name__ == "__main__":
    key = Emulator()
    key.emulate_key("volumeUp")
# pylint: skip-file

from platform import platform
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.operating_system import OperatingSystem

plat = sys.platform.lower()
osp = OperatingSystem()

def test_os_name():
    if plat == 'linux':
        assert osp.is_linux()
    elif plat == "windows":
        assert osp.is_windows()
    elif plat == 'darwin':
        assert osp.is_mac()

def test_os_version_name():
    if plat == 'linux':
        assert osp.platform == 'Linux'
    elif plat == "windows":
        assert osp.platform == 'Windows'
    elif plat == 'darwin':
        assert osp.platform == 'Darwin'

def test_os_string_modifier():
    if plat == 'Linux':
        assert str(osp) == platform()
    elif plat == "Windows":
        assert str(osp) == platform()
    elif plat == 'Darwin':
        assert str(osp) == platform()


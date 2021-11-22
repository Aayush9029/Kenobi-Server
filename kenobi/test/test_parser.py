# pylint: skip-file

from helpers.message_parser import MessageParser
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


def test_exception():
    """
    Test if exceptions are thrown correctly
    """
    message = "Hello World!"
    parser = MessageParser()
    try:
        _ = parser.parse(message)
    except ValueError:
        assert True
    except:
        assert False

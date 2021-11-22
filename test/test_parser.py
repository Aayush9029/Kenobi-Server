# pylint: skip-file

import sys
import os
import pytest
from random import randint, choice, shuffle
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.message_parser import MessageParser

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

def test_parse_message():
    """
    Test if the message is parsed correctly
    """
    message = "PING:Hello"
    parser = MessageParser()
    parsed = parser.parse(message)
    assert parsed == ("PING", "Hello")

def test_parse_message_with_space():
    """
    Test if the message is parsed correctly
    """
    message = "PING: Hello"
    parser = MessageParser()
    parsed = parser.parse(message)
    assert parsed == ("PING", " Hello")


# Loop through all KeyHeaders and test if they are parsed correctly
headers = [
    'PING',
    "KEY",
    "MOUSE",
    "MEDIA",
    "CLICK",
    "SITE",
    "POWER",
    "LAUNCHAPP",
]    

@pytest.mark.parametrize("test_input, _", zip(headers, headers))
def test_parse_message_with_colon(test_input, _):
    """
    Test if the message is parsed correctly
    """
    message = test_input + ":COMMAND"
    parser = MessageParser()
    parsed = parser.parse(message)
    assert parsed == (test_input, "COMMAND")


mediaCommands = [ "left", "right", "up", "down", "space", "tab", "return", "escape", "playpause", "next", "previous", "mute", "volumeup", "volumedown"]
@pytest.mark.parametrize("test_input, _", zip(mediaCommands, mediaCommands))
def test_parse_message_with_media_command(test_input, _):
    """
    Test if the message is parsed correctly
    """
    message = "MEDIA:" + test_input
    parser = MessageParser()
    parsed = parser.parse(message)
    assert parsed == ("MEDIA", test_input)


# generate array with structure like this -32.4@51.12 24.0@-12.77
def generate_coordinates():
    """
    Generate random coordinates
    """
    x = randint(-1000, 1000)
    y = randint(-1000, 1000)
    return str(x) + "@" + str(y)

coordinates = [generate_coordinates() for _ in range(50)]

@pytest.mark.parametrize("test_input, _", zip(coordinates, coordinates))
def test_parse_message_with_coordinates(test_input, _):
    """
    Test if the message is parsed correctly
    """
    message = test_input
    parser = MessageParser()
    parsed = parser.extract_x_y(message)
    assert parsed == (test_input.split("@")[0], test_input.split("@")[1])


# generate random words 
def generate_words():
    """
    Generate random words
    """
    return ''.join(choice(string.ascii_letters) for _ in range(randint(10, 100)))
    
words = [generate_words() for _ in range(25)]

words = words + headers
shuffle(words)

@pytest.mark.parametrize("test_input, _", zip(words, words))
def test_parse_message_with_words(test_input, _):
    """
    Test if the message is parsed correctly
    """
    message = test_input
    parser = MessageParser()
    if test_input in headers:
        parsed = parser.extract_key(message)
        assert parsed == test_input
    else:
        try:
            parsed = parser.parse(message)
            assert parsed[0] == None or parsed[1] == None
        except ValueError:
            assert True
        except:
            assert False

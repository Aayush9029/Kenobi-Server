# [Kenobi-Server](https://aayush9029.github.io/KenobiSite/)
PIP package for opensource implementation of the kenobi macOS app.

[![pylint](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml/badge.svg)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml) [![pytest](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pytest.yml)

---
Download the Apple Watch app to get started.

<a href="https://apps.apple.com/us/app/kenobi/id1595469125"><img src="https://raw.githubusercontent.com/Aayush9029/Kenobi-Server/main/readme-assets/download-appstore-icon.png" width="150px"></a>

![Apple watch image with Kenobi app running](https://aayush9029.github.io/KenobiSite/img/mainresize.png)


### Features
  - Media Playback
    - Increase / Decrease volume
    - Pause / Play media
    - Forward / Rewind media
    - Toggle Mute
    - Exit full screen
    
  - Keyboard control
    - Up arrow
    - Down arrow
    - Right arrow
    - Left arrow
    - Space
    - Return (Enter) key
    - TAB
    
  - Trackpad Support
    - Move the cursor on the desktop by simply interacting with watch Screen.
   
  - Ping Desktop
    - Play a ping noise
    - Say "Hello There! General Kenobi!"
    - Rickroll: [Plays This beauty](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
   
  - Power options
    - Log out
    - Sleep
    - Restart
    - Power off
   
  - Launch apps
    - MacOS
      - FaceTime, Messages, Mail, Music, Notes, Safari, System Pref, Apple TV, Youtube
    - Windows / Linux
      - TBD


### Usage

```python
from kenobi import Kenobi
Kenobi()
```

*Kenobi will start listening for client's websocket commands.*

> You can spawn a new thread, or run it this in the background. 

[More Info and Documentations](https://github.com/Aayush9029/Kenobi-Server)
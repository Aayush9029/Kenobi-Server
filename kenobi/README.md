# [Kenobi-Opensource](https://aayush9029.github.io/KenobiSite/)
Open-source implementation of the Kenobi macOS app.

[![pylint](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml/badge.svg)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml) [![pytest](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pytest.yml)

---

### Usage

```python
from kenobi import Kenobi
Kenobi()
```

*Kenobi will start listening for client's web-socket commands.*

> You can either spawn a new thread or run this in the background. 

[More Info and Documentation](https://github.com/Aayush9029/Kenobi-Server)

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

> This provides server framework for your application, you can use this to quickly create client applications for Android, iOS or even use PWA / web-sockets (via browser)

# [Kenobi-Server](https://aayush9029.github.io/KenobiSite/)
Archived Opensource desktop application for Kenobi.

# Developer Notice: There's a brand new iOS, watchOS and macOS app in developement. Kenobi uses sockets where as the brand new app will use Multipeer and watch connectivity (Apple's native framework) which will dramatically decrease issues and maintenance. 

### Kenobi-Server and the app will be archived in the coming weeks

#### Current users will get access to the new app for free!

---

![macOS](https://img.shields.io/badge/MacOS-working%20(fully)-brightgreen?style=flat&labelColor=343b41&color=3fc855&logo=apple) ![windows](https://img.shields.io/badge/windows-working%20(partial)-brightgreen?style=flat&labelColor=343b41&color=3fc855&logo=windows) ![linux](https://img.shields.io/badge/linux-not%20tested-orange?style=flat&labelColor=343b41&color=838c96&logo=linux)

[![CodeQL](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/codeql-analysis.yml/badge.svg?branch=alpha-staging?style=flat-square&)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/codeql-analysis.yml) [![pylint](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml/badge.svg)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pylint.yml) [![pytest](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/Aayush9029/Kenobi-Server/actions/workflows/pytest.yml)

---
Download the Apple Watch app to get started.

<a href="https://apps.apple.com/us/app/kenobi/id1595469125"><img src="https://raw.githubusercontent.com/Aayush9029/Kenobi-Server/main/readme-assets/download-appstore-icon.png" width="150px"></a>

![Apple watch image with Kenobi app running](https://aayush9029.github.io/KenobiSite/img/mainresize.png)

---

### Installation 

- Release: https://pypi.org/project/kenobi-app/


```
pip install kenobi-app --user
```

### App usage

```bash
python3 -m kenobi 
```
*if you want to run the program in the background add an ampersand at the end*
```bash
python3 -m kenobi &
```


### PIP Usage

```python
python3 
>>> from kenobi import Kenobi
>>> Kenobi()
```


### Here's the expected output
![Screen Shot 2021-11-22 at 2 17 44 PM](https://user-images.githubusercontent.com/43297314/142921896-93bbf13c-8c96-45e4-b18f-1f4b29288831.png)

### What is [this repo?](https://github.com/Aayush9029/Kenobi-Server)
It's repo for the opensource version of Kenobi desktop app which works on Windows, Linux along side MacOS.

### Why is the desktop app opensource?
To help others who are struggling with writing code that commnunicates with between *desktop <=> iOS Devices*
> It is not limited to iOS devices (can be expanded to PWA, Android apps and even desktop apps)


### How does this work?
> Websockets! 
> Desktop Application acts as a websocket server which is then connected to via client.
>
> The client then sends commands to the server and the server acts upon it.
>

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
   

> The opensource desktop app is CLI based for now keeping it's resource usage as minimum as possible.

[2nd License - DWYW ?? Aayush Pokharel](https://raw.githubusercontent.com/Aayush9029/Kenobi-Server/main/LICENSE2.md)

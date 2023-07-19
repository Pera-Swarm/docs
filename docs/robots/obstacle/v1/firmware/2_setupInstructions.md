---
layout: default
parent: Firmware
grand_parent: Obstacle Robots
title: Firmware Setup Guide
nav_order: 2
permalink: robots/obstacle-robot/v1/firmware/setup/

gh_link: docs/robots/obstacle/v1/firmware/2_setupInstructions.md
---

# Firmware Setup Guide
{: .no_toc }

### Table of content
{: .no_toc }
- TOC
{:toc}

### 1. Install PlatformIO

- It is suggested to use VS Code IDE for the development. Follow the guide in [PlatformIO IDE for VSCode](https://docs.platformio.org/en/latest/integration/ide/vscode.html#ide-vscode) to install PlatformIO Extension with VS Code IDE. 
- If you are using another IDE, please check [here](https://docs.platformio.org/en/latest/integration/ide/index.html#desktop-ides) for the installation instructions.

### 2. Install Arduino Framework 

- We are using [atmelavr](https://docs.platformio.org/en/latest/platforms/atmelavr.html) Plafrorm with [Arduino](https://docs.platformio.org/en/latest/frameworks/arduino.html) framework. The first time you build the project, this will be downloaded automatically with the other required packages, tools, and libraries.

### 3. Prepare config.h

- Once you set up the repository, you need to copy the 'src/config/config_sample.h' file and create 'src/config/config.h'. 
- As for now, no any configurations need to be done.

### 4. Build and Upload

- You can use the **Build** button in the IDE or use the below command in the terminal to build the firmware. 

```sh 
pio build
```

- You can use the **Upload** button in the IDE or use the below command in the terminal to build the firmware and upload it to the development board. 
- Usually, PlatformIO will automatically identify the COM port that the robot is connected to. 
- You need to use an external _USB to UART_ converter to upload the firmware into the Arduino Pro Mini boards.

```sh 
pio run --target upload 
```

- If you got any _'sync'_ related error while uploading, press the **Reset** button in the Pro-Mini development board and try again.
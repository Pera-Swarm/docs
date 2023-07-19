---
layout: default
parent: Firmware
grand_parent: Main Robots
title: Firmware Setup Guide
nav_order: 2
permalink: robots/v4/firmware/setup/

gh_link: docs/robots/main/v4/firmware/2_setupInstructions.md
---

# Firmware Setup Guide
{: .no_toc }

##### Table of content
{: .no_toc }
- TOC
{:toc}

### 1. Install PlatformIO

- It is suggested to use VS Code IDE for the development. Follow the guide in [PlatformIO IDE for VSCode](https://docs.platformio.org/en/latest/integration/ide/vscode.html#ide-vscode) to install PlatformIO Extension with VS Code IDE. 
- If you are using another IDE, please check [here](https://docs.platformio.org/en/latest/integration/ide/index.html#desktop-ides) for the installation instructions.

### 2. Install ESP32 Framework 

- We are using [Espressif 32](https://docs.platformio.org/en/latest/platforms/espressif32.html) Plafrorm with _Arduino_ framework. The first time you build the project, this will be downloaded automatically with the other required packages, tools, and libraries.

### 3. Prepare config.h

- Once you set up the repository, you need to copy the 'src/config/config_sample.h' file and create 'src/config/config.h'. 
- Next, open the 'config.h' file and fill in the below __definitions__ with the MQTT Broker you are using.

```cpp
#define MQTT_SERVER "192.168.8.1"
#define MQTT_PORT 1883
#define MQTT_CLIENT "Robot"
#define MQTT_USERNAME "mqtt_username"
#define MQTT_PASSWORD "mqtt_password"
```

- Fill in the below __definitions__ with the credentials of the WiFi network you are using.

```cpp
#define WIFI_SSID "wifi_SSID"
#define WIFI_PASS "wifi_password"
```

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

- If you are getting an error like _'Failed to connect to ESP32: Timed out… Connecting…'_, you need to hold down the **BOOT** button in the development board, and press the **Upload** button in the IDE. After you see the _'Connecting...'_ message in the IDE, you can release the **BOOT** button.


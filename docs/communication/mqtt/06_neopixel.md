---
title: "NeoPixel LEDs"
nav_order: 6
---

## NeoPixel LED Protocols

### /output/neopixel

| Property       | Value                                                                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Source         | Robot (Physical &#124; Virtual)                                                                                                                                                            |
| Destination    | Server / GUI                                                                                                                                                                               |
| Data Type      | JSON                                                                                                                                                                                       |
| Message Format | `{"id": 10, "R": [R], "G": [B], "B": [B]}`                                                                                                                                                 |
| Description    | Broadcast the RGB values of robot's NeoPixel LED ring to the Server/ GUI through the topic.<br><br>**id**: ID number of the robot<br>**R,G,B**: RGB color components &#124; range: [0,255] |

### /output/neopixel/{robotID}

| Property       | Value                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Server                                                                                                                                                                                               |
| Destination    | Robot (Physical &#124; Virtual)                                                                                                                                                                      |
| Data Type      | String                                                                                                                                                                                               |
| Message Format | `[R] [G] [B]`                                                                                                                                                                                        |
| Description    | Server can ask from robot to change their colors by using the topic `/output/neopixel/{robotID}`<br><br>**robotID**: ID number of the robot<br>**R,G,B**: RGB color components &#124; range: [0,255] |

---
title: "Robot"
nav_order: 1
---

## Robot Protocols

### /robot/msg/{robotID}

| Property       | Value                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------- |
| Source         | Simulator                                                                                 |
| Destination    | Robot (Virtual &#124; Physical)                                                           |
| Data Type      | String                                                                                    |
| Sample Message | `[MessageType] [MessageValue]`                                                            |
| Description    | Send a control message to an individual robot.<br><br>**robotID**: ID number of the robot |

### /robot/msg/broadcast

| Property       | Value                                        |
| -------------- | -------------------------------------------- |
| Source         | Simulator                                    |
| Destination    | Robot (Virtual &#124; Physical)              |
| Data Type      | String                                       |
| Sample Message | `[MessageType] [MessageValue]`               |
| Description    | Send a control message to all active robots. |

Example _MessageType_ and _MessageValue_ pairs:

- ID? -1
- START -1
- STOP -1
- RESET -1

### /robot/live

| Property       | Value                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Robot (Virtual &#124; Physical)                                                                                                                                                                      |
| Destination    | Simulator                                                                                                                                                                                            |
| Data Type      | JSON                                                                                                                                                                                                 |
| Sample Message | `{"id": [robotID], "reality": [reality]}`                                                                                                                                                            |
| Description    | Heartbeat signal from the robots to server. Simulator will keep a track of this to prune dead robots from the system.<br><br>**robotID**: ID number of the robot<br>**reality**: V: virtual, R: real |

### /robot/create

| Property       | Value                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Localization System, Virtual Robot                                                                                                                                                                                                                                                                                                                                                                                   |
| Destination    | Simulator, Visualizer                                                                                                                                                                                                                                                                                                                                                                                                |
| Data Type      | JSON                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Sample Message | `{ "id":0, "x":10, "y":10, "heading":0.0, "reality": "R" }`                                                                                                                                                                                                                                                                                                                                                          |
| Description    | This will be originated by virtual robots themselves at the beginning, or by the localization system for physical robots. Information taken by the Simulator will create a robot instance in its Mixed Reality Environment and the Visualizer will create a robot geometry.<br><br>**id**: ID number of the robot<br>**x, y, z, heading**: floating point number with 2 decimals<br>**reality**: V: virtual, R: real |

### /robot/delete

| Property       | Value                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Simulator                                                                                                                                       |
| Destination    | Visualizer                                                                                                                                      |
| Data Type      | JSON                                                                                                                                            |
| Sample Message | `{ "id": [robotID] }`                                                                                                                           |
| Description    | This will inform other systems to remove the robot. Invoked by the prune scheduler on the Simulator.<br><br>**robotID**: ID number of the robot |

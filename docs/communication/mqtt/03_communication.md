---
title: "Communication"
nav_order: 3
---

## Communication Protocols

### /comm/in/simple/{robotID}

| Property       | Value                                                                                                                                                                                                                                                           |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Server                                                                                                                                                                                                                                                          |
| Destination    | Robot                                                                                                                                                                                                                                                           |
| Data Type      | String                                                                                                                                                                                                                                                          |
| Message Format | `[message]`                                                                                                                                                                                                                                                     |
| Description    | The server will send a message sent via simple communication to a robot. A pure virtual implementation, receivers will be decided by the simulation server.<br><br>**robotID**: ID number of the robot<br>**message**: The message string, max length: 64 chars |

### /comm/in/direct/{robotID}

| Property       | Value                                                                                                                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Server                                                                                                                                                                                                                                                            |
| Destination    | Robot                                                                                                                                                                                                                                                             |
| Data Type      | String                                                                                                                                                                                                                                                            |
| Message Format | `[message]`                                                                                                                                                                                                                                                       |
| Description    | The server will send a message sent via directed communication to a robot. A pure virtual implementation, receivers will be decided by the simulation server.<br><br>**robotID**: ID number of the robot<br>**message**: The message string, max length: 64 chars |

### /comm/out/{protocol}

| Property       | Value                                                                                                                                                                                                                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Robot                                                                                                                                                                                                                                                                                                                                                             |
| Destination    | Server                                                                                                                                                                                                                                                                                                                                                            |
| Data Type      | JSON                                                                                                                                                                                                                                                                                                                                                              |
| Message Format | `{"id":[robotID], "msg": "This is a sample", "dist":[dist]}`                                                                                                                                                                                                                                                                                                      |
| Description    | The robots can transmit messages to other robots using a pre-implemented transmission protocol. Server will decide the robots who can receive the message.<br><br>**protocol**: simple, direct<br>**robotId**: ID number of the robot<br>**message**: The message string, max length: 64 chars<br>**dist (optional)**: maximum distance that message can be sent. |

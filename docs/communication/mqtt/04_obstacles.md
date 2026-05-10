---
title: "Obstacles"
nav_order: 4
---

## Obstacles Protocols

### /obstacles/?

| Property       | Value                                                                                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Visualizer                                                                                                                                                                                                             |
| Destination    | Simulator                                                                                                                                                                                                              |
| Data Type      | String                                                                                                                                                                                                                 |
| Message Format | `{reality}`                                                                                                                                                                                                            |
| Description    | The visualizer can request from the Simulator about obstacle data, filtered by the reality. Reply will be received through the topic `/obstacles`.<br><br>**reality**: M: mixed, V: virtual, R: real &#124; default: M |

### /obstacles

| Property       | Value                                                                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Simulator                                                                                                                                                                                                                                           |
| Destination    | Visualizer                                                                                                                                                                                                                                          |
| Data Type      | JSON List                                                                                                                                                                                                                                           |
| Message Format | `[Obstacle1, Obstacle2]`                                                                                                                                                                                                                            |
| Description    | The Simulator will send this as response to the `/obstacles/?` request. ~~This is always a retained type message~~<br><br>**obstacle**: Refer [Obstacle](../json/02_environment.md) JSON API definitions to learn more about Obstacle JSONs schema. |

### /obstacles/delete

| Property       | Value                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Simulator                                                                                                                                                                                      |
| Destination    | Visualizer                                                                                                                                                                                     |
| Data Type      | JSON                                                                                                                                                                                           |
| Message Format | `{ "id": [obstacle_Id] }`                                                                                                                                                                      |
| Description    | Delete the obstacle from the environment, which has given id.<br><br>**obstacle_Id**: A randomly generated, unique UUID number of the obstacle, assigned by the Simulator, once it was created |

### /obstacles/delete/all

| Property       | Value                                        |
| -------------- | -------------------------------------------- |
| Source         | Simulator                                    |
| Destination    | Visualizer                                   |
| Data Type      | String                                       |
| Message Format | `?`                                          |
| Description    | Delete all the obstacles in the environment. |

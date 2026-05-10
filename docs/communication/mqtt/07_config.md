---
title: "Config"
nav_order: 7
---

## Config Protocols

### /config/arena/

| Property       | Value                                                                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source         | Simulator                                                                                                                                                               |
| Destination    | Visualizer                                                                                                                                                              |
| Data Type      | JSON List                                                                                                                                                               |
| Message Format | `{ "xMin": [number], "xMax": [number], "yMin": [number], "yMax": [number], "units": "virtual" }`                                                                        |
| Description    | The Simulator will send this at the start, including the arena configuration details. Visualizer will use this to override its own default arena configuration details. |

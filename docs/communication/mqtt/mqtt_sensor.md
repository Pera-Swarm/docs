---
layout: default
parent: MQTT
grand_parent: Communication
title: Sensor
nav_order: 6
permalink: communication/mqtt/sensor/

gh_link: docs/communication/mqtt/mqtt_sensor.md
---

## Sensor Protocols
{: .no_toc }

- TOC
{:toc}

## Distance Sensor

### /sensor/distance/{robotID}/?

<table>
    <tr><td>Source</td><td> Simulator</td></tr>
    <tr><td>Destination</td><td> Robot ( Physical | Virtual ) </td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        ?
    </td></tr>
    <tr><td>Description</td><td>
        This will request distance sensor readings from a robot.
        Typically used by the Simulator or Sandbox.

        <br><br>
        <dd>robotID: Robot ID</dd>
    </td></tr>
</table>


### /sensor/distance/{robotID}

<table>
    <tr><td>Source</td><td> Simulator
    </td></tr>
    <tr><td>Destination</td><td> Robot</td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        {distance}
    </td></tr>
    <tr><td>Description</td><td>
        Simulator will inform Mixed Reality Environment readings to the robot,
        as a reply to the topic <i>/sensor/distance</i>

        <br><br>
        <dd>robotID: Robot ID</dd>
        <dd>distance: Distance in centimeters as a float</dd>
    </td></tr>
</table>

### /sensor/distance

<table>
    <tr><td>Source</td><td>Robot</td></tr>
    <tr><td>Destination</td><td>Simulator</td></tr>
    <tr><td>Data Type</td><td> JSON</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                {
                    "id": <i>[robotID]</i>,
                    "dist": <i>[distance]</i>,
                    "reality": "M"
                }
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        Robots can request mixed-reality sensor reading from simulator through this topic.
        There as an optional parameter, <i>'reality'</i> is used to request the reading only on a specified reality.
        Reply from the simulator will be received through the topic <i>/sensor/distance/{robotID}</i>.
        <br><br>
        Optionally, physical robots can inform their distance sensor readings to the server using dist parameters.

        <br><br>
        <dd>robotID: Robot ID</dd>
        <dd>dist(optional): Distance in centimeters as a float</dd>
        <dd>reality(optional): M: mixed, V: virtual, R: real | default: V</dd>
    </td></tr>
</table>

## Color  Sensor

### /sensor/color/{robotID}/?

<table>
    <tr><td>Source</td><td> Simulator</td></tr>
    <tr><td>Destination</td><td> Robot ( Physical | Virtual ) </td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        ?
    </td></tr>
    <tr><td>Description</td><td>
        This will request color sensor readings from a robot.
        Typically used by the Simulator or Sandbox.
    </td></tr>
</table>


### /sensor/color/{robotID}

<table>
    <tr><td>Source</td><td> Simulator
    </td></tr>
    <tr><td>Destination</td><td> Robot</td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        {R} {G} {B} {ambient}
    </td></tr>
    <tr><td>Description</td><td>
        Simulator will inform Mixed Reality Environment readings to the robot.
        Sensor readings must wait for this reply before deciding the final value.

        <br><br>
        <dd>R,G,B: corresponding color reading | range: [0,255]</dd>
        <dd>ambient: Ambient light of the environment | range: [0,255]</dd>
    </td></tr>
</table>

### /sensor/color

<table>
    <tr><td>Source</td><td> Physical Robot</td></tr>
    <tr><td>Destination</td><td> Simulator
    </td></tr>
    <tr><td>Data Type</td><td> JSON</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                {
                    "id":<i>[robotID]</i>,
                    "R":<i>[R]</i>,
                    "G":<i>[G]</i>,
                    "B":<i>[B]</i>,
                    "ambient":<i>[ambient]</i>,
                    "reality": "M"
                }
            </code>
        </div>

    </td></tr>
    <tr><td>Description</td><td>
        Robots can request mixed-reality sensor reading through this topic.
        There as an optional parameter, <i>'reality'</i> is used to request the reading only on a specified reality.
        Reply from the simulator will be received through the topic <i>/sensor/distance/{robotID}</i>.
        <br><br>
        Optionally, physical robots can inform their sensor readings to the server using R,G,B, ambient parameters.

        <br><br>
        <dd>id: Robot ID</dd>
        <dd>reality(optional): M: mixed, V: virtual, R: real | default: V</dd>

        <dd>R,G,B (optional): corresponding color reading | range: [0,255]</dd>
        <dd>ambient (optional): Ambient light of the environment | range: [0,255]</dd>
    </td></tr>
</table>

## Proximity Sensor (Subject to change)

### /sensor/proximity/{robotID}

<table>
    <tr><td>Source</td><td> Simulator</td></tr>
    <tr><td>Destination</td><td> Robot (Physical, Virtual)</td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        %d %d %d %d %d
    </td></tr>
    <tr><td>Description</td><td>
        Simulator will update virtual proximity sensor readings to the robot,
        as the reply to the ‘/sensor/proximity’ topic.<br><br>

        5 readings are representing the distance readings of following 5 angles,
        relative to the heading direction of the robot.<br><br>

        <dd>[-150, -90, 0, 90, 150]</dd>
    </td></tr>
</table>


### /sensor/proximity

<table>
    <tr><td>Source</td><td> Robot (Physical, Virtual)</td></tr>
    <tr><td>Destination</td><td> Simulator </td></tr>
    <tr><td>Data Type</td><td> JSON</td></tr>
    <tr><td>Message Format</td><td>
        {
            "id":0, "reality":[reality]
        }

    </td></tr>
    <tr><td>Description</td><td>
        The sensor is entirely virtual and both virtual and physical robots can
        request the proximity readings from the simulator using this.
        <br><br>
        <dd>reality(optional): V: virtual(default, and the only possible option far)</dd>
    </td></tr>
</table>

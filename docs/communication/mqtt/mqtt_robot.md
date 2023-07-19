---
layout: default
parent: MQTT
grand_parent: Communication
title: Robot
nav_order: 1
permalink: communication/mqtt/robot/

gh_link: docs/communication/mqtt/mqtt_robot.md
---

## Robot Protocols
{: .no_toc }

- TOC
{:toc}

### /robot/msg/{robotID}

<table>
    <tr><td>Source</td><td>Simulator</td></tr>
    <tr><td>Destination</td><td>Robot (Virtual | Physical)</td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Sample Message</td><td>
        <i>[MessageType] [MessageValue]</i>
    </td></tr>
    <tr><td>Description</td>
        <td>Send a control message to an individual robot.
            <br><br>
            <dd>robotID: ID number of the robot</dd>
        </td>
    </tr>
</table>

### /robot/msg/broadcast

<table>
    <tr><td>Source</td><td>Simulator</td></tr>
    <tr><td>Destination</td><td>Robot (Virtual | Physical)</td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Sample Message</td><td>
        <i>[MessageType] [MessageValue]</i>
    </td></tr>
    <tr><td>Description</td><td>Send a control message to all active robots.
    </td></tr>
</table>


Example *MessageType* and *MessageValue* pairs:
- ID? -1
- START -1
- STOP -1
- RESET -1


### /robot/live

<table>
    <tr><td>Source</td><td>Robot (Virtual | Physical)</td></tr>
    <tr><td>Destination</td><td>Simulator</td></tr>
    <tr><td>Data Type</td><td>JSON</td></tr>
    <tr><td>Sample Message</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                {"id": <i>[robotID]</i>, "reality": <i>[reality]</i>}
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        Heartbeat signal from the robots to server.
        Simulator will keep a track of this to prune dead robots from the system.
        <br><br>
        <dd>robotID: ID number of the robot</dd>
        <dd>reality: V: virtual, R: real</dd>
    </td></tr>
</table>

### /robot/create

<table>
    <tr><td>Source</td><td>Localization System, Virtual Robot</td></tr>
    <tr><td>Destination</td><td>Simulator, Visualizer</td></tr>
    <tr><td>Data Type</td><td>JSON</td></tr>
    <tr><td>Sample Message</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                { "id":0, "x":10, "y":10, "heading":0.0, "reality": "R" }
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        This will be originated by virtual robots themselves at the beginning,
        or by the localization system for physical robots.
        Information taken by the <i>Simulator</i> will create a robot instance,
        in its Mixed Reality Environment and the <i>Visualizer</i> will create a robot geometry.
        <br><br>
        <dd>id: ID number of the robot</dd>
        <dd>x, y, z, heading : floating point number with 2 decimals</dd>
        <dd>reality: V: virtual, R: real</dd>
    </td></tr>
</table>

### /robot/delete

<table>
    <tr><td>Source</td><td>Simulator</td></tr>
    <tr><td>Destination</td><td>Visualizer</td></tr>
    <tr><td>Data Type</td><td>JSON</td></tr>
    <tr><td>Sample Message</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                { "id": <i>[robotID]</i> }
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        This will inform other systems to remove the robot.
        Invoked by the prune scheduler on the <i>Simulator</i>.
        <br><br>
        <dd>robotID: ID number of the robot</dd>
    </td></tr>
</table>

---
layout: default
parent: MQTT
grand_parent: Communication
title: Localization
nav_order: 3
permalink: communication/mqtt/localization

gh_link: docs/communication/mqtt/mqtt_localization.md
---

## Localization Protocols
{: .no_toc }

- TOC
{:toc}

###  /localization/data/?

<table>
    <tr><td>Source</td><td>Subsystem (Visualizer, Sandbox)</td></tr>
    <tr><td>Destination</td><td>Simulator</td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Message Format</td><td>
        {reality}
    </td></tr>
    <tr><td>Description</td><td>
        Subsystems can request robot coordinate details through this topic, with a reality filter.
        Simulator will reply coordinate list through the topic <i>/localization/data</i>
        <br><br>
        <dd>reality: M: mixed (default), V: virtual, R: real</dd>
    </td></tr>
</table>

###  /localization/data

<table>
    <tr><td>Source</td><td>Simulator</td></tr>
    <tr><td>Destination</td><td>Subsystems (Visualizer, Sandbox)</td></tr>
    <tr><td>Data Type</td><td>JSON List</td></tr>
    <tr><td>Sample Message</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                [
                {
                    "id": "<i>[robotID]</i>",
                    "x": "<i>[X]</i>",
                    "y": "<i>[Y]</i>",
                    "heading": "<i>[heading]</i>",
                    "reality": <i>[reality]</i>
                },
                ...
                ]
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        This is the response to the topic, <i>/localization/data/?</i>,
        a list of robot coordinates in requested reality.

        <br><br>
        <dd>id: ID number of the robot</dd>
        <dd>X,Y: Robot coordinate readings in centimeters</dd>
        <dd>heading: heading of the robot in degrees, 0=x+ direction</dd>
        <dd>reality: R: real, V:virtual, required</dd>

    </td></tr>
</table>



### /localization

<table>
    <tr><td>Source</td><td>Robot ( Physical | Virtual )</td></tr>
    <tr><td>Destination</td><td>Simulator</td></tr>
    <tr><td>Data Type</td><td>JSON</td></tr>
    <tr><td>Message Format</td><td>
        [robotId]
    </td></tr>
    <tr><td>Description</td><td>
        Both physical and virtual robots can publish into this topic to request their own localization details
        from the Simulator. This is mostly used by the hardware robots to correct their internal coordinate variables.
        They will receive the results through the topic <i>/localization/{robotId}</i>.

        <br><br>
        <dd>robotID: ID number of the robot</dd>
    </td></tr>
</table>

### /localization/{robotId}

<table>
    <tr><td>Source</td><td>Simulator</td></tr>
    <tr><td>Destination</td><td>Robot ( Physical | Virtual ) </td></tr>
    <tr><td>Data Type</td><td>JSON</td></tr>
    <tr><td>Message Format</td><td>
        {X} {Y} {heading}
    </td></tr>
    <tr><td>Description</td><td>
        Simulator will reply the robots coordinates to the robot that request their own
        coordinates. This will be sent as a response to the topic <i>/localization</i>

        <br><br>
        <dd>robotID: ID number of the robot</dd>
        <dd>X,Y: Robot coordinate readings in centimeters</dd>
        <dd>heading: heading of the robot in degrees, 0=x+ direction</dd>
    </td></tr>
</table>

###  /localization/update/?

<table>
    <tr><td>Source</td><td>Simulator</td></tr>
    <tr><td>Destination</td><td>Localization System, Virtual Robots
    </td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Message Format</td><td>
        ?
    </td></tr>
    <tr><td>Description</td><td>
        The simulator can request coordinate details from the
        Localization System (for physical robots) or Virtual Robots by publishing
        into this topic. Recomended to use this by Simulation, once it is started.
        This will receive the response through <i>/localization/update</i> topic.
    </td></tr>
</table>


###  /localization/update

<table>
    <tr><td>Source</td><td>Virtual Robots, Localization System</td></tr>
    <tr><td>Destination</td><td>Simulator</td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                [
                {
                    "id": "<i>[robotID]</i>",
                    "x": "<i>[X]</i>",
                    "y": "<i>[Y]</i>",
                    "heading": "<i>[heading]</i>",
                    "reality": <i>[reality]</i>
                },
                ...
                ]
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        Subsystems can inform the actual coordinates of the robots to the Simulator using this topic.
        Used by Localization System, to send a list of coordinates with <i>"reality": "R"</i>, and
        Virtual robots to send a single coordinate with <i>"reality": "V"</i>

        <br><br>
        <dd>robotID: ID number of the robot</dd>
        <dd>X,Y: Robot coordinate readings in centimeters</dd>
        <dd>heading: heading of the robot in degrees, 0=x+ direction</dd>
        <dd>reality: R: real, V:virtual, required</dd>
    </td></tr>
</table>

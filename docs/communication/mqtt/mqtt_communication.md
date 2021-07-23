---
layout: default
parent: MQTT
grand_parent: Communication
title: Communication
nav_order: 4
permalink: communication/mqtt/comm

gh_link: docs/communication/mqtt/mqtt_communication.md
---

## Communication Protocols
{: .no_toc }

- TOC
{:toc}

### /comm/in/simple/{robotID}

<table>
    <tr><td>Source</td><td> Server</td></tr>
    <tr><td>Destination</td><td> Robot</td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        <i>[message]</i>
    </td></tr>
    <tr><td>Description</td><td>
        The server will send a message sent via <i>simple communication</i> to a robot.
        A pure virtual implementation, receivers will be decided by the simulation server.

        <br><br>
        <dd>robotID: ID number of the robot</dd>
        <dd>message: The message string, max length: 64 chars</dd>
    </td></tr>

</table>

### /comm/in/direct/{robotID}

<table>
    <tr><td>Source</td><td> Server</td></tr>
    <tr><td>Destination</td><td> Robot</td></tr>
    <tr><td>Data Type</td><td> String</td></tr>
    <tr><td>Message Format</td><td>
        <i>[message]</i>
    </td></tr>
    <tr><td>Description</td><td>
        The server will send a message sent via <i>directed communication</i> to a robot.
        A pure virtual implementation, receivers will be decided by the simulation server.

        <br><br>
        <dd>robotID: ID number of the robot</dd>
        <dd>message: The message string, max length: 64 chars</dd>
    </td></tr>

</table>

### /comm/out/{protocol}

<table>
    <tr><td>Source</td><td> Robot</td></tr>
    <tr><td>Destination</td><td> Server</td></tr>
    <tr><td>Data Type</td><td> JSON</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                {
                    "id":[robotID],
                    "msg": "This is a sample",
                    "dist":[dist]
                }
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        The robots can transmit messages to other robots using an pre-implemented transmission protocol.
        Server will decide the robots who can receive the message.

        <br><br>
        <dd>protocol: simple, direct</dd>
        <dd>robotId: ID number of the robot</dd>
        <dd>message: The message string, max length: 64 chars</dd>
        <dd>dist (optional): maximum distance that message can be sent.</dd>
    </td></tr>

</table>

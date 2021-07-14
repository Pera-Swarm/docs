---
layout: default
parent: MQTT
grand_parent: Communication
title: Obstacles
nav_order: 5
permalink: communication/mqtt/obstacles

gh_link: docs/communication/mqtt/mqtt_obstacles.md
---

## Obstacles Protocols
{: .no_toc }

- TOC
{:toc}


### /obstacles/?

<table>
    <tr><td>Source</td><td>Visualizer</td></tr>
    <tr><td>Destination</td><td>Simulator</td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Message Format</td><td>
        {reality}
    </td></tr>
    <tr><td>Description</td>
        <td>
            The visualizer can request from the Simulator about obstacle data, filtered by the reality. Reply will be received through the topic <i>/obstacles</i>.

            <br><br>
            <dd>reality: M: mixed, V: virtual, R: real | default: M</dd>
        </td>
    </tr>
</table>

### /obstacles

<table>
    <tr><td>Source</td><td> Simulator </td></tr>
    <tr><td>Destination</td><td> Visualizer</td></tr>
    <tr><td>Data Type</td><td> JSON List</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                [
                Obstacle1,
                Obstacle2
                ]
            </code>
        </div>

    </td></tr>
    <tr><td>Description</td><td>
        The Simulator will send this as response to the <i>/obstacles/?</i> request.
        <strike>This is always a retained type message</strike>.

        <br><br>
        <dd>obstacle: Refer <a href="../json/obstacles"> Obstacle</a>
        JSON API definitions for learn more about Obstacle JSONs schema.</dd>
    </td></tr>
</table>

### /obstacles/delete

<table>
    <tr><td>Source</td><td> Simulator </td></tr>
    <tr><td>Destination</td><td> Visualizer</td></tr>
    <tr><td>Data Type</td><td> JSON</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                { "id": <i>[obstacle_Id]</i> }
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        Delete the obstacle from the environment, which has given id.
        <br><br>
        <dd>obstacle_Id: A randomly generated, unique UUID number of the obstacle,
            assigned by the Simulator, once it was created</dd>
        </td>
    </tr>
</table>

### /obstacles/delete/all

<table>
    <tr><td>Source</td><td> Simulator </td></tr>
    <tr><td>Destination</td><td> Visualizer</td></tr>
    <tr><td>Data Type</td><td> String </td></tr>
    <tr><td>Message Format</td><td>
        ?
    </td></tr>
    <tr><td>Description</td><td>
        Delete all the obstacles in the environment.
    </td></tr>
</table>

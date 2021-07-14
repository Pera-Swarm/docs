---
layout: default
parent: MQTT
grand_parent: Communication
title: NeoPixel LEDs
nav_order: 7
permalink: communication/mqtt/neopixel

gh_link: docs/communication/mqtt/mqtt_neopixel.md
---

## NeoPixel LED Protocols
{: .no_toc }

- TOC
{:toc}

###  /output/neopixel

<table>
    <tr><td>Source</td><td>Robot ( Physical | Virtual ) </td></tr>
    <tr><td>Destination</td><td>Server / GUI</td></tr>
    <tr><td>Data Type</td><td>JSON</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                {
                    "id": 10,
                    "R": <i>[R]</i>,
                    "G": <i>[B]</i>,
                    "B": <i>[B]</i>
                }
            </code>
        </div>
    </td></tr>
    <tr><td>Description</td><td>
        Broadcast the RGB values of robot's NeoPixel LED ring to the Server/ GUI through the topic.

        <br><br>
        <dd>id: ID number of the robot</dd>
        <dd>R,G,B: RGB color components | range: [0,255]</dd>
    </td></tr>
</table>

### /output/neopixel/{robotID}

<table>
    <tr><td>Source</td><td>Server</td></tr>
    <tr><td>Destination</td><td>Robot ( Physical | Virtual ) </td></tr>
    <tr><td>Data Type</td><td>String</td></tr>
    <tr><td>Messaage Format</td><td>
        [R] [G] [B]
    </td></tr>
    <tr><td>Description</td><td>
        Server can ask from robot to change their colors by using the topic <i>/output/neopixel/{robotID}</i>
        <br><br>
        <dd>robotID: ID number of the robot</dd>
        <dd>R,G,B: RGB color components | range: [0,255]</dd>
    </td></tr>
</table>

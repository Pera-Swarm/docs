---
layout: default
parent: MQTT
grand_parent: Communication
title: Config
nav_order: 8
permalink: communication/mqtt/config

gh_link: docs/communication/mqtt/mqtt_config.md
---

## Config Protocols
{: .no_toc }

- TOC
{:toc}


### /config/arena

<table>
    <tr><td>Source</td><td> Simulator </td></tr>
    <tr><td>Destination</td><td> Visualizer</td></tr>
    <tr><td>Data Type</td><td> JSON List</td></tr>
    <tr><td>Message Format</td><td>
        <div class="language-json highlighter-rouge">
            <code class="highlight">
                { "xMin": <i>[number]</i>, "xMax": <i>[number]</i>, "yMin": <i>[number]</i>, "yMax": <i>[number]</i>, "units": "virtual" }
            </code>
        </div>

    </td></tr>
    <tr><td>Description</td><td>
        The Simulator will send this at the start, inclusing the arean configuration details. Visualizer will use this to override it's own default arena configuration details.
    </td></tr>
</table>

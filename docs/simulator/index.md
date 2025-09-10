---
layout: default
title: Simulator
permalink: simulator/

nav_order: 5
has_children: true
has_toc: false
---

# Mixed Reality Simulator

Mixed reality-based swarm simulator that supports both virtual and physical robots in the same environment. The simulator is built using Node.js and uses MQTT protocol for communication. The simulator can be used to support physical and virtual robots in the same environment.

{: .no_toc }

![Node.js CI](https://github.com/Pera-Swarm/e15-fyp-swarm-server/workflows/Node.js%20CI/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## System Requirements

Please install node dependencies as follows. Make sure you have Node.js and npm installed.

```bash
npm install
```

| It is recommended to use Node 16 or newer version

### Environment Variables

Please copy the _sample.env_ file and rename into _.env_ and complete the configurations for HTTP and MQTT

```bash
MQTT_HOST=mqtt://localhost
MQTT_USER=user
MQTT_PASS=password
MQTT_CLIENT=mqtt_server
MQTT_CHANNEL=v1

ARENA_CONFIG="./app/config/arena/{arena_config}.json"

LOG_LEVEL='info'
```

### Run/Deployment

#### Local Deployment

```bash
# Dev Server with live reload
npm run dev

# Production ready build
npm run start
```

#### Production Deployment

```bash
# Install PM2 globally (if not yet)
sudo npm i -g pm2

# Start the server (give a proper server name)
pm2 start app/index.js --name {server_name}

# Generate and register a systemd unit for PM2
# This command above prints another command with sudo, and copy/paste that into CLI
pm2 startup systemd

# Persist the current PM2 process list
pm2 save

# Restart the server
pm2 restart {server_name}

# Stop the server
pm2 stop {server_name}
```

### Architecture

{% include thumbnail.html src="/docs/assets/images/simulator/simulator_overview.png" alt="Simulator Architecture" %}

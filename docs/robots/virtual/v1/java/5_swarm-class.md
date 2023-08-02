---
layout: default
parent: Java Robot
grand_parent: Virtual Robots
title: Swarm Class
nav_order: 5
permalink: robots/virtual/v1/java/swarm-class/

gh_link: docs/robots/virtual/v1/java/4_swarm-class.md
---

# Swarm Class
{: .no_toc }

This Swarm class is now renamed as `App`, according to the standard naming convention for Java programs. The file can be found on `/src/main/java/App.java`. 

##### Table of content
{: .no_toc }
- TOC
{:toc}

---

## Introduction

This class is similar to most of the standard Java classes that will be used as an entry point to a program. The structure is as below:

```java 
import swarm.configs.MQTTSettings;
import swarm.robot.VirtualRobot;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import Robots.samples.SampleRobot;

public class App {

    public static void main(String[] args) {

        try {
            // COMPLETE THIS BEFORE RUN
            // Read config properties from the file, src/resources/config/mqtt.properties
            // If it isn't there, please make one, as given sample in the
            // 'sample_mqtt.properties' file

            File configFile = new File("src/resources/config/mqtt.properties");
            FileReader reader = new FileReader(configFile);
            Properties props = new Properties();
            props.load(reader);

            MQTTSettings.server = props.getProperty("server");
            MQTTSettings.port = Integer.parseInt(props.getProperty("port", "1883"));
            MQTTSettings.userName = props.getProperty("username");
            MQTTSettings.password = props.getProperty("password");
            MQTTSettings.channel = props.getProperty("channel", "v1");
            reader.close();

            VirtualRobot robot = new SampleRobot(10, -52, 32, 45);
            new Thread(robot).start();

        } catch (FileNotFoundException ex) {
            // file does not exist
            System.out.println("File Not Found !!!");

        } catch (IOException ex) {
            // I/O error
            System.out.println("IO Error !!!");
        }
    }

}
```

### Create an Experiment

#### With a single robot 

- First, it will try to load the configuration file, and apply the configuration values into the `MQTTSettings` class. These config values will define the MQTT broker need to be used for communicate with the simulator application.

- You can use a code snippet like following to initiate a single Virtual Robot instance. Insted of `SampleRobot`, you can use your own implementation. 

```java 
int id = 0; // an uniquire identifier for each robot
int x = 10; // starting x coordinate
int y = 20; // starting y coordinate
int heading = 45; // heading direction in degrees 

VirtualRobot robot = new SampleRobot(id, x, y, heading);
new Thread(robot).start();
```

#### With a group of robot 

- You can write a code snippet like below for start a group of robots. However, initiating multiple robots can cause to the simulation performance, since robots are working on different threads.

```java 
int[] robotList = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

int startX = 0;
int startY = 0;
int startHeading = 90;

Robot[] vr = new VirtualRobot[robotList.length];

for (int i = 0; i < robotList.length; i++) {
    vr[i] = new SampleRobot(robotList[i], startX + 40 * i, startY + 50 * i,
            startHeading + 10 * i);
    new Thread(vr[i]).start();
}
```
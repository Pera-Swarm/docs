---
layout: default
parent: Firmware
grand_parent: Virtual Robots
title: Setup Guide
nav_order: 1
permalink: robots/virtual/v1/firmware/setup-guide/

gh_link: docs/robots/virtual/v1/firmware/1_setup-guide.md
---

# Setup Guide
{: .no_toc }

##### Table of content
{: .no_toc }
- TOC
{:toc}

----
## Getting Started

### What is Maven ?

Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information. Using maven we can build and manage any Java based project.

### Why Maven was used ?

Since this repository is based on OOP concepts and have a few dependencies on ready made libraries, it was required to have a proper project management and dependency management tool. It will help to build the project easily.  


## Getting started with Java Library

If you need to update the core functionalities, while the robot implementations, you need to  fork and clone the repository, [github.com/Pera-Swarm/robot-library-java](https://github.com/Pera-Swarm/robot-library-java){:target="_blank"} first. Then you need to install the dependencies and compile the project with your changes.

It is recommended to use a IDE like **Visual Studio Code** / **IntelliJ IDEA**, since it will help you to install dependencies easily.

- Download the repository from [github.com/Pera-Swarm/robot-library-java](https://github.com/Pera-Swarm/robot-library-java){:target="_blank"}
- Once you download the repository, you need to copy the 'src/resources/config/sample_mqtt.properties' file and create 'src/resources/config/sample_mqtt.properties'.

- You need to update the following values with the values of the **MQTT Broker** you are using.

```bash
server=127.0.0.1
port=1883
username=user
password=pass
channel=v1
```

- Install Packages and Dependencies using **mvn install** command
- Compile using **mvn compile** command
- You can open the 'src/main/java/swarm/Swarm.java' file and run it using the **Run** or **Debug** option in the IDE to initiate the running of the implementation.


Auto-generated full documentation can be found in [http://pera-swarm.ce.pdn.ac.lk/robot-library-java/](http://pera-swarm.ce.pdn.ac.lk/robot-library-java/).

{% include alert.html message="It is assumed that you already installed *Java JRE* and *Maven Build Tool*." type="alert-primary" type="alert-warning" %}

## Getting started with pre-build environment

If you are interested in only the robot functionalities, not the core functionalities, you can start with the *pre-build / pre-compiled* JAR file.

You need to fork and clone the repository, [github.com/Pera-Swarm/java-robot](https://github.com/Pera-Swarm/java-robot){:target="_blank"} and implement the *Robot Class* as provided examples.


{% include alert.html message="Remaining Under Construction" type="alert-primary" %}


Additionally, you can import the latest version of the Java Library from Maven Package Regisotry, by adding the below XML code into your pom.xml. Replace the text, **VERSION** with the latest release can be found in [here](https://github.com/Pera-Swarm/robot-library-java/packages/)

```xml 
<dependency>
  <groupId>pera.swarm</groupId>
  <artifactId>java-robot</artifactId>
  <version>{{ VERSION }}</version>
</dependency>
```

## Additional Readings

- [Maven - Environment Setup](https://www.tutorialspoint.com/maven/maven_environment_setup.htm){:target="_blank"}

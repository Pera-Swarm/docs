---
layout: default
parent: Java Robot
grand_parent: Virtual Robots
title: Java Robot Library
nav_order: 2
permalink: robots/virtual/v1/java/setup-guide-library/

gh_link: docs/robots/virtual/v1/java/2_setup-guide-library.md
---

# Setup Guide for the Java Robot Library
{: .no_toc }

The **Java Robot Library** is the core of the Java Robots, which is implemented on Java, based on OOP concepts, and build using the Maven build system. It will be also available through Maven Package Repository maintained by GitHub from [here](https://github.com/Pera-Swarm/robot-library-java/packages).

This will guide you to setup the core library of the Pera-Swarm virtual robots, by importing the necessary dependencies, and doing the configurations.

##### Table of content
{: .no_toc }
- TOC
{:toc}

----

## Getting started

If you need to update the core functionalities, while the robot implementations, you need to  fork and clone the repository, [Pera-Swarm/robot-library-java](https://github.com/Pera-Swarm/robot-library-java){:target="_blank"} first. Then you need to install the dependencies and compile the project with your changes, and later work on a release.

It is recommended to use an IDE like **Visual Studio Code** / **IntelliJ IDEA**, since it will help you to install dependencies easily.

- Download the repository from [Pera-Swarm/robot-library-java](https://github.com/Pera-Swarm/robot-library-java){:target="_blank"}

- Once you download the repository, you need to copy the `src/resources/config/sample_mqtt.properties` file and create `src/resources/config/sample_mqtt.properties`.

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
- You can open the `src/main/java/swarm/App.java` file and run it using the **Run** or **Debug** option in the IDE to initiate the running of the implementation.


Auto-generated full documentation of the available _Class_ and _Methods_ can be found at [http://pera-swarm.ce.pdn.ac.lk/robot-library-java/](http://pera-swarm.ce.pdn.ac.lk/robot-library-java/).

{% include alert.html message="It is assumed that you already installed _Java Runtime Environment_ and _Maven Build Tool_." type="alert-primary" type="alert-warning" %}

## Publishing a new version 

- You need to update the version of the package in the **./pom.xml** file, with the version you hope to release. 

```xml 
<groupId>pera.swarm</groupId>
<artifactId>java-robot</artifactId>
<version>1.0.0</version>
```

- Next, you can prepare the release via GitHub from [here](https://github.com/Pera-Swarm/robot-library-java/releases). The release process will be done automatically via [Maven Publish](https://github.com/Pera-Swarm/robot-library-java/blob/main/.github/workflows/maven-publish.yml) GitHub CI Action workflow at a release.

- Next, you can use the following code block to use the Java Library on your Maven Projects. Replace the &lt;version&gt;1.0.0&lt;/version&gt; with the version you want to use. (Please note that to use this Maven library, you need to Authenticate with a GitHub token. Further info is available [here]({{ '/robots/virtual/v1/java/setup-guide/' | relative_url }}).) 

```xml 
<dependency>
  <groupId>pera.swarm</groupId>
  <artifactId>java-robot</artifactId>
  <version>1.0.0</version>
</dependency>
```


## Additional Readings

### What is Maven ?

Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information. Using maven we can build and manage any Java based project.

### Why Maven was used ?

Since this repository is based on OOP concepts and have a few dependencies on ready made libraries, it was required to have a proper project management and dependency management tool. It will help to build the project easily.  

- [Maven - Environment Setup](https://www.tutorialspoint.com/maven/maven_environment_setup.htm){:target="_blank"}

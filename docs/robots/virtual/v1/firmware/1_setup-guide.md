---
layout: default
parent: Firmware
grand_parent: Virtual Robots
title: Setup Guide
nav_order: 1
permalink: robots/virtual/firmware/v1/setup-guide/

gh_link: docs/robots/virtual/v1/firmware/1_setup-guide.md
---

# Setup Guide
{: .no_toc }

### Table of content
{: .no_toc }
- TOC
{:toc}

----
## Getting Started

### What is Maven ?

Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information. Using maven we can build and manage any Java based project.

### Why Maven was used ?

Since this repository is based on OOP concepts and have a few dependencies on ready made libraries, it was required to have a proper project management and dependency management tool. It will help to build the project easily.  


## Getting started with entire build environment

If you need to update the core functionalities, while the robot implementations, you need to  fork and clone the repository, [github.com/Pera-Swarm/java-swarm-node](https://github.com/Pera-Swarm/java-swarm-node){:target="_blank"} first. Then you need to install the dependencies and compile the project with your changes.

It is recommended to use a IDE like **IntelliJ IDEA**, since it will help you to install dependencies easily.

<!-- TODO: @Dilshani, can you write the rest with instructions? -->


## Getting started with pre-build environment

If you are interested in only the robot functionalities, not the core functionalities, you can start with the *pre-build / pre-compiled* JAR file.

You need to fork and clone the repository, [github.com/Pera-Swarm/java-robot](https://github.com/Pera-Swarm/java-robot){:target="_blank"} and implement the *Robot Class* as provided examples.

{% include alert.html message="Remaining Under Construction" type="alert-primary" %}

## Additional Readings

- [Maven - Environment Setup](https://www.tutorialspoint.com/maven/maven_environment_setup.htm){:target="_blank"}

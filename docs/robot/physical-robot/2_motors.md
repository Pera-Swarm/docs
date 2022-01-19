---
layout: default
parent: Physical Robot
grand_parent: Robots
title: Motor Library
nav_order: 2
permalink: robot/physical-robot/motor_library

gh_link: docs/robot/physical-robot/2_motors.md
---

# Motor Library
{: .no_toc }

### Table of content
{: .no_toc }
- TOC
{:toc}

----
# Motors

To add the motors of the Swarm-Robot, you need to include the following header file.

```cpp
#include "src/SW_Motors.h"
```

You can turn on or off the motors library functionality by comment out and comment in the following definition. (in features.h)

```cpp
#define ENABLE_MOTORS
```

There are two types of motors drivers are supported.

1.Servo Drive

**Warning: This is discontinued implementation**

With this, you can connect continuous rotation servo motors directly to the 'motor connector' in the robot controller board. To enable this, you must uncomment #define DRIVE_SERVO in features.h

Available functions:
```cpp
void SW_Motors::write(int16_t leftSpeed, int16_t rightSpeed)
void SW_Motors::stop()		// Stop motors
void SW_Motors::attach()   	// Attach Servo motors
void SW_Motors::detach()   	// Detach Servo motors
```

2.PWM Drive

With this, you can connect any standard motors through a H-bridge motor driver to the controller board. Please refer *MotorDriver daughter board* (will be updated soon) for detailed technical information.

To enable this, you must uncomment #define DRIVE_PWM in features.h.

## Setup the Motors

To initiate the *Robot_Motors*, you need to use motors.begin(). If motors were enabled by 'ENABLE_MOTORS' directive, it will print a message like '>> Motors  :enabled,servoMode' or '>> Motors  :enabled,pwmMode' according to the enabled motor driver.

```cpp
SW_Motors motors;
motors.begin();
```

## Motor Functions

### motors.write(leftSpeed, rightSpeed);

This will write PWM value to motors. *leftSpeed* and *rightSpeed* values must be an integer between [-255,255].
Positive integer values will rotate motors forward and negative ones will rotate motors backward with the given speed.

```cpp
motors.write(int16_t leftSpeed, int16_t rightSpeed);
```

### motors.stop();

This will turn off both motors.

```cpp
motors.stop();
```

The following function will stop both motors after a delay of given milliseconds.

```cpp
motors.stop(int16_t delay);
```

### motors.test();

This is used to test the functionality of the motors. It will execute the following procedures once called.
- Turn Counter Clockwise for ~0.5 seconds.
- Turn Clockwise for ~0.5 seconds.
- Move forward with increasing speed for ~6.5 seconds.
- Move forward with decreasing speed for ~6.5 seconds.
- Move backward with increasing speed for ~6.5 seconds.
- Move backward with decreasing speed for ~6.5 seconds.

```cpp
motors.test()
```

## Configurations

In addition to the above functions, there are two publicly accessible variables to adjust the drift of the motors.
The values should be stored in EEPROM memory and write into variables during *memory.begin()*.

Following will update the error correction values on the memory.
- Default: 0
- Max: 127
- Min: -128

```cpp
memory.setErrorCorrection(LEFT, 0);
memory.setErrorCorrection(RIGHT, 0);
```

Set the error correction values to the motors. This can be updated at any time after motors are initiated.
```cpp
motors.rightCorrection =  memory.getErrorCorrection(RIGHT);
motors.leftCorrection = memory.getErrorCorrection(LEFT);

```


----
# Wheel Encoders

Robot wheels come with optical rotary encoders. There are 36 holes in the robot wheel, therefore 36 signals microcontroller will be captured once the wheel makes a full turn. Since the diameter of the wheel is 34mm, the perimeter of the wheel is 106.8mm. Then one tick of the rotary encoder represents a movement of nearly 3mm.

One thing to note that, since there is only one counter for a wheel, and it can't detect the direction of the rotation. So it is recommended that the values should read and reset every time the rotation direction of the wheels is changing.

**TODO**: implement to take the rotation direction from *motors.write()* and correct the counting readings at software level.

## Encoder Functions

```cpp
void SW_Motors::enableEncoders();
void SW_Motors::encoderReset();
int SW_Motors::encoderAverage();
void SW_Motors::encoderPrint();
```

### void enableEncoders();

This will enable the encoders by attaching the microcontroller's internal counter to the IR speed encoder module and reset the counter values to 0.

```cpp
motors.enableEncoders();
```

### void encoderReset();

This will clean the counter values.

```cpp
motors.encoderReset();
```

### uint encoderAverage();

This will return the average reading of the left and right counters as an unsigned integer.

```cpp
int a = motors.encoderAverage();
```

### uint getEncoderReading(uint8_t wheel);

This will return the average reading of either left or right counter as an unsigned integer.

```cpp
int right = motors.getEncoderReading(RIGHT);
int left = motors.getEncoderReading(LEFT);
```

### void encoderPrint();

This will print the current encoder reading of both sensors.

```cpp
motors.encoderPrint();
```
example:
```bash
Encoder L:10 R:20
```


## Additional Readings

- [H bridge Motor Driver Circuit](https://www.circuitstoday.com/h-bridge-motor-driver-circuit){:target="_blank"}
- [A guide on Motor Speed Sensor](https://www.teachmemicro.com/lm393-ir-module-motor-speed-sensor/){:target="_blank"}

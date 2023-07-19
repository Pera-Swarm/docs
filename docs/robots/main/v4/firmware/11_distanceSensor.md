---
layout: default
parent: Firmware
grand_parent: Main Robots
title: Distance Sensor Library
nav_order: 11
permalink: robots/v4/firmware/distance_library

gh_link: docs/robots/main/v4/firmware/11_distanceSensors.md
---

# Distance Sensor Library
{: .no_toc }

### Table of content
{: .no_toc }

- TOC
{:toc}

----

To enable the distance sensor of the robot, you need to uncomment the following line in the *features.h* first.

```cpp
#define ENABLE_DISTANCE_SENSOR   
```

Implementations are available for two distance sensors.
1. GP2Y0A21YK0F Analog Distance Sensor
2. VL53LX0 ToF Sensor

GP2Y0A21YK0F support is now discontinued, but you can still use it by defining the correct PIN to use for analog operation from the sensor.

```cpp
// File: ./src/def_pins.h
#define PIN_DIST_SENSOR 32

```

VL53LX0 ToF Sensor uses an I2C channel with I2C address 0x2A for its operations. So no need for additional configurations for it.

To select one of the above-mentioned distance sensors,  you need to uncomment the relevant line of the below code in *features.h*

```cpp
// #define DISTANCE_GP2Y0A21YK0F
// #define DISTANCE_VL53LX0
```

## Setup the Sensor

After defined the distance sensor options, you can import the header file of the distance sensor and initiate a distance sensor object. It is recommended that not to update any of the below.

```cpp
#include "src/SW_Distance.h"
SW_Distance distance;
```

## Available Functions

The following are available for both GP2Y0A21YK0F and VL53LX0 distance sensors.

```cpp
SW_Distance::SW_Distance()

void SW_Distance::begin()
void SW_Distance::setFilterRate(float rate)
uint16_t SW_Distance::getRawDistance( bool avoidBurstRead )
float SW_Distance::getDistanceFloat(bool avoidBurstRead )
uint16_t SW_Distance::getDistanceInt(bool avoidBurstRead )
void SW_Distance::test()
```

### distance.begin();

You need to call the following function to setup the distance sensor in method *setup()*.

```cpp
distance.begin();
```

If you are using the GP2Y0A21YK0F sensor, it will print a message like '>> Dist.Sensor :enabled, GP2Y0A21YK0F' or, if you are using the VL53LX0 sensor, it will print a message like '>> Dist.Sensor :enabled, VL53LX0' in the Serial Monitor.

### getRawDistance( bool avoidBurstRead );

If there no obstacle found within the range *DISTANCE_MAX_THRESHOLD* (defined in src/SW_Distance.h) the function will return *DISTANCE_MAX_THRESHOLD*.

If the range reading of the sensor is equal or less than *DISTANCE_MIN_THRESHOLD* (defined in src/SW_Distance.h) the function will return *DISTANCE_MAX_THRESHOLD* (this is an observation based result, if no obstacle within the max range of the sensor, it will return a small value, less than this *DISTANCE_MIN_THRESHOLD*).

Otherwise, this will return the raw distance reading as a 16-bit integer; the distance in mm. (after correcting the reading with *DISTANCE_OFFSET*)

If the boolean flag *avoidBurstRead* is set to *true*, it will add a DISTANCE_BURST_DELAY amount of  milliseconds before reading. (defined in src/SW_Distance.h, the default is 20). This will help in taking continuous readings from the sensor. The default value is *true*.

```cpp
uint16_t d = distance.getRawDistance(); // with a delay
uint16_t d = distance.getRawDistance(false); // without a delay
```

### getDistanceFloat( bool avoidBurstRead );

Return the raw distance reading in millimeters as a floating point number.

```cpp
float d = distance.getDistanceFloat(bool avoidBurstRead);
```

### getDistanceInt( bool avoidBurstRead );

Return the distance reading in millimeters as a 16-bit integer. TODO: need to implement a mathematical filter inside this function for VL53LX0 sensor

```cpp
uint16_t d = distance.getDistanceInt(bool avoidBurstRead);
```

### test();

Used as a test pattern. Prints the raw distance sensor into *Serial Monitor*.

```cpp
distance.test()
```

## Configurations

### setFilterRate(float alpha);

Can configure the alpha value of the exponential filter. Currently only used for GP2Y0A21YK0F distance sensor.

```cpp
distance.setFilterRate( float alpha )
```

Filter function:
```
average = (alpha * reading)  + ((1 - alpha) * average);
```


Apart from the Filter Rate, it is possible to configure the following parameters in the *SW_Distance.h*

```cpp
// If the distance reading is greater than this, distance function returns -1
#define DISTANCE_MAX_THRESHOLD 800

// Burst reading delay
#define DISTANCE_BURST_DELAY 20

// The correction value for the difference between sensor and robot's center.
// Positive means the sensor is in front of the center of the robot by that given value.
#define DISTANCE_OFFSET 30
```

## Additional Readings

- [Datasheet: GP2Y0A21YK0F](https://global.sharp/products/device/lineup/data/pdf/datasheet/gp2y0a21yk_e.pdf){:target="_blank"}
- [Datasheet: VL53LX0](https://www.st.com/resource/en/datasheet/vl53l0x.pdf){:target="_blank"}
- [Time of Flight Micro-LIDAR Distance Sensor](https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/arduino-code){:target="_blank"}

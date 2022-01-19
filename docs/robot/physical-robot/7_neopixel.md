---
layout: default
parent: Physical Robot
grand_parent: Robots
title: Neopixel LED Library
nav_order: 7
permalink: robot/physical-robot/neopixel_library

gh_link: docs/robot/physical-robot/7_neopixel.md
---

# Neopixel LED Library
{: .no_toc }

### Table of content
{: .no_toc }

- TOC
{:toc}

----
## Getting started

Neopixel LED array contains 21 WS2812 addressable LEDs and 20 of them displayed in the outer ring of the robot. (First LED isn't exposed to the outside) This robot is using [Adafruit Neopixel](https://github.com/adafruit/Adafruit_NeoPixel){:target="_blank"} library to control the NeoPixels.

To enable the NeoPixel LED ring, the following should be uncommented in *features.h*.

```cpp
#define ENABLE_NEOPIXEL_RING
```

## Setup

The followings are the definitions and the constructor used for the NeoPixels. We recommended to keep them as default.

```cpp
#include <Adafruit_NeoPixel.h>

#define PIN_NEOPIXEL_LED    23
#define NEOPIXEL_LED_COUNT  21
#define NEOPIXEL_BRIGHTNESS 50
#define DELAYVAL 150

Adafruit_NeoPixel neopixel(NEOPIXEL_LED_COUNT, PIN_NEOPIXEL_LED, NEO_GRB + NEO_KHZ800);

```

*beginNeoPixel()* function should be called in the *setup()* function to begin the NeoPixel ring properly.

```cpp
void beginNeoPixel();
```


## Available Library Functions

Following functions can be accessed through the Adafruit Library


### neopixel.setPixelColor(n, r, g, b)

Set a pixel's color using separate red, green, and blue components.

- n: Pixel index, starting from 0
- r: Red brightness, 0 = minimum (off), 255 = maximum
- g: Green brightness, 0 = minimum (off), 255 = maximum
- b: Blue brightness, 0 = minimum (off), 255 = maximum

```cpp
void setPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b);
```

### neopixel.getPixelColor(n)

Query the color of a previously-set pixel.

- n: Index of pixel to read (0 = first).

```cpp
uint32_t Adafruit_NeoPixel::getPixelColor(uint16_t n);

```

### neopixel.Color(r, g, b);

Convert separate red, green and blue values into a single packed 32-bit RGB color

- r: Red brightness, 0 = minimum (off), 255 = maximum
- g: Green brightness, 0 = minimum (off), 255 = maximum
- b: Blue brightness, 0 = minimum (off), 255 = maximum

```cpp
static uint32_t Color(uint8_t r, uint8_t g, uint8_t b)
```

###  neopixel.ColorHSV(hue, sat, val)

Convert hue, saturation, and value into a packed 32-bit RGB color that can be passed to setPixelColor() or other RGB-compatible functions.

- hue:  Hue, an unsigned 16-bit value, 0 to 65535, representing one full loop of the color wheel
- sat:  Saturation, 8-bit value, 0 (min or pure grayscale) to 255
- val:  Value, brightness, 8-bit, 0 (off) to 255 (full brightness). The default of 255 if unspecified

```cpp
uint32_t ColorHSV(uint16_t hue, uint8_t sat, uint8_t val);
```

### neopixel.fill(c, first, count)

Fill all or part of the NeoPixel strip with a color, c

- c: 32-bit color value
- first: Index of the first pixel to fill
- count: Number of pixels to fill

```cpp
void fill(uint32_t c=0, uint16_t first=0, uint16_t count=0);
```

### neopixel.setBrightness(b)

Adjust output brightness. Does not immediately affect what's currently displayed on the LEDs. The next call to show() will refresh the LEDs at this level.

- b: 0=minimum (off), 255=brightest

```cpp
void setBrightness(uint8_t b);
```

### neopixel.show()

Transmit pixel data in the microcontroller to NeoPixels.

```cpp
void show();
```

### neopixel.clear();
Fill the whole NeoPixel strip with 0 / black / off.

```cpp
void clear();
```


## Implemented Functions

Followings are implemented in **neoPixel.ino**.

```cpp
// A test for the functionality of the strip
void neoPixelTest();

// Fill the strip with the given color
void pixelShowColor(int r, int g, int b);

// Make sequential wave of given color from back corners to the front-mid.
void pixelColorWave(int r, int g, int b);

// Make a wipe of color from left to right with the given color
void colorWipe(uint32_t color, int wait);

// Turn off all NeoPixels
void pixelOff();

// Test patterns used in neoPixelTest()
void whiteOverRainbow(int whiteSpeed, int whiteLength);
void rainbowFade2White(int wait, int rainbowLoops, int whiteLoops);
```

## Additional Readings

- [Adafruit NeoPixel Library](https://github.com/adafruit/Adafruit_NeoPixel){:target="_blank"}
- [WS2812B Datasheet](https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf){:target="_blank"}

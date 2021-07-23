---
layout: default
parent: JSON
grand_parent: Communication
title: Obstacles
nav_order: 1
permalink: communication/json/obstacles/

gh_link: docs/communication/mqtt/mqtt_localization.md
---

# Obstacles JSON

Following JSON Schemas are used to communicate obstacle details from the simualtor to visualizer.
(Not a fully completed yet)


```js
{
    id: 1000,
    name: "Obstacle Name",
    reality: [reality],
    geometry: { … },
    material : { … },
    position: { x: 0, y: 0 },
    rotation:{ x: 0,  y: 0,  z: 0 }
}
```

### Name

A name can be provided to the obstacles using the *name* parameter in *env.config.json* file.

### Reality

- V: virtual (default)
- R: real

### Geometry

Available geometric shapes, with parameters:
- Box Geometry

    - width: required, ex: 300,
    - height: required, ex: 5,
    - depth: required, ex: 20

- Cylinder Geometry

    - radiusTop: required, ex: 20,
    - radiusBottom: required, ex: 20,
    - height: required, ex: 20
    - heightSegments: optional, default: 2
    - radialSegments: optional, default: 16

- Sphere Geometry

    - radius: required, ex: 20
    - widthSegments: optional, default: 16
    - heightSegments: optional, default: 16

#### Geometry for a box shaped object:
```js
{
    type: 'BoxGeometry',
    width: 300,
    height: 5,
    depth: 20
}
```

#### Geometry for a cylinder shaped object:
```js
{
    type: 'CylinderGeometry',
    radiusTop: 20,
    radiusBottom: 20,
    height: 20
}
```

#### Geometry for a sphere shaped object:
```js
{
    type: 'SphereGeometry',
    radius: 20
}
```

### Material

Available materials:
- MeshBasicMaterial
[https://threejs.org/docs/#api/en/materials/MeshBasicMaterial]()

- MeshNormalMaterial
[https://threejs.org/docs/api/en/materials/MeshNormalMaterial.html]()

- MeshPhongMaterial
[https://threejs.org/docs/#api/en/materials/MeshPhongMaterial]()

- MeshPhysicalMaterial
[https://threejs.org/docs/#api/en/materials/MeshPhysicalMaterial]()

- MeshStandardMaterial
[https://threejs.org/docs/#api/en/materials/MeshStandardMaterial]()

Example:
```js
{
    type: 'MeshPhysicalMaterial',
    properties: {
        color:0x7602f9,
    }
}
```

Full Example:
```js
{
  "geometry":{"type":"BoxGeometry","width":300,"height":20,"depth":5},
  "material":{"type":"MeshPhysicalMaterial","properties":{"color":7734009}},
  "position":{"x":0,"y":0},
  "rotation":{"x":0,"y":0,"z":0}
}
```

### Position

<dd>x: X coordinate of the object</dd>
<dd>y: Y coordinate of the object</dd>
<dd>z: Z coordinate of the object | optional</dd>

### Rotation

<dd>x: rotation through the x-axis of the object</dd>
<dd>y: rotation through the y-axis of the object</dd>
<dd>z: rotation through the z-axis of the object</dd>

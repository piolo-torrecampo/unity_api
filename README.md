# DATA STRUCTURE

#### TABLE OF CONENTS
- [scale](#scale)
- [rotation](#rotation)
- [remove](#remove)
- [replace](#replace)

## SCALE
Scale is a the tool for making the object bigger.
```
{
    "prompt": "Double the scale of the cube x axis",
    "action": "scale",
    "prefab": "Cube", 
    "axis": "x", // x, y, z, all, increase, decrease
    "value": "2" // no limit (can destroy the scene)
}
```
### Parameters
Name | Data Type | Description
| -- | -- | -- | 
prompt | string | prompt of the user
action | string | action performed by unity
prefab | string | 3d object name
axis | string | target axis to scale
value | float | number of units to be applied for scaling


## ROTATION
This tool allows to rotate specific object in the scene.
```
{
    "prompt": "Rotate the cube at 90 degrees in x axis",
    "action": "rotate",
    "prefab": "Cube",
    "axis": "x", // x, y, z
    "value": "45" // -360 to 360
}
```
### Parameters
Name | Data Type | Description
| -- | -- | -- | 
prompt | string | prompt of the user
action | string | action performed by unity
prefab | string | 3d object name
axis | string | target axis to rotate
value | float | degrees of rotation


## REMOVE
This tool allows to remove a specific object in the scene.
```
{
    "prompt": "Remove 5 cube",
    "action": "remove",
    "prefab": "Cube",
    "value": "5" // can be any number
}
```
### Parameters
Name | Data Type | Description
| -- | -- | -- | 
prompt | string | prompt of the user
action | string | action performed by unity
prefab | string | 3d object tag name
value | float | quantity of the 3d object/s that will be remove


## REPLACE
This tool allows to replace a specific object in the scene and put another object in the same place.
```
{
    "prompt": "Replace the cube to Sphere",
    "action": "replace",
    "prefab": "Sphere",
    "object_to_replace": "Cube" 
}
```
### Parameters
Name | Data Type | Description
| -- | -- | -- | 
prompt | string | prompt of the user
action | string | action performed by unity
prefab | string | 3d object name under resources folder
object_to_replace | string| name of old object

## MOVE
This tool allows to move a specific object in the scene. 
```
{
    "prompt": "Move the cube to the right",
    "action": "move",
    "prefab": "Cube",
    "direction": "bottom", // top, left, right, bottom, front, back
    "value": "1" // units
}
```
### Parameters
Name | Data Type | Description
| -- | -- | -- | 
prompt | string | prompt of the user
action | string | action performed by unity
prefab | string | 3d object name under resources folder
direction | string | direction of the next movement of the object
object_to_replace | string| name of old object

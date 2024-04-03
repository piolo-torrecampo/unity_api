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
    "prompt": "Double the scale of the workbench",
    "action": "scale",
    "parameters": {
        "prefab": "workbench",
        "axis": "all", "x", // x, y, z, all, increase, decrease
        "value": "2" // no limit
    }
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
    "prompt": "Rotate the workbench at 45 degrees in z axis",
    "action": "rotate",
    "parameters": {
        "prefab": "workbench",
        "axis": "z", // x, y, z
        "value": "45" // -360 to 360
    }
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
    "prompt": "Romeve workbench",
    "action": "remove",
    "parameters": {
        "prefab": "workbench",
        "value": "1" // can be any number
    }  
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
    "prompt": "Replace the cube to workbench",
    "action": "replace",
    "parameters": {
        "prefab": "Cube",
        "object_to_replace": "workbench"
    }   
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
    "prompt": "Move the workbench to the right",
    "action": "move",
    "parameters": {
        "prefab": "workbench",
        "direction": "right", // top, left, right, bottom, front, back
        "value": "1"
    }
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

from flask import Flask, request, jsonify
import json
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


currentInstruction = {
    "action": "",
    "parameters": ""

}

errorResponse = {
    "message": ""
}

"""
actions = ['insert', 'duplicate', 'delete', 'move', 'replace', 'rotate', 'scale']
insert_params = ['reference_object', 'prefab', 'direction', 'value']
duplicate_params = ['prefab', 'axis']
move_params = ['prefab', 'direction', 'value']
remove_params = ['prefab', 'value']
replace_params = ['prefab', 'object_to_replace']
rotate_params = ['prefab', 'axis', 'value']
scale_params = ['prefab', 'axis', 'value']
"""

axisList = ['x', 'y', 'z', 'default', 'all'] # default and all are the same | move, insert
directionsList = ["left", "right", "front", "back", "top", "bottom", "default"] #rotate, scale

@app.route("/set/insert", methods=["POST"])
def set_insert(): 
    """
    INSERT OBJECT
    ---
    parameters:
        - name: insert object
          in: "body"
          description: "insert object inside of Unity"
          required: true
          schema:
            type: "object"
            properties:
              reference_object: 
                type: "string"
                description: "reference object for placement of the new prefab"
              prefab:
                type: "string"
                description: "object that will be deployed in Unity"
              direction:
                type: "string"
                description: "direction which the object will be placed in Unity"
              value:
                type: "string"
                description: "distance of the prefab from the reference object"
    responses:
        200:
            description: Returns the output of the LLM
    """
     
    action = "insert"
    referenceObject = request.json.get("reference_object", "")
    prefab = request.json.get("prefab", "")
    direction = request.json.get("direction", "")
    value = request.json.get("value", "")

    insertObject = {
        "action": action,
        "parameters": {
            "reference_object": "",
            "prefab": "",
            "direction": "",
            "value": ""
        }
    }

    if len(prefab) > 0:
        insertObject['parameters']['reference_object'] = referenceObject

    if len(prefab) > 0:
        insertObject['parameters']['prefab'] = prefab
    
    if len(direction) > 0:
        insertObject['parameters']['direction'] = direction

    if len(value) > 0:
        insertObject['parameters']['value'] = value

    paramsWithoutValue = []
    for key, item in insertObject["parameters"].items():
        if len(item) == 0:
            paramsWithoutValue.append(key)

    if paramsWithoutValue:
        return jsonify(f"Parameter/s are required: {paramsWithoutValue}"), 400
    else:
        if direction.lower() not in directionsList:
            return jsonify(f"Direction is invalid. {directionsList}"), 400
        elif value.isdigit() == False:
            return jsonify(f"Value should be a number."), 400
        else: 
            currentInstruction['action'] = insertObject['action']
            currentInstruction['parameters'] = insertObject['parameters']
            return jsonify(insertObject), 200
    
@app.route("/set/move", methods=["POST"])
def set_move(): 
    """
    MOVE OBJECT
    ---
    parameters:
        - name: move object
          in: "body"
          description: "move object inside of Unity"
          required: true
          schema:
            type: "object"
            properties:
              prefab:
                type: "string"
                description: "target object"
              direction:
                type: "string"
                description: "direction where the object will be moved"
              value:
                type: "string"
                description: "distance value of the object placement"
    responses:
        200:
            description: Returns the output of the LLM
    """
     
    action = "move"
    prefab = request.json.get("prefab", "")
    direction = request.json.get("direction", "")
    value = request.json.get("value", "")

    moveObject = {
        "action": action,
        "parameters": {
            "prefab": "",
            "direction": "",
            "value": ""
        }
    }

    if len(prefab) > 0:
        moveObject['parameters']['prefab'] = prefab
    
    if len(direction) > 0:
        moveObject['parameters']['direction'] = direction

    if len(value) > 0:
        moveObject['parameters']['value'] = value

    paramsWithoutValue = []
    for key, item in moveObject["parameters"].items():
        if len(item) == 0:
            paramsWithoutValue.append(key)

    if paramsWithoutValue:
        return jsonify(f"Parameter/s are required: {paramsWithoutValue}"), 400
    else:
        if direction.lower() not in directionsList:
            return jsonify(f"Direction is invalid. {directionsList}"), 400
        elif value.isdigit() == False:
             return jsonify(f"Value should be a number."), 400
        else: 
            currentInstruction['action'] = moveObject['action']
            currentInstruction['parameters'] = moveObject['parameters']
            return jsonify(moveObject), 200

@app.route("/set/remove", methods=["POST"])
def set_remove(): 
    """
    REMOVE OBJECT
    ---
    parameters:
        - name: remove object
          in: "body"
          description: "remove object inside of Unity"
          required: true
          schema:
            type: "object"
            properties:
              prefab:
                type: "string"
                description: "target object"
              value:
                type: "string"
                description: "Number of object to be removed and targets the objects with the same prefab name"
    responses:
        200:
            description: Returns the output of the LLM
    """
     
    action = "remove"
    prefab = request.json.get("prefab", "")
    value = request.json.get("value", "")

    removeObject = {
        "action": action,
        "parameters": {
            "prefab": "",
            "value": ""
        }
    }

    if len(prefab) > 0:
        removeObject['parameters']['prefab'] = prefab

    if len(value) > 0:
        removeObject['parameters']['value'] = value

    paramsWithoutValue = []
    for key, item in removeObject["parameters"].items():
        if len(item) == 0:
            paramsWithoutValue.append(key)

    if paramsWithoutValue:
        return jsonify(f"Parameter/s are required: {paramsWithoutValue}"), 400
    else:
        if value.isdigit() == False:
             return jsonify(f"Value should be a number."), 400
        else: 
            currentInstruction['action'] = removeObject['action']
            currentInstruction['parameters'] = removeObject['parameters']
            return jsonify(removeObject), 200
    
@app.route("/set/replace", methods=["POST"])
def set_replace(): 
    """
    REPLACE OBJECT
    ---
    parameters:
        - name: replace object
          in: "body"
          description: "replace object inside of Unity"
          required: true
          schema:
            type: "object"
            properties:
              prefab:
                type: "string"
                description: "target object to be repalced"
              object_to_replace:
                type: "string"
                description: "object to insert"
    responses:
        200:
            description: Returns the output of the LLM
    """
     
    action = "replace"
    prefab = request.json.get("prefab", "")
    objectToReplace = request.json.get("object_to_replace", "")

    replaceObject = {
        "action": action,
        "parameters": {
            "prefab": "",
            "object_to_replace": ""
        }
    }

    if len(prefab) > 0:
        replaceObject['parameters']['prefab'] = prefab

    if len(objectToReplace) > 0:
        replaceObject['parameters']['object_to_replace'] = objectToReplace

    paramsWithoutValue = []
    for key, item in replaceObject["parameters"].items():
        if len(item) == 0:
            paramsWithoutValue.append(key)

    if paramsWithoutValue:
        return jsonify(f"Parameter/s are required: {paramsWithoutValue}"), 400
    else:
        currentInstruction['action'] = replaceObject['action']
        currentInstruction['parameters'] = replaceObject['parameters']
        return jsonify(replaceObject), 200

@app.route("/set/scale", methods=["POST"])
def set_scale(): 
    """
    SCALE OBJECT
    ---
    parameters:
        - name: scale instruction
          in: "body"
          description: "scale object"
          required: true
          schema:
            type: "object"
            properties:
              prefab:
                type: "string"
                description: "target object to be scaled"
              axis:
                type: "string"
                description: "axis where the object should be scaled"
              value:
                type: "string"
                description: "amount scaling for the object"
    responses:
        200:
            description: Returns the output of the LLM
    """

    action = "scale"
    prefab = request.json.get("prefab", "")
    axis = request.json.get("axis", "")
    value = request.json.get("value", "")

    scaleObject = {
        "action": action,
        "parameters": {
            "prefab": "",
            "axis": "",
            "value": ""
        }
    }

    if len(prefab) > 0:
        scaleObject['parameters']['prefab'] = prefab

    if len(axis) > 0:
        scaleObject['parameters']['axis'] = axis
    
    if len(value) > 0:
        scaleObject['parameters']['value'] = value

    paramsWithoutValue = []
    for key, item in scaleObject["parameters"].items():
        if len(item) == 0:
            paramsWithoutValue.append(key)

    if paramsWithoutValue:
        return jsonify(f"Parameter/s are required: {paramsWithoutValue}"), 400
    else:
        if axis.lower() not in axisList:
            return jsonify(f"Axis is invalid. {axisList}"), 400
        elif value.isdigit() == False:
             return jsonify(f"Value should be a number."), 400
        else: 
            currentInstruction['action'] = scaleObject['action']
            currentInstruction['parameters'] = scaleObject['parameters']
            return jsonify(scaleObject), 200

@app.route("/set/rotate", methods=["POST"])
def set_rotate(): 
    """
    ROTATE OBJECT
    ---
    parameters:
        - name: rotate instruction
          in: "body"
          description: "rotate object"
          required: true
          schema:
            type: "object"
            properties:
              prefab:
                type: "string"
                description: "target object to be rotated"
              axis:
                type: "string"
                description: "axis where the object should be rotated"
              value:
                type: "string"
                description: "degree of rotation"
    responses:
        200:
            description: Returns the output of the LLM
    """

    action = "rotate"
    prefab = request.json.get("prefab", "")
    axis = request.json.get("axis", "")
    value = request.json.get("value", "")

    rotateObject = {
        "action": action,
        "parameters": {
            "prefab": "",
            "axis": "",
            "value": ""
        }
    }

    if len(prefab) > 0:
        rotateObject['parameters']['prefab'] = prefab

    if len(axis) > 0:
        rotateObject['parameters']['axis'] = axis
    
    if len(value) > 0:
        rotateObject['parameters']['value'] = value

    paramsWithoutValue = []
    for key, item in rotateObject["parameters"].items():
        if len(item) == 0:
            paramsWithoutValue.append(key)

    if paramsWithoutValue:
        return jsonify(f"Parameter/s are required: {paramsWithoutValue}"), 400
    else:
        if axis.lower() not in axisList:
            return jsonify(f"Axis is invalid. {axisList}"), 400
        elif value.isdigit() == False:
             return jsonify(f"Value should be a number."), 400
        else: 
            currentInstruction['action'] = rotateObject['action']
            currentInstruction['parameters'] = rotateObject['parameters']
            return jsonify(rotateObject), 200

@app.route("/instruction")
def get_instruction():
    """
    Returns the instruction which access by Unity.
    ---
    responses:
        200:
            description: Returns the output of the LLM.
    """
    return jsonify(currentInstruction)

if __name__ == "__main__":
    app.run(debug=True, port=9001)
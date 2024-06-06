from flask import Flask, request, jsonify
import json

app = Flask(__name__)

currentInstruction = {
    "prompt": "",
    "action": "",
    "parameters": ""
}

errorResponse = {
    "message": ""
}

actions = ['insert', 'duplicate', 'delete', 'move', 'replace', 'rotate', 'scale']
insert_params = ['reference_object', 'prefab', 'direction', 'value']
duplicate_params = ['prefab', 'axis']
move_params = ['prefab', 'direction', 'value']
remove_params = ['prefab', 'value']
replace_params = ['prefab', 'object_to_replace']
rotate_params = ['prefab', 'axis', 'value']
scale_params = ['prefab', 'axis', 'value']

def validateParameters(parameterKeys, parameterValues):
    checkParameters = True
    missingParams = []
    for item in parameterValues:
        if item not in parameterKeys:
            missingParams.append(item)
            checkParameters = False
    return checkParameters, missingParams

@app.route("/set/instruction", methods=["POST"])
def set_instruction(): 
    action = request.json.get("action")
    prompt = request.json.get("prompt")
    parameters = request.json.get("parameters")
    parameterKeys = list(parameters.keys())

    isAction = True
    
    match action:
        case 'insert':
            checkParameters, missingParams = validateParameters(parameterKeys, insert_params)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}"
        case 'duplicate':
            checkParameters, missingParams = validateParameters(parameterKeys, duplicate_params)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}"
        case 'move':
            checkParameters, missingParams = validateParameters(parameterKeys, move_params)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}"
        case 'remove':
            checkParameters, missingParams = validateParameters(parameterKeys, remove_params)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}"
        case 'replace':
            checkParameters, missingParams = validateParameters(parameterKeys, replace_params)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}"
        case 'rotate':
            checkParameters, missingParams = validateParameters(parameterKeys, rotate_params)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}"
        case 'scale':
            checkParameters, missingParams = validateParameters(parameterKeys, missingParams)
            if(checkParameters == False):
                errorResponse['message'] = f"Incompatible parameters. {str(missingParams)}" 
        case _:
            isAction = False
            errorResponse['message'] = f"Action named '{action}' is not supported."

    if(isAction and checkParameters):
        if(prompt == None or action == None or parameters == None):
            errorResponse['message'] = "Incomplete variables."
            return jsonify(errorResponse)
        else:
            currentInstruction["prompt"] = prompt
            currentInstruction["action"] = action
            currentInstruction["parameters"] = parameters
            return jsonify(currentInstruction)
    else:
        return jsonify(errorResponse)

@app.route("/get/instruction")
def get_instruction():
    return jsonify(currentInstruction)

if __name__ == "__main__":
    app.run(debug=True, port=9001)
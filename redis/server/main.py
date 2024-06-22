from fastapi import FastAPI, HTTPException, Body, Request
from pydantic import BaseModel
from redis import Redis
from rq import Queue
import uuid 
import json

app = FastAPI()

# create redis queue
redis_conn = Redis(host='redis', port=6379)
task_queue = Queue("task_queue", connection=redis_conn, db=0)

class SpawnObject(BaseModel):
    reference_object: str
    prefab: str
    direction: str
    value: str

class SnapObject(BaseModel):
    snap_point: str
    prefab: str

class MoveObject(BaseModel):
    prefab: str
    direction: str
    value: str

class RemoveObject(BaseModel):
    prefab: str
    value: str

class ReplaceObject(BaseModel):
    prefab: str
    object_to_replace: str

class ScaleObject(BaseModel):
    prefab: str
    axis: str
    value: str

class RotateObject(BaseModel):
    prefab: str
    axis: str
    value: str

class UnityResponseObject(BaseModel):
    message: str
    current_object: str
    available_prefabs: str

currentInstruction = {
    "action": "",
    "parameters": ""
}

responseFromUnity = {"response": ""}

axisList = ['x', 'y', 'z', 'reset', 'default']
scaleList = ['x_up', 'y_up', 'z_up', 'x_down', 'y_down', 'z_down', 'multiply', 'increase', 'decrease', 'reset', 'default']
directionsList = ["left", "right", "front", "back", "top", "bottom", "default"]

@app.post("/set/spawn")
async def set_spawn(spawn_obj: SpawnObject):
    spawn_params = dict(spawn_obj)
    print(type(spawn_obj))
    if spawn_params['direction'].lower() not in directionsList:
        raise HTTPException(status_code=400, detail=f"Direction is invalid. {directionsList}")
    elif not spawn_params['value'].isdigit():
        raise HTTPException(status_code=400, detail="Value should be a number.")
    else:
        currentInstruction['action'] = "spawn"
        currentInstruction['parameters'] = spawn_params
    
        try:
            redis_conn.rpush('instruction', json.dumps(currentInstruction))
            return {
                "success": True,
                "message": "Pushed to Redis Queue",
                "payload": currentInstruction
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

@app.post("/set/snap")
async def set_snap(snap_obj: SnapObject):
    snap_params = dict(snap_obj)
    currentInstruction['action'] = "snap"
    currentInstruction['parameters'] = snap_params

    try:
        redis_conn.rpush('instruction', json.dumps(currentInstruction))
        return {
            "success": True,
            "message": "Pushed to Redis Queue",
            "payload": currentInstruction
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@app.post("/set/move")
async def set_move(move_obj: MoveObject):
    move_params = dict(move_obj)
    if move_params['direction'].lower() not in directionsList:
        raise HTTPException(status_code=400, detail=f"Direction is invalid. {directionsList}")
    elif not move_params['value'].isdigit():
        raise HTTPException(status_code=400, detail="Value should be a number.")
    else:
        currentInstruction['action'] = "move"
        currentInstruction['parameters'] = move_params
        
        try:
            redis_conn.rpush('instruction', json.dumps(currentInstruction))
            return {
                "success": True,
                "message": "Pushed to Redis Queue",
                "payload": currentInstruction
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
@app.post("/set/remove")
async def set_remove(remove_obj: RemoveObject):
    remove_params = dict(remove_obj)
    if not remove_params['value'].isdigit():
        raise HTTPException(status_code=400, detail="Value should be a number.")
    else:
        currentInstruction['action'] = "remove"
        currentInstruction['parameters'] = remove_params
        
        try:
            redis_conn.rpush('instruction', json.dumps(currentInstruction))
            return {
                "success": True,
                "message": "Pushed to Redis Queue",
                "payload": currentInstruction
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

@app.post("/set/replace")
async def set_replace(replace_obj: ReplaceObject):
    replace_params = dict(replace_obj)
    currentInstruction['action'] = "replace"
    currentInstruction['parameters'] = replace_params
    
    try:
        redis_conn.rpush('instruction', json.dumps(currentInstruction))
        return {
            "success": True,
            "message": "Pushed to Redis Queue",
            "payload": currentInstruction
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@app.post("/set/scale")
async def set_scale(scale_obj: ScaleObject):
    scale_params = dict(scale_obj)
    if scale_params['axis'].lower() not in scaleList:
        raise HTTPException(status_code=400, detail=f"Axis is invalid. {scaleList}")
    elif not scale_params['value'].isdigit():
        raise HTTPException(status_code=400, detail="Value should be a number.")
    else:
        currentInstruction['action'] = "scale"
        currentInstruction['parameters'] = scale_params
        
        try:
            redis_conn.rpush('instruction', json.dumps(currentInstruction))
            return {
                "success": True,
                "message": "Pushed to Redis Queue",
                "payload": currentInstruction
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

@app.post("/set/rotate")
async def set_rotate(rotate_obj: RotateObject):
    rotate_params = dict(rotate_obj)
    if rotate_params['axis'].lower() not in axisList:
        raise HTTPException(status_code=400, detail=f"Axis is invalid. {axisList}")
    elif not rotate_params['value'].isdigit():
        raise HTTPException(status_code=400, detail="Value should be a number.")
    else:
        currentInstruction['action'] = "rotate"
        currentInstruction['parameters'] = rotate_params
        
        try:
            redis_conn.rpush('instruction', json.dumps(currentInstruction))
            return {
                "success": True,
                "message": "Pushed to Redis Queue",
                "payload": currentInstruction
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

@app.post("/set/response")
async def set_response(reponse_obj: UnityResponseObject):
    reponse_params = dict(reponse_obj)
    responseFromUnity['response'] = reponse_params
    return responseFromUnity

@app.get("/response")
async def get_response():
    return responseFromUnity

@app.get("/instruction")
async def get_instruction():
    try:
        return json.loads(redis_conn.lpop("instruction"))
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
   

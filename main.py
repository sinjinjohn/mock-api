from fastapi import FastAPI, HTTPException
app = FastAPI(title="Mock Device API Server")

MOCK_DEVICES = {
    "device001": {
        "battery_charged": True,
        "sim_type": "one-lap",
        "sim_active": True,
        "has_sent_location_ever": True,
        "has_valid_expiry":True
    },
    "device002": {
        "battery_charged": False,
        "sim_type": "personal",
        "sim_active": False,
        "has_sent_location_ever": False,
        "has_valid_expiry": False
    },
    "device003": {
        "battery_charged": True,
        "sim_type": "personal",
        "sim_active": True,
        "has_sent_location_ever": False,
        "has_valid_expiry": True
    }
}


def get_device(device_id: str):
    if device_id not in MOCK_DEVICES:
        raise HTTPException(status_code=404, detail="Device not found")
    return MOCK_DEVICES[device_id]


@app.get("/device/{device_id}/battery")
def batter_status(device_id:str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "battery_charged": device["battery_charged"]
        }



@app.get("/device/{device_id}/sim_type")
def sim_type(device_id:str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "sim_type": device["sim_type"]
        }


@app.get("/device/{device_id}/sim_active")
def sim_type(device_id:str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "sim_active": device["sim_active"]
        }

@app.get("/device/{device_id}/location-status")
def location_status(device_id: str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "has_sent_location_ever": device["has_sent_location_ever"]
    }



@app.get("/device/{device_id}/expiry-status")
def location_status(device_id: str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "has_valid_expiry": device["has_valid_expiry"]
    }
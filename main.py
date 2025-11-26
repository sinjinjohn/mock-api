from fastapi import FastAPI, HTTPException
app = FastAPI(title="Mock Device API Server")

MOCK_DEVICES = {
    "device001": {
        "battery_charged": True,
        "sim_type": "one-lap",
        "sim_active": True,
        "has_sent_location_ever": True,
        "has_valid_expiry":True,
        "imei": "356938035643809",
        "ip": "192.168.1.1",
        "port":"5023",
        "serial_number_webOnelap":"SN123456789",
        "serial_number_ecom":"SN123456789"
    },
    "device002": {
        "battery_charged": False,
        "sim_type": "personal",
        "sim_active": False,
        "has_sent_location_ever": False,
        "has_valid_expiry": False,
        "imei": "356938035643810",
        "ip": "192.168.1.1",
        "port":"5023",
        "serial_number_webOnelap":"SN123456789",
        "serial_number_ecom":"SN123456789"
    },
    "device003": {
        "battery_charged": True,
        "sim_type": "personal",
        "sim_active": True,
        "has_sent_location_ever": False,
        "has_valid_expiry": True,
        "imei": "356938035643811",
        "ip": "192.168.1.1",
        "port":"5023",
        "serial_number_webOnelap":"SN123456789",
        "serial_number_ecom":"SN123456789"
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


@app.get("/device/{device_id}/server-parameters")
def get_server_parameters(device_id: str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "imei": device["imei"],
        "ip": device["ip"],
        "port": device["port"]
    }


@app.post("/device/{device_id}/close-ticket")
def close_ticket(device_id: str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "status": "Ticket closed successfully"
    }


@app.get("/device/{device_id}/serial-number-exists")
def serialNumberExists_webonelap(device_id: str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "serial_number_exists_webonelap": True if "serial_number_webOnelap" in device else False
    }

@app.get("/device/{device_id}/serial-number-ecom-exists")
def serial_number_exists_ecom(device_id: str):
    device = get_device(device_id)
    return {
        "device_id": device_id,
        "serial_number_exists_ecom": True if "serial_number_ecom" in device else False
    }

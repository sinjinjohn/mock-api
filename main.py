from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase_client import supabase

from typing import Optional

app = FastAPI(title="Mock Device API Server")



class DeviceUpdate(BaseModel):
    battery_charged: Optional[bool] = None
    sim_type: Optional[str] = None
    sim_active: Optional[bool] = None
    has_sent_location_ever: Optional[bool] = None
    has_valid_expiry: Optional[bool] = None
    imei: Optional[str] = None
    ip: Optional[str] = None
    port: Optional[str] = None
    serial_number_webOnelap: Optional[str] = None
    serial_number_ecom: Optional[str] = None

# MOCK_DEVICES = {
#     "device001": {
#         "battery_charged": True,
#         "sim_type": "one-lap",
#         "sim_active": True,
#         "has_sent_location_ever": True,
#         "has_valid_expiry":True,
#         "imei": "356938035643809",
#         "ip": "192.168.1.1",
#         "port":"5023",
#         "serial_number_webOnelap":"SN123456789",
#         "serial_number_ecom":"SN123456789"
#     },
#     "device002": {
#         "battery_charged": False,
#         "sim_type": "personal",
#         "sim_active": False,
#         "has_sent_location_ever": False,
#         "has_valid_expiry": False,
#         "imei": "356938035643810",
#         "ip": "192.168.1.1",
#         "port":"5023",
#         "serial_number_webOnelap":"SN123456789",
#         "serial_number_ecom":"SN123456789"
#     },
#     "device003": {
#         "battery_charged": True,
#         "sim_type": "personal",
#         "sim_active": True,
#         "has_sent_location_ever": False,
#         "has_valid_expiry": True,
#         "imei": "356938035643811",
#         "ip": "192.168.1.1",
#         "port":"5023",
#         "serial_number_webOnelap":"SN123456789",
#         "serial_number_ecom":"SN123456789"
#     }
# }


def get_device(device_id: str):
    response = supabase.table("devices").select("*").eq("device_id", device_id).single().execute()

    if response.data is None:
        raise HTTPException(status_code=404, detail="Device not found")

    return response.data


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
def sim_type_active(device_id:str):
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


# post request for all above endpoints

@app.post("/device/{device_id}/update-data")
def update_device(device_id: str, payload: DeviceUpdate):
    get_device(device_id)

    update_data = payload.model_dump(exclude_none=True)

    if not update_data:
        raise HTTPException(400, "No valid fields to update")

    supabase.table("devices").update(update_data).eq("device_id", device_id).execute()

    return {
        "device_id": device_id,
        "updated_fields": update_data,
        "status": "success"
    }



#Api to send new vodafone sim
@app.post("/device/{device_id}/send-vodafone-sim")
def send_vodafone_sim(device_id: str):
    return {
        "device_id": device_id,
        "status": "Vodafone SIM sent successfully"
    }

#Api to send new aitel sim
@app.post("/device/{device_id}/send-airtel-sim")
def send_airtel_sim(device_id: str):
    return {
        "device_id": device_id,
        "status": "Airtel SIM sent successfully"
    }
#Api to update apn with respect to the new sim
@app.post("/device/{device_id}/update-apn")
def update_apn(device_id: str):
    return {
        "device_id": device_id,
        "status": "APN updated successfully"
    }

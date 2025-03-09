from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
import pyodbc
import uvicorn

app = FastAPI()

# Fix CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Fix incorrect attribute name
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Database Connection String (Update for your environment)
connection_string = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=LAPTOP-BCPV2OBE;"
    r"DATABASE=practice;"
    r"TRUSTED_CONNECTION=yes"
)

def get_db_connection():
    return pyodbc.connect(connection_string)

@app.post("/energy-usage")
def submit_energy_usage(
    user_type: str = Form(...),
    location: str = Form(...),
    building_size: float = Form(...),
    occupants: int = Form(...),
    heating_system: str = Form(...),
    cooling_system: str = Form(...),
    high_power_devices: int = Form(...),
    num_fans: int = Form(...),
    num_lights: int = Form(...),
    usage_hours: str = Form(...),
    energy_source: str = Form(...)
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO energy_usage (user_type, location, building_size, occupants, heating_system,
                                      cooling_system, high_power_devices, num_fans, num_lights, usage_hours, energy_source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_type, location, building_size, occupants, heating_system, cooling_system,
              high_power_devices, num_fans, num_lights, usage_hours, energy_source))

        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Energy usage data submitted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

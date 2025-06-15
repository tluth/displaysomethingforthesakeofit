import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_humidity import BrickletHumidity
from tinkerforge.bricklet_temperature import BrickletTemperature
from tinkerforge.bricklet_co2 import BrickletCO2


def get_humidity_temperature_readings(
        host: str, port: int, humidity_uid: str, temp_uid: str, co2_uid: str
) -> dict:
    """Fetch Humidity and Temperature readings and display them on the LCD."""
    ipcon = IPConnection()
    humidity = BrickletHumidity(humidity_uid, ipcon)
    temperature = BrickletTemperature(temp_uid, ipcon)
    co2 = BrickletCO2(co2_uid, ipcon)

    try:
        ipcon.connect(host, port)

        humidity_value = humidity.get_humidity() / 10.0
        temperature_value = temperature.get_temperature() / 100.0
        co2_value = co2.get_co2_concentration()
        print("Connected to Masterbrick...")

        return {
            "temperature": temperature_value,
            "humidity": humidity_value,
            "co2": co2_value
        }

    except Exception:
        print("Error reading sensors")

    finally:
        ipcon.disconnect()
        print("Disconnected.")

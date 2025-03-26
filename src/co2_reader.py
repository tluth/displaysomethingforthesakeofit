import time
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2 import BrickletCO2


def get_co2_readings(host: str, port: int, uid: str) -> None:
    """ Continuously fetch CO2 readings from the CO2 Bricklet every second. """
    ipcon = IPConnection()
    co2 = BrickletCO2(uid, ipcon)

    try:
        ipcon.connect(host, port)
        print("Connected to Masterbrick. Fetching CO2 readings...")

        while True:
            co2_concentration = co2.get_co2_concentration()
            print(f"CO2 Concentration: {co2_concentration} ppm")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping CO2 readings.")
    finally:
        ipcon.disconnect()
        print("Disconnected.")


if __name__ == "__main__":
    MASTERBRICK_HOST = "localhost"
    MASTERBRICK_PORT = 4223
    CO2_BRICKLET_UID = "YOUR_UID"

    get_co2_readings(MASTERBRICK_HOST, MASTERBRICK_PORT, CO2_BRICKLET_UID)

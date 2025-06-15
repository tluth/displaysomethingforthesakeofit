import time

from sensors import get_humidity_temperature_readings
from display import lcd_init

MASTERBRICK_HOST = "192.168.1.9"
MASTERBRICK_PORT = 4223
HUMIDITY_UID = "C1g"
TEMP_UID = "zEG"
CO2_UID = "Gtr"


def main() -> None:
    try:
        lcd = lcd_init()

        while True:
            sensor_data = get_humidity_temperature_readings(
                MASTERBRICK_HOST, MASTERBRICK_PORT, HUMIDITY_UID, TEMP_UID, CO2_UID
            )
            # Format display text
            temp_text = f"{sensor_data['temperature']:.1f}C | "
            hum_text = f"{sensor_data['humidity']:.1f}% hum"
            co2_text = f"CO2: {sensor_data['co2']} ppm"

            # Print to LCD
            lcd.cursor_pos = (0, 0)
            lcd.write_string(temp_text)
            lcd.cursor_pos = (0, 8)
            lcd.write_string(hum_text)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(co2_text)
            time.sleep(2)  # Update every 2 seconds

    except KeyboardInterrupt:
        print("Stopping readings and clearing LCD.")
        time.sleep(2)
        lcd.clear()

    finally:
        lcd.clear()
        exit()
        print("Disconnected.")


if __name__ == "__main__":
    main()

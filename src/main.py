import time

from sensors import get_humidity_temperature_readings
from display import lcd_init

MASTERBRICK_HOST = "192.168.1.2"
MASTERBRICK_PORT = 4223
HUMIDITY_UID = "C1g"
TEMP_UID = "zEG"

def main() -> None:

    try:
        print("Connected to Masterbrick. Displaying readings on LCD...")
        lcd = lcd_init()
        
        while True:
            sensor_data = get_humidity_temperature_readings(MASTERBRICK_HOST, MASTERBRICK_PORT, HUMIDITY_UID, TEMP_UID)

            # Format display text
            temp_text = f"Temp: {sensor_data["temperature"]:.1f}C"
            hum_text = f"Hum: {sensor_data["humidity"]:.1f}%"

            # Print to LCD
            lcd.cursor_pos = (0, 0)
            lcd.write_string(temp_text)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(hum_text)
            time.sleep(2)  # Update every 2 seconds

    except KeyboardInterrupt:
        print("Stopping readings and clearing LCD.")
        time.sleep(2)
        lcd.clear()
    
    finally:
        lcd.clear()
        exit()
        print("Disconnected.")
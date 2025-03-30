from RPLCD.i2c import CharLCD

LCD_ADDRESS = 0x27
I2C_BUS = 1
I2C_EXPANDER = "PCF8574"
LCD_CHR = 1
CHAR_MAP = "A00"

def lcd_init():
    return CharLCD(
        i2c_expander=I2C_EXPANDER, 
        address=LCD_ADDRESS, 
        port=I2C_BUS,
        cols=16, 
        rows=2, 
        charmap=CHAR_MAP, 
        auto_linebreaks=True
    )


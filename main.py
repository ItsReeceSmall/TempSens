import os
import glob
import time
from lib.lcd1602 import LCD1602
import lib.temp

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

temp.read_temp_raw()
temp.read_temp()
##############################################	
lcd = LCD1602()                                           # calls class from file
try:
    while True:
        c, f = read_temp()                                # Reads Temp
        temp = str(int(c))                                # sets the Celcius value to the variable temp
        msg = temp + ' degrees C'                         # sets the variable msg as a set string consisting of the temp + string
        lcd.lcd_string("Temperature is",lcd.LCD_LINE_1)   # Prints this to the top line of the LCD
        lcd.lcd_string(msg, lcd.LCD_LINE_2)               # Prints msg to the bottom line of LCD
        time.sleep(1)                                     # pause of 1 second

except KeyboardInterrupt:
    lcd.lcd_string("Closing ...", lcd.LCD_LINE_1)         # Registers request to close and prints closing
    lcd.lcd_string("", lcd.LCD_LINE_2)                    # clears line 2
    time.sleep(3)                                         # 3 second pause

finally:
    lcd.lcd_clear()                                       # runs method from class

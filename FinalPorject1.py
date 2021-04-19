import grovepi
from grove_rgb_lcd import *
import time
import math
import sqlite3
import random

# Connect the Grove Temperature & Humidity Sensor Pro to digital port 6.
sensor = 6  

# temp_humidity_sensor_type
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

# Create conncetion and table SQLite
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS weather (
            temperature real,
            humidity real,
            time integer
    )
    """)

# temperature, humidity = 27, 69
while True:
    try:
        Reads temp and humidity from dht module
        [temperature,humidity] = grovepi.dht(sensor,blue)
        # temperature += random.random() - 0.5
        # humidity += random.random() - 0.5
        temp =(temperature * 1.8) + 32
        # If grovepi is not ready to be polled it will return nan, so check for that to ignore
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            # Saves temperature, humidity and time into sqlite datatable.
            c.execute("INSERT INTO weather (temperature, humidity, time) values (?, ?, ?)", (temp, humidity, int(time.time())))
            conn.commit()
      
                
    except (IOError, TypeError) as e:
        print(str(e))        

    except KeyboardInterrupt as e:
        print(str(e))        


    
    time.sleep(1)

conn.close()
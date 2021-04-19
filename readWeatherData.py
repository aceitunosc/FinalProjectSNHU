import math
import sqlite3
import time

lookback = 24 * 86400
startTime = int(time.time()) - lookback


conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('SELECT temperature, humidity, time FROM weather WHERE time > ? ORDER BY time', (startTime,))
rows = c.fetchall()
# print(rows)

temps = [r[0] for r in rows]
hums = [r[1] for r in rows]


def mean(data):
    n = len(data)
    mean = sum(data) / n
    return mean

def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

def min(data):
    mn = math.inf 
    for n in data: 
        if n < mn:
            mn = n
    return mn 
def max(data):
    mx = -math.inf 
    for n in data:
        if n > mx:
            mx = n
    return mx

print()
print("Current Temperature: %5.1f   Min: %5.1f   Max: %5.1f   Avg: %5.1f   StdDev: %5.2f" % (rows[-1][0], min(temps), max(temps), mean(temps), stdev(temps)))
print("Current Humidity:    %5.1f   Min: %5.1f   Max: %5.1f   Avg: %5.1f   StdDev: %5.2f" % (rows[-1][1], min(hums), max(hums), mean(hums), stdev(hums)))

# print("Standard Deviation of the sample is %s "% (stdev(data)))
# print("Mean of the sample is %s " % (mean(data)))
# print()


# <count> data points collected since <startTime, or time of earliest data point>
# <some number> most recent data points:
# ...
# ...

# average, stddev, max, min (temp and humidity)
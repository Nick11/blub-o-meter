import LSM6DS3
import time
import array

def tuple_16_to_array(tup):
    return array.array('h', tup)

sensor = LSM6DS3.LSM6DS3()
with open('rawdata-' + time.strftime('%Y%m%d%H%M%S'), 'wb') as f:
    for val in sensor.accelvalues():
        tuple_16_to_array(val).tofile(f)

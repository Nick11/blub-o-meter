import sys
import time
import math

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.I2C as I2C

address = 0x6b

class LSM6DS3:
    i2c = None
    tempvar = 0
    global accel_center_x
    accel_center_x = 0
    global accel_center_y
    accel_center_y = 0
    global accel_center_z
    accel_center_z = 0


    def __init__(self, address=0x6b, debug=0, pause=0.8):
        self.i2c = I2C.get_i2c_device(address)
        self.address = address
        dataToWrite = 0 #Start Fresh!
        dataToWrite |= 0x03 # set at 50hz, bandwidth
        dataToWrite |= 0x00  # 2g accel range
        dataToWrite |= 0x40 # 13hz ODR
        self.i2c.write8(0X10, dataToWrite) #writeRegister(LSM6DS3_ACC_GYRO_CTRL2_G, dataToWrite);

        accel_center_x = self.i2c.readS16(0X28)
        accel_center_y = self.i2c.readS16(0x2A)
        accel_center_z = self.i2c.readS16(0x2C)

    def accelvalues(self):
        while True:
            yield self.readRawAccel()
            time.sleep(0.01)

    def readRawAccel(self):
        return (self.readRawAccelX(), self.readRawAccelY(), self.readRawAccelZ())

    def readRawAccelX(self):
        output = self.i2c.readS16(0X28)
        return output;

    def readRawAccelY(self):
        output = self.i2c.readS16(0x2A)
        return output;

    def readRawAccelZ(self):
        output = self.i2c.readS16(0x2C)
        return output;

    def readRawGyroX(self):
        output = self.i2c.readS16(0X22)
        return output;

    def readFloatGyroX(self):
        output = self.calcGyro(self.readRawGyroX())
        return output;

    def calcGyroXAngle(self):
        temp = 0
        temp += self.readFloatGyroX()
        if (temp > 3 or temp < 0):
            self.tempvar += temp
        return self.tempvar;

    def calcGyro(self, rawInput):
        gyroRangeDivisor = 245 / 125; #500 is the gyro range (DPS)
        output = rawInput * 4.375 * (gyroRangeDivisor) / 1000;
        return output;



if __name__=='__main__':
    sensor = LSM6DS3()
    while True:
        print(sensor.readRawAccelX(), ',', sensor.readRawAccelY(), ',', sensor.readRawAccelZ(), ',', time.time())
        time.sleep(0.01)

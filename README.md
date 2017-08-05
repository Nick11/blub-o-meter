# Blub-o-Meter
The objective of the blub-o-meter is to measure fermentation intensity on a fermentation lock by counting the number of bubbles.
Reads from a LSM6DS3 accelerometer and converts it to bubbles/time and finally sends this imformation to a server.

## Hardware used
- Raspberry Pi 3 (any version is fine)
- LSM 6DS3 accelerometer

## Installation

## Prepare Raspberry Pi
- configure i2c interface [see instructions by adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
  - `sudo apt-get install -y python-smbus i2c-tools`
  - `sudo raspi-config` then Advanced Options->I2C->Yes
  - test I2C using `sudo i2cdetect -y 1`(or `sudo i2cdetect -y 0` on a 256MB Raspberry Pi Model B)

## Dependencies
- Adafruit Python GPIO Library [see instructions on github](https://github.com/adafruit/Adafruit_Python_GPIO) 
  -`sudo apt-get update`
  -`sudo apt-get install build-essential python-pip python-dev python-smbus git`
  -`cd externals`
  -`git clone https://github.com/adafruit/Adafruit_Python_GPIO.git`
  -`cd Adafruit_Python_GPIO`
  -`sudo python setup.py install`


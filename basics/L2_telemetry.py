import board
import digitalio
import netifaces as ni
from time import sleep
from threading import Thread
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from adafruit_ina219 import INA219
import subprocess
import L1_oled as display
import L1_ina as botData
import L1_log as nodeWrite


while(1):
    botVolt = botData.readVolts()
    nodeWrite.tmpFile(botVolt, "Voltage")
    sleep(1)




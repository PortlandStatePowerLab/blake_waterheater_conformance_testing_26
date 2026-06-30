from datetime import datetime
from numpy.random import normal
from numpy import zeros, savetxt, loadtxt
import random
import RPi.GPIO as GPIO
from time import time, sleep
from threading import Thread
import os
import csv

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FMPIN = 6    # flow meter GPIO pin
VPIN = 17    # valve GPIO pin
GPIO.setup(FMPIN, GPIO.IN, GPIO.PUD_UP) # setup flow meter pin as input
GPIO.setup(VPIN, GPIO.OUT, initial=GPIO.LOW)    # setup valve pin as output
GPIO.add_event_detect(FMPIN, GPIO.RISING)   # add rising edge detection

# Define function to draw water
def draw_water(targetVol):
    if targetVol <= 0:
        return()

    print('Drawing %.2f gallon(s).' % targetVol)
    start_time = time()
    print('Start time:', datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"))
    volume = 0
    numPulses = 0
    GPIO.output(VPIN, GPIO.HIGH)    # open valve
    while volume < targetVol:  # keep valve open until the desired volume has passed
        if GPIO.event_detected(FMPIN):
            numPulses += 1    # Count pulses from flow meter
            volume = float(numPulses) / 476    # Calculate volume
        # Check if drawing time exceeds 2 minutes
        if time() - start_time > 100:
            print("Drawing time exceeded 2 minutes. Stopping the program.")
            GPIO.output(VPIN, GPIO.LOW) # close valve
            exit()  # Terminate the program

    stop_time = time()
    GPIO.output(VPIN, GPIO.LOW) # close valve
    print('Volume drawn: %.2f gallon(s).' % volume)
    print('Stop time:', datetime.fromtimestamp(stop_time).strftime("%Y-%m-%d %H:%M:%S"))
    print('Count of pulses:', numPulses)

thread_draw = Thread(target=draw_water, args=[0])
times = []
volumes = []

file = open('24H_WDP.csv')
read = csv.reader(file)
for row in read:
    times.append(row[0])
    volumes.append(row[1])
file.close()

#print('Starting 24 Hour Scheduled Draw.  ' + str(datetime.now()))
print('Starting 24 Hours Scheduled Draw.  ' + str(datetime.now()))
print('\nWaiting for draw...')

# Enter main program loop
while True:
    now = datetime.now()    # Update date/time
    filename = 'WH_Data_' + str(now.month) + '-' + str(now.day) + '-' + str(now.year) + '.csv'
    if not os.path.isfile(filename): # Check if a new day has begun
        data = open(filename, 'w')
        data.write('Time,Draw Amount\n')
        data.close

    # Draw water if there is an event at this minute
    timestr = datetime.strftime(now, "%H:%M:%S")
    drawVolume = 0
    for i in range(0, len(times)):
        if times[i] == timestr:
            drawVolume = volumes[i]
    
    if drawVolume != 0:
        if thread_draw.is_alive() == True:
            print('Debugging: Previous draw is still running. Waiting for draw to finish.\n')
            thread_draw.join()

        thread_draw = Thread(target=draw_water, args=[float(drawVolume)])
        thread_draw.start()

        data = open(filename, 'a')
        data.write(timestr + ',' + str(drawVolume) + '\n')
        data.close

    sleep(1)

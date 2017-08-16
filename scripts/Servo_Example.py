#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import numpy as np
import math
# ===========================================================================
############################### Mover Motores ###############################
# ===========================================================================

def POS(grados,n):
  pulso =grados*400/180
  pulso = pulso+100
  print("done", pulso)
  pwm.setPWM(n-1, 0, pulso)
  
def CIN(pos):
  px2 = pow(pos[0],2)
  py2 = pow(pos[1],2)
  a2 = 10
  a3 = 17.5
  D = (px2+py2-pow(a2,2)-pow(a3,2))/(2*a2*a3)
  q3r = math.atan2(math.sqrt(1-pow(D,2)),D)
  q3 = round(math.degrees(q3r))
  betta = math.atan(pos[1]/pos[0])
  alfa = math.atan((a3*math.sin(q3r))/(a2+a3*math.cos(q3r)))
  q1r = betta - alfa
  q1 = round(math.degrees(q1r))
  if (q1 < 0):
    q1 = 180+q1
  # EXISTE UN CAMNIO DE Q2 A Q1, SOLO CAMBIA EL NOMBRE DE LA VARIABLE
  q2r = math.atan(pos[2]/pos[1])
  q2 = round(math.degrees(q2r))
  #if (pos[3] == 1 )
  print(q1,q2,q3)
# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 10  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
cont = 0
while (True):
  # Change speed of continuous servo on channel O
  print("grados")
  grados = input()
  POS(grados,1)
  time.sleep(1)
  cont = cont+1





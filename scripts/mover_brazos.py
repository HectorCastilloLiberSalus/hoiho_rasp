#!/usr/bin/env python


import rospy
from std_msgs.msg import Float32
from beginner_tutorials.msg import num 
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
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    #POS(data.data,1)
    CIN(data.data)
def CIN(pos):
  X = pos[0]+.1
  Y = pos[1]+.1
  Z = pos[2]+.1
  px2 = pow(X,2)
  py2 = pow(Y,2)
  a2 = 10
  a3 = 17.5
  D = (px2+py2-pow(a2,2)-pow(a3,2))/(2*a2*a3)
  print(D)
  q3r = math.atan2(math.sqrt(1-pow(D,2)),D)
  q3 = round(math.degrees(q3r))
  betta = math.atan(Y/X)
  alfa = math.atan((a3*math.sin(q3r))/(a2+(a3*math.cos(q3r))))
  q1r = betta - alfa
  q1 = round(math.degrees(q1r))
  if (q1 < 0):
    q1 = -q1
  # EXISTE UN CAMBIO DE Q2 A Q1, SOLO CAMBIA EL NOMBRE DE LA VARIABLE
  if (Z>0.2):
    q2r = math.atan(Z/Y)
    q2 = round(math.degrees(q2r))
  else:
    q2 = 0
  print(q1,q2,q3)
  q2 = 180-q2
  if (pos[4] == 1 ):
    q5 = 50
  else:
    q5 = 0
  q1 = 180-q1
  POS(int(q1),1)
  time.sleep(0.3)
  POS(int(q2),2)
  time.sleep(0.3)
  POS(int(q3),3)
  time.sleep(0.3)
  POS(int(pos[3]),4)
  time.sleep(0.3)
  POS(int(q5),5)
  time.sleep(0.3)
  
def listener():
    rospy.init_node('mover_brazos', anonymous=True)
    rospy.Subscriber('derecho', num, callback)
    rospy.spin()

pwm = PWM(0x40)

servoMin = 10  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
cont = 0

if __name__ == '__main__':
    listener()

#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from beginner_tutorials.msg import num 
from Adafruit_PWM_Servo_Driver import PWM
import time
import numpy as np
import math
# ===========================================================================
############################### Mover Motores ###############################
# ===========================================================================
global t1, t2, t4, t5, t6, t7, t8, t9, t10, t11, t12

t1 = 90
t2 = 180
t3 = 150
t4 = 90
t5 = 0
t6 = 90
t7 = 0
t8 = 20
t9 = 90
t10 = 0
t11 = 90
t12 = 50

def POS(grados,n):
  pulso =grados*400/180
  pulso = pulso+100
  #####print("done", pulso)
  pwm.setPWM(n-1, 0, pulso)
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    CIN(data.data)
def callbackderecho(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard derecho %s', data.data)
    CIND(data.data)
def callbackrot(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard cabeza 1 %s', data.data)
    CINR(data.data)
def callbackrot2(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard cabeza 2 %s', data.data)
    CINR2(data.data)

def CINR(pos):
  global t11
  x11 = int(pos[0])
  if (x11>t11):
    for x11 in range(t11,x11):
      POS(x11,11)
      time.sleep(0.05)
  else:
    for x11 in range(t11,x11,-1):
      POS(x11,11)
      time.sleep(0.05)
  t11 = x11


def CINR2(pos):
  global t12
  x12 = int(pos[0])
  if (x12>t12):
    for x12 in range(t12,x12):
      POS(x12,12)
      time.sleep(0.05)
  else:
    for x12 in range(t12,x12,-1):
      POS(x12,12)
      time.sleep(0.05)
  t12 = x12  






def CIN(pos):
  global t1, t2, t3, t4, t5
  ####################Gripper#################
  if (pos[4] == 1 ):
    q5 = 80
  else:
    q5 = 0
  ############################################  
  x1 = int(pos[0])
  x2 = int(pos[1])
  x3 = int(pos[2])
  x4 = int(pos[3])
  x5 = int(pos[4])
  #################### Motor 1################
  if (x1>t1):
    for x1 in range(t1,x1):
      POS(x1,1)
      time.sleep(0.015)
  else:
    for x1 in range(t1,x1,-1):
      POS(x1,1)
      time.sleep(0.015)
  t1 = x1
  ################## Motor 2##################
  if (x2>t2):
    for x2 in range(t2,x2):
      POS(x2,2)
      time.sleep(0.015)
  else:
    for x2 in range(t2,x2,-1):
      POS(x2,2)
      time.sleep(0.015)
  t2 = x2
  ################## Motor 3##################
  if (x3>t3):
    for x3 in range(t3,x3):
      POS(x3,3)
      time.sleep(0.015)
  else:
    for x3 in range(t3,x3,-1):
      POS(x3,3)
      time.sleep(0.015)
  t3 = x3
  ################## Motor 4##################
  if (x4>t4):
    for x4 in range(t4,x4):
      POS(x4,4)
      time.sleep(0.015)
  else:
    for x4 in range(t4,x4,-1):
      POS(x4,4)
      time.sleep(0.015)
  t4 = x4
  ################## Motor 5##################
  POS(q5,5)
#####################################################







def CIND(pos):
  global t6, t7, t8, t9, t10
  if (pos[4] == 1 ):
    q5 = 80
  else:
    q5 = 0

  x6 = int(pos[0])
  x7 = int(pos[1])
  x8 = int(pos[2])
  x9 = int(pos[3])
  x10 = int(pos[4])  
################### Motor 6 #########################
  if (x6>t6):
    for x6 in range(t6,x6):
      POS(x6,6)
      time.sleep(0.03)
  else:
    for x6 in range(t6,x6,-1):
      POS(x6,6)
      time.sleep(0.03)
  t6 = x6
################### Motor 7 #########################
  if (x7>t7):
    for x7 in range(t7,x7):
      POS(x7,7)
      time.sleep(0.03)
  else:
    for x7 in range(t7,x7,-1):
      POS(x7,7)
      time.sleep(0.03)
  t7 = x7
################### Motor 8 #########################
  if (x8>t8):
    for x8 in range(t8,x8):
      POS(x8,8)
      time.sleep(0.03)
  else:
    for x8 in range(t8,x8,-1):
      POS(x8,8)
      time.sleep(0.03)
  t8 = x8
################### Motor 9 #########################    
  if (x9>t9):
    for x9 in range(t9,x9):
      POS(x9,9)
      time.sleep(0.03)
  else:
    for x9 in range(t9,x9,-1):
      POS(x9,9)
      time.sleep(0.03)
  t9 = x9

################### Motor 10 ########################  
  POS(int(q5),10)
#####################################################
  
def listener():
    rospy.init_node('mover_brazos_grados', anonymous=True)
    rospy.Subscriber('derecho', num, callbackderecho)
    rospy.Subscriber('izquierdo', num, callback)
    rospy.Subscriber('cabezarot', num, callbackrot)
    rospy.Subscriber('cabezarot2', num, callbackrot2)
    rospy.spin()
    

pwm = PWM(0x40)

servoMin = 10  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
pwm.setPWMFreq(50)                        # Set frequency to 50 Hz
condt = 0

if __name__ == '__main__':

    listener()

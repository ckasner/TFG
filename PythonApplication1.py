

import sys
import time
import ovr
from socket import *
import numpy as np
from math import cos, sin, radians, degrees, atan2, sqrt, acos, pi
from Quaternion import Quat
from collections import namedtuple
import datetime 

def convert_to_degrees(radians):
    return (radians*180) / pi

def quaternion_to_euler(x,y,z,w):
    sqw = w * w
    sqx = x * x
    sqy = y * y
    sqz = z * z

    normal = math.sqrt(sqw + sqx + sqy + sqz)
    pole_result = (x * z) + (y * w)

    if (pole_result > (0.5 * normal)): # singularity at north pole
        ry = math.pi/2 #heading/yaw?
        rz = 0 #attitude/roll?
        rx = 2 * math.atan2(x, w) #bank/pitch?
        return Euler(rx, ry, rz)
    if (pole_result < (-0.5 * normal)): # singularity at south pole
        ry = -math.pi/2
        rz = 0
        rx = -2 * math.atan2(x, w)
        return Euler(rx, ry, rz)

    r11 = 2*(x*y + w*z)
    r12 = sqw + sqx - sqy - sqz
    r21 = -2*(x*z - w*y)
    r31 = 2*(y*z + w*x)
    r32 = sqw - sqx - sqy + sqz

    rx = math.atan2( r31, r32 )
    ry = math.asin ( r21 )
    rz = math.atan2( r11, r12 )

    return Euler(rx, ry, rz)

ovr.initialize(None)
session, luid = ovr.create()
hmdDesc = ovr.getHmdDesc(session)
print hmdDesc.ProductName
aux = 0
aux2 = 9



host = "192.168.1.35"

print host

port = 4446
port2 = 4447
s = socket(AF_INET, SOCK_STREAM)
s2 = socket(AF_INET, SOCK_STREAM)
print "Socket Made"
s.bind((host,port))
s2.bind((host,port2))
print "Socket Bound"

s.listen(5)
s2.listen(5)
print "Listening for connections..."
q,addr = s.accept()

q2,addr2 = s2.accept()


pos=0
posH = 0


time.sleep(5)


ts  = ovr.getTrackingState(session, ovr.getTimeInSeconds(), True)
if ts.StatusFlags & (ovr.Status_OrientationTracked | ovr.Status_PositionTracked):
    time.sleep(0.200)
        
    pos =ts.HeadPose.ThePose.Orientation.x
    posH =ts.HeadPose.ThePose.Orientation.y


    degaux = convert_to_degrees(pos)
    degauxH = convert_to_degrees(posH)
    degaux = degaux+90
    degaux = round(degaux)
    deg = degaux

    degauxH = degauxH+90
    degauxH = round(degauxH)
    degH = degauxH

    data = str(degH)

    q2.send(data)
    
   
    i=0
    t=0

while(1):  
    ts  = ovr.getTrackingState(session, ovr.getTimeInSeconds(), True)
    if ts.StatusFlags & (ovr.Status_OrientationTracked | ovr.Status_PositionTracked):
        
        
        pos =ts.HeadPose.ThePose.Orientation.x
        deg = convert_to_degrees(pos*2.2)
  
        deg = deg+90
        deg = round(deg)

        posH =ts.HeadPose.ThePose.Orientation.y
        degH = convert_to_degrees(posH*2.2)
  
        degH = degH+90
        degH = round(degH)
     
       

        if(abs(degaux-deg)>4):
            if((deg < 0.0) | (deg >170.0)):
                continue

            if (deg>110.0):
                q2.send("A")
                deg=105.0
                data=str(deg)
                q.send(data)
            elif (deg<109.0):
                q2.send("P")
                data=str(deg)
                q.send(data)
            else:
                data = str(deg)
                q.send(data)  
          
   
            pos=0
            degaux = deg
            deg = 0
         

        pos=0
        deg = 0



        if(abs(degauxH-degH)>8):
           
            data = str(degH)
            print data
            q2.send(data)  
   
            posH=0
            degauxH = degH
            degH = 0
         

        posH=0
        degH = 0
  
    
    time.sleep(0.200)
    


ovr.destroy(session)
ovr.shutdown()
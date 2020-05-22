#!/usr/bin/env python
#encoding: utf8                 #長くてコメントが増えそうなので入れました
import sys, rospy
from pimouse_ros.msg import LightSensorValues

rospy.init_node('lightsensors')

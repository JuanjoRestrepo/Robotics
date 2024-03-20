#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def callback(msg):
    print(msg)

# ===== Node + SUbscriber initialization =====
# Initializing subscriber node
rospy.init_node('subscriber')

# Creating subscriber object (It is a message: msg_name, msg_type, callback)
rospy.Subscriber('topic', Int64, callback)

# Keeps the Subscriber Node running/spinning
rospy.spin()

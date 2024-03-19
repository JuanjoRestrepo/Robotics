#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

# ===== Node + Topic initialization =====
# Initializing publisher node
rospy.init_node('publisher_node')

# Creating publisher object (It is a message: msg_name, msg_type, queue_size)
pub = rospy.Publisher('topic', Int64, queue_size=1)

# Keep sending messages
while not rospy.is_shutdown():
    pub.publish(1) # sends number one as a data message
    rospy.sleep(1) #sleeps for a second
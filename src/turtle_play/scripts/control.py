#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("control")
publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)

msg = Twist()
msg.linear.x = -1 # 1m/s

for i in range(5):
    publisher.publish(msg)
    rospy.sleep(1)

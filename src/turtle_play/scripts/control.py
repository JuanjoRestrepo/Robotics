#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback(msg):
    print(msg)

rospy.init_node("control")
publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 1)
rospy.Subscriber("/turtle1/pose", Pose, callback)

msg = Twist()
#msg.linear.x = 1 # 1m/s
msg.angular.z = 1 #rads

for i in range(5):
    publisher.publish(msg)
    rospy.sleep(1)

#rospy.spin()

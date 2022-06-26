#!/usr/bin/env python3


import rospy
from std_msgs.msg import Int8MultiArray


def callback(data):
    rospy.loginfo(data.data)
    
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/chatter', Int8MultiArray, callback)
    rospy.spin()
    
    
if __name__=='__main__':
   try:
       listener()
   except KeyboardInterrupt:
       pass
   
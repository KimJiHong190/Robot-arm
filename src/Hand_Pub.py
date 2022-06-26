#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8MultiArray
from hand import main

def talker():
    pub=rospy.Publisher('chatter',Int8MultiArray,queue_size=1)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        cord=Int8MultiArray()
        cord.data=main()
        rospy.loginfo(cord)
        pub.publish(cord)
        rate.sleep()
        
        
if __name__ =='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
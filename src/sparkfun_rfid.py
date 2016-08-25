#!/usr/bin/env python
# ROS imports
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    
    rospy.init_node('talker', anonymous=True)
    
    # Parameters
    port = rospy.get_param('~port','/dev/ttyUSB0')
    rospy.loginfo("%s"%port)

    try:
        talker()
    except rospy.ROSInterruptException:
        pass

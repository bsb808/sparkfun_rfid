#!/usr/bin/env python
# ROS imports
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header

import serial

def rfidnode():
    rospy.init_node('talker', anonymous=True)
    
    # Parameters
    port = rospy.get_param('~port','/dev/ttyUSB0')
    rospy.loginfo("%s"%port)

    ser = serial.Serial(port,9600,timeout=1.0)

    pub = rospy.Publisher('rfid', String, queue_size=10)

    msg = String()
    
    while True:
        x = ser.read(16)
        #print type(x)
        #print len(x)

        if len(x)==16:
            rfid = ""
            for xx in x:
                rfid += "%d:"%ord(xx)
            rfid = rfid[:-1]
            rospy.loginfo(rfid)
            msg.data = rfid
            pub.publish(rfid)


if __name__ == '__main__':
    

    try:
        rfidnode()
    except rospy.ROSInterruptException:
        pass

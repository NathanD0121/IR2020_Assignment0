#!/usr/bin/env python
#Publisher node

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def botPublisher():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.init_node('botPublisher', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        #TODO: Add movement code here
        #move = 0 (stop), move = 1 (forward), move = 2(rotate)
        #Might need to use /cmd_vel to control robot

        #move = 0

        msg = Twist()
        msg.angular.z = 1.0

        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        botPublisher()
    except rospy.ROSInterruptException:
        pass

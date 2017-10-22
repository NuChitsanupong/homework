#!/usr/bin/python2
import rospy
# import module string
from calculate.msg import cal_detail

def publisher():
        pub = rospy.Publisher('/publisher_cal', cal_detail, queue_size=10)
	msg = cal_detail()
	msg.command = "plus"
	msg.num1 = 1
	msg.num2 = 3
        while not rospy.is_shutdown():
                rospy.loginfo(msg)
                pub.publish(msg)

if __name__=='__main__':
        rospy.init_node('node_publisher', anonymous=True)
        publisher()


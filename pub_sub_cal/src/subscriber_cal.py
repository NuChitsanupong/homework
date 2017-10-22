#!/usr/bin/python2
import rospy
from calculate.msg import cal_detail

def callback(data):
	if data.command == "plus":		
        	rospy.loginfo("%d + %d = %d"%(data.num1,data.num2,(data.num1+data.num2)))
	elif data.command == "minus":
                rospy.loginfo("%d - %d = %d"%(data.num1,data.num2,(data.num1-data.num2)))

if __name__=='__main__':
        rospy.init_node('node_subscriber', anonymous=True)
        rospy.Subscriber('/publisher_cal', cal_detail, callback)
        rospy.spin()


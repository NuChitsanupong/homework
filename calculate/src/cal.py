#!/usr/bin/python2
import rospy
inp = input()
num1 = int(input())
num2 = int(input())
if inp == 1:
	print("%.2f"%(num1+num2))
if inp == 2:
        print("%.2f"%(num1-num2))


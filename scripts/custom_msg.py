#! /usr/bin/env python

import rospy
import sys
import os
from nav_msgs.msg import Odometry as Odom
from rt1_second_assignment.msg import odom_custom_msg

def pub(message):
## This is the publisher, that publishes the robot's position and velocity as a custom message, (x,y,vel_x,vel_y), by relying on the values published in the /odom topic. The user interface is defined in the action_client script ##
	publisher = rospy.Publisher("robot_informations", odom_custom_msg, queue_size = 5)
	
	custom_msg = odom_custom_msg()
	
	custom_msg.x = message.pose.pose.position.x
	custom_msg.y = message.pose.pose.position.y
	custom_msg.vel_x = message.twist.twist.linear.x
	custom_msg.vel_y = message.twist.twist.linear.y
	
	print("- [NODE] Publisher's message: ", custom_msg)
	
	publisher.publish(custom_msg)
	

if __name__ == "__main__":
	try:
		# Initialize custom_msg node and subscribe the publisher to the /odom topic
		rospy.init_node('custom_msg')
		rospy.Subscriber('/odom', Odom, pub)
		
		# Waiting command
		rospy.spin()
	
	# Handling server errors
	except rospy.ROSInterruptException:
		print("- [ERROR] Program aborted before completion.			-\n")	

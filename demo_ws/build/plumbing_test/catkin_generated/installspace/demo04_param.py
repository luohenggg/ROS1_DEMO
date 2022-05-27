#!/usr/bin/env python2

import rospy
"""
    更换背景色
"""
if __name__ == "__main__":
    rospy.init_node("background")
    rospy.set_param("/turtlesim/background_b",0)
    rospy.set_param("/turtlesim/background_r",255)
    rospy.set_param("/turtlesim/background_g",0)
#! /usr/bin/env python
"""
"""

import rospy

if __name__ == "__main__":
    rospy.init_node("set_param_p")


    #设置参数
    rospy.set_param("p_int",10)
    rospy.set_param("p_string","hello_world")

    #修改
    rospy.set_param("p_int",5)
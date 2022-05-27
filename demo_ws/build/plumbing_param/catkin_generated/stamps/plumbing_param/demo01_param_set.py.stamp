#! /usr/bin/env python
"""
python实现参数服务器  新增和修改
"""

import rospy

if __name__ == "__main__":
    rospy.init_node("set_param_p")


    #设置参数
    rospy.set_param("p_int",10)
    rospy.set_param("p_string","hello_world")
    rospy.set_param("p_list",["hello","haha","xixi"])
    rospy.set_param("p_dict",{"name":"huliu","age":8})
    #修改
    rospy.set_param("p_int",5)
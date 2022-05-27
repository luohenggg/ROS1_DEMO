#!/usr/bin/env python2
"""
    参数服务器之  删除
        rospy.delete_param("键")
            键存在时，可以删除成功，键不存在时，会抛出异常
"""
import rospy


if __name__ == "__main__":
    rospy.init_node("delete_param")

    try:
        rospy.delete_param("p_int")
        rospy.loginfo("删除成功")
    except:
        rospy.loginfo("删除失败")
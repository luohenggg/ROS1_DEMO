#! /usr/bin/env python

import rospy

if __name__=="__main__":
    rospy.init_node("timer")

    #获取当前时刻
    right_now = rospy.Time.now()
    rospy.loginfo("当前时刻:%.2f",right_now.to_sec())
    rospy.loginfo("当前时刻:%.2f",right_now.to_nsec())
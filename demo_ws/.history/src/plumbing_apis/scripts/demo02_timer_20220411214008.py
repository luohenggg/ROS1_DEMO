#! /usr/bin/env python

import rospy

if __name__=="__main__":
    rospy.init_node("timer")

    #获取当前时刻
    right_now = rospy.Time.now()
    rospy.loginfo("当前时刻:%.2f",right_now.to_sec())
    rospy.loginfo("当前时刻:%.2f",right_now.to_nsec())

    #自定义时刻
    some_time1 = rospy.Time(123.546546)
    some_time2 = rospy.Time(123.565)
    rospy.loginfo("设置时刻1:%.2f",some_time1.to_sec())
    rospy.loginfo("设置时刻2:%.2f",some_time2.to_sec())

    #从时间创建对象
    some_time3  = rospy.Time.from_sec(545.32)
    rospy.loginfo("设置时刻3:%.2f",some_time3.to_sec())

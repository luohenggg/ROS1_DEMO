#! /usr/bin/env python

import rospy

def doMsg(event):
    rospy.loginfo("+++++++")
    rospy.loginfo("当前时刻：%s",str(event.current_real))
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

    #持续时间相关API
    rospy.loginfo("持续时间测试开始")
    du = rospy.Duration(3.3)
    rospy.loginfo("du1 持续时间:%.2f",du.to_sec())
    #rospy.sleep(du)#休眠函数
    rospy.loginfo("持续时间测试结束")

    #时间与时刻的运算
    rospy.loginfo("时间运算")
    now = rospy.Time.now()
    du1 = rospy.Duration(10)
    du2 = rospy.Duration(20)
    rospy.loginfo("当前时刻:%.2f",now.to_sec())
    before_now = now - du1
    after_now = now + du1
    dd = du1 + du2
    rospy.loginfo("之前时刻:%.2f",before_now.to_sec())
    rospy.loginfo("之后时刻:%.2f",after_now.to_sec())
    rospy.loginfo("持续时间相加:%.2f",dd.to_sec())

    #设置执行频率
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        rate.sleep()
        rospy.loginfo("+++++++++++")

    rospy.Timer(rospy.Duration(1), doMsg)
    rospy.spin()
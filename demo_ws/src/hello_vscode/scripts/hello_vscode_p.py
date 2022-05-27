
#! /usr/bin/env python

#导包
import rospy
#入口
if __name__=="__main__":

    #初始化ros节点
    rospy.init_node("hello_vscode_ppppp")
    #输出
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        #rospy.loginfo("hello vscode!这是Python!")
        #rospy.logdebug("Debug message dddddddddddddd")
        rospy.loginfo("Info message ooooooooooooo")
        # rospy.logwarn("warn message wwwwwwwwwwwwww")
        # rospy.logerr("Error EEEEEEEEEEEEEEE")
        # rospy.logfatal("Fatal fffffffffffffffffffff")
        rate.sleep()

#! /usr/bin/env python

#导包
import rospy
#入口
if __name__=="__main__":

    #初始化ros节点
    rospy.init_node("hello_vscode_p")
    #输出
    rospy.loginfo("hello vscode!这是Python!")
    
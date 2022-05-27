#! /usr/bin/env python

import rospy
from turtlesim.msg import Pose
"""
    订阅小乌龟的位姿：实时获取小乌龟在窗体中的坐标并打印
    准备工作：
        1.获取话题名称  rostopic list -->/turtle1/pose  和类型 rostopic type /turtle1/pose -->turtlesim/Pose
        2.获取消息类型 rosmsg info turtlesim/Pose  --> float32 x  float32 y...

    实现流程：
        1.导包
        2.初始化ROS节点
        3.创建订阅者对象
        4.回调函数处理订阅的数据
        5.spin
"""

def doPose(pose):
    rospy.loginfo("乌龟坐标：x=%.2f,y=%.2f,theta=%.2f,linear_vel =%.2f,angular_vel=%.2f",
    pose.x,pose.y,pose.theta,pose.linear_velocity,pose.angular_velocity)
if __name__=="__main__":
        # 2.初始化ROS节点
        rospy.init_node("sub_pose")
        # 3.创建订阅者对象
        sub = rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size = 10)
        # 4.回调函数处理订阅的数据

        # 5.spin
        rospy.spin()
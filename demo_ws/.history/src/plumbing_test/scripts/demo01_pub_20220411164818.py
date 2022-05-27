#! /usr/bin/env python

"""
    编写ROS节点，控制小乌龟画圈

    准备工作：
        1.获取topic(rostopic list找出话题--> /turtle1/cmd_vel)
        2.获取topic类型(rostopic type /turtle1/cmd_vel --> geometry_msgs/Twist)
        3.获取消息类型(rosmsg info geometry_msgs/Twist--->       geometry_msgs/Vector3 linear....)
        4.运行前，先启动turtlesim_node 节点(rosrun turtlesim turtlesim_node)

    实现流程：
        1.导包
        2.初始化ROS节点
        3.创建发布者对象
        4.循环发布运动控制消息
"""

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
        # 2.初始化ROS节点
        rospy.init_node("control_circle")
        # 3.创建发布者对象
        pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size = 10)
        # 4.循环发布运动控制消息
        rate = rospy.Rate(10)
        msg = Twist()
        msg.linear.x = 1.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.0

        while not rospy.is_shutdown():
            pub.publish(msg)
            rate.sleep()

#! /usr/bin/env python2.7
# -*- coding:UTF-8 -*-

import rospy
import rosbag
from std_msgs.msg import String
"""
    需求: 读取 磁盘上 的 bag文件
    流程：
        1.导包
        2.初始化
        3.创建 rosbag 对象并且打开文件流
        4.读数据
        5.关闭流
"""
if __name__ == "__main__":
    # 2.初始化
    rospy.init_node("rosbag_read")
    # 3.创建 rosbag 对象并且打开文件流
    bag = rosbag.Bag("./bags/hi.bag",'r')
    # 4.读数据
    msgs = bag.read_messages()
    for topic,msg,time in msgs:
        rospy.loginfo("话题:%s,消息:%s,时间;%s",topic,msg.data,time)
    # 5.关闭流
    bag.close()
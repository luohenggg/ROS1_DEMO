#! /usr/bin/env python2.7
# -*- coding:UTF-8 -*-
import rospy
import rosbag
from std_msgs.msg import String
"""
    需求: 写出消息数据 到磁盘上 的 bag文件
    流程：
        1.导包
        2.初始化
        3.创建 rosbag 对象并且打开文件流
        4.写数据
        5.关闭流
"""
if __name__ == "__main__":
    # 2.初始化
    rospy.init_node("rosbag_write")
    # 3.创建 rosbag 对象并且打开文件流
    bag = rosbag.Bag("./bags/hi.bag",'w')
    # 4.写数据
    msgs = String()
    msgs.data = "hello"
    bag.write("/liaoTian",msgs)
    bag.write("/liaoTian",msgs)
    bag.write("/liaoTian",msgs)
    bag.write("/liaoTian",msgs)
    bag.write("/liaoTian",msgs)
    # 5.关闭流
    bag.close()
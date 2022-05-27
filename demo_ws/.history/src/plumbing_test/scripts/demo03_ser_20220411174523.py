#! /usr/bin/env python
"""
    生成一直小乌龟
    准备工作：
        1.服务话题 rostopic list  -->  /spawn
        2.服务话题类型rostopic type /spawn  -->turtlesim/Spawn
        3.服务消息类型 rossrv type turtlesim/Spawn
        4.运行前县启动 turtlesim_node 节点

    实现流程:
        1.导包
            需要包含turtlesim 包下资源，注意在package.xml配置
        2.初始化ROS节点
        3.创建service客户端
        4.等待服务启动
        5.发送请求
        6.处理响应
"""
import rospy

if __name__=="__main__":
    pass
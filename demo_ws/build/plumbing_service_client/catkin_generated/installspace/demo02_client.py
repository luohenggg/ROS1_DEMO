#!/usr/bin/env python2
"""
需求:
        编写两个节点实现服务通信，客户端节点需要提交两个整数到服务器
        服务器需要解析客户端提交的数据，相加后，将结果响应回客户端
        客户端再解析

    服务器端实现:
        # 1. 导包
        # 2. 初始化ROS节点
        # 3. 创建请求对象
        # 4. 发送请求
        # 5. 接收并处理响应
"""

  # 1. 导包
import rospy
from plumbing_service_client.srv import *
import sys

if __name__ == "__main__":
    #优化
    if len(sys.argv) != 3:
        rospy.loginfo("请正确输入参数")
        sys.exit(1)
    # 2. 初始化ROS节点
    rospy.init_node("AddInts_client")
    # 3. 创建请求对象
    client = rospy.ServiceProxy("AddInts",AddInts)

    #请求前，等待服务已经就绪
    client.wait_for_service()
    # 4. 发送请求
    #resp = client(3,5)
    req = AddIntsRequest()
    #优化实现
    req.num1 = int(sys.argv[1]) 
    req.num2 = int(sys.argv[2]) 
    # 5. 接收并处理响应
    resp = client.call(req)
    rospy.loginfo("响应结果:%d",resp.sum)

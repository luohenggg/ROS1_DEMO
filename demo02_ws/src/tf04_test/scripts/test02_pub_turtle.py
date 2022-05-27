#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped
import tf
import sys
"""
    发布方：订阅乌龟的位姿信息，转换成坐标系的相对关系，再发布
    准 备：
        话题：/turtlex/pose
        消息类型: /turtlesim/Pose
    
    流程：
        1.导包
        2.初始化ROS节点
        3.创建订阅对象
        4.回调函数处理订阅到的消息(核心)
        5.spin()
"""

turtle_name=""

def doPose(pose):
    #1.创建发布坐标系相对关系的对象
    pub = tf2_ros.TransformBroadcaster()
    #2.将pose转换成 坐标系相对关系消息
    ts = TransformStamped()
    ts.header.frame_id = "world"
    ts.header.stamp = rospy.Time.now()
    ts.child_frame_id = turtle_name
    ##---子级坐标系 相对于 父级坐标系的偏移量
    ts.transform.translation.x = pose.x
    ts.transform.translation.y = pose.y
    ts.transform.translation.z = 0
    ##---四元数
    #从 欧拉角 转换 四元数
    """
        乌龟是2D,不存在 X 上的翻滚Y上的俯仰,只有Z上的偏航
        0 0 pose.theta
    """
    qtn = tf.transformations.quaternion_from_euler(0,0,pose.theta)
    ts.transform.rotation.x = qtn[0]
    ts.transform.rotation.y = qtn[1]
    ts.transform.rotation.z = qtn[2]
    ts.transform.rotation.w = qtn[3]

    #3.发布
    pub.sendTransform(ts)




if __name__ == "__main__":
    # 2.初始化ROS节点
    rospy.init_node("dynamic_pub")
    #解析传入的参数
    if len(sys.argv) != 4:
        rospy.loginfo("请输出4个参数")
        sys.exit(1)
    else:
        turtle_name = sys.argv[1]
    # 3.创建订阅对象
    sub = rospy.Subscriber(turtle_name + "/pose",Pose,doPose,queue_size=100)
    # 4.回调函数处理订阅到的消息(核心)
    # 5.spin()
    rospy.spin()
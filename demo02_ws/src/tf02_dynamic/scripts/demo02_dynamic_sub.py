#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-


import rospy
import tf2_ros
from tf2_geometry_msgs import PointStamped
"""
直接复制  静态坐标变换下  的订阅方实现
修改4个地方：
1.子坐标名字 ps.header.frame_id = "turtle1"
2.父坐标名字 ps_out = buffer.transform(ps,"world")
3.时间戳删去now, ps.header.stamp = rospy.Time()
4.节点名字    rospy.init_node("dynamic_sub")
"""


if __name__ == "__main__":
    # 2.初始化
    rospy.init_node("dynamic_sub")
    # 3.创建订阅对象
    #3-1创建缓存对象
    buffer = tf2_ros.Buffer()
    #3-2创建订阅对象(将缓存传入)
    sub = tf2_ros.TransformListener(buffer)
    # 4.组织被转换的坐标点
    #创建一个radar坐标系中的坐标点
    ps = PointStamped()
    ps.header.frame_id = "turtle1"
    ps.header.stamp = rospy.Time()
    ps.point.x = 22.0
    ps.point.y = 32.0
    ps.point.z = 55.0

    # 5.转换逻辑实现, 调用TF封装的算法
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            ps_out = buffer.transform(ps,"world")
            """
            transform函数,参数1为被转换的坐标点, 参数2为目标坐标系
            返回值：转换后的坐标点

                PS:
                问题：抛出异常 base_link 不存在
                原因: 转换函数调用时，可能还没有订阅到坐标系的相对信息
                解决: 用try捕获异常, 并处理
            """
            # 6.输出结果
            rospy.loginfo("转换后的坐标:(%.2f,%.2f,%.2f),参考的坐标系:%s",
                            ps_out.point.x,
                            ps_out.point.y,
                            ps_out.point.z,
                            ps_out.header.frame_id)
        except Exception as e:
            rospy.logwarn("错误提示:%s",e)

        rate.sleep()
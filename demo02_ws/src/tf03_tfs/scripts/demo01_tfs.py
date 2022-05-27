#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import rospy
import tf2_ros
from tf2_geometry_msgs import PointStamped


if __name__ == "__main__":
    # 2.初始化
    rospy.init_node("tfs_static_sub")
    # 3.创建订阅对象
    #3-1创建缓存对象
    buffer = tf2_ros.Buffer()
    #3-2创建订阅对象(将缓存传入)
    sub = tf2_ros.TransformListener(buffer)
    # 4.组织被转换的坐标点
    #创建一个son1坐标系中的坐标点(1,2,5)
    ps = PointStamped()
    ps.header.frame_id = "son1"
    ps.header.stamp = rospy.Time()
    ps.point.x = 1.0
    ps.point.y = 2.0
    ps.point.z = 3.0

    # 5.转换逻辑实现, 调用TF封装的算法
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            #---计算 son1 相对于 son2 的坐标关系
            ts = buffer.lookup_transform("son2","son1",rospy.Time(0))
            rospy.loginfo("父级坐标系:%s,子级坐标系:%s,偏移量(%.2f,%.2f,%.2f)",
                        ts.header.frame_id,
                        ts.child_frame_id,
                        ts.transform.translation.x,
                        ts.transform.translation.y,
                        ts.transform.translation.z,
                        )
            #转换实现
            ps_out = buffer.transform(ps,"son2")

            # 6.输出结果
            rospy.loginfo("源坐标点转换后的坐标:(%.2f,%.2f,%.2f),参考的坐标系:%s",
                            ps_out.point.x,
                            ps_out.point.y,
                            ps_out.point.z,
                            ps_out.header.frame_id)
        except Exception as e:
            rospy.logwarn("错误提示:%s",e)

        rate.sleep()
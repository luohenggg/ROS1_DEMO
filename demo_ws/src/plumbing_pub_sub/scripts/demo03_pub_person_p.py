#! /usr/bin/env python
import rospy
from plumbing_pub_sub.msg import Person
"""
    发布方：发布人的消息
        1.导包；
        2.初始化ROS节点；
        3.创建发布者对象；
        4.组织发布逻辑并发布数据。
"""
if __name__=="__main__":
    # 2.初始化ROS节点；
    rospy.init_node("dama")
    # 3.创建发布者对象；
    pub = rospy.Publisher("dapai",Person,queue_size=10)
    # 4.组织发布逻辑并发布数据。
    #4-1 创建Person数据
    p = Person()
    p.name = "奥特曼"
    p.age = 18
    p.height = 1.85
    #4-2 创建Rate对象
    rate = rospy.Rate(1)
    #4-3 循环发布数据
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("发布人的姓名：%s,年龄：%d,身高：%.2f",p.name,p.age,p.height)
        p.age += 1
        rate.sleep()

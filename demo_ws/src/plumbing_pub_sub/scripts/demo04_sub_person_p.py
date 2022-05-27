#! /usr/bin/env python
import rospy
from plumbing_pub_sub.msg import Person
"""
    订阅方：订阅人的消息
        1.导包；
        2.初始化ROS节点；
        3.创建订阅者对象；
        4.处理订阅消息；
        5.spin()。
"""
def doperson(per):
    rospy.loginfo("订阅到的消息：姓名：%s,年龄：%d,身高：%.2f",per.name,per.age,per.height)

if __name__=="__main__":
    # 2.初始化ROS节点；
    rospy.init_node("daye")
    # 3.创建订阅者对象；
    sub = rospy.Subscriber("dapai",Person,doperson,queue_size=10)
    # 4.处理订阅消息；
    # 5.spin()。
    rospy.spin()
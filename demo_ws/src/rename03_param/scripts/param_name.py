#! /usr/bin/env python
import rospy

if __name__=="__main__":
    rospy.init_node("hi")
    """
        设置不同类型的参数
    """
    #1.全局
    rospy.set_param("/radiusA",10)
    #2.相对
    rospy.set_param("radiusB",10)

    #3.私有
    rospy.set_param("~radiusC",10)
    while not rospy.is_shutdown():

        pass
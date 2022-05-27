#! /usr/bin/env python

"""
    参数服务器操作之  查询
        get_param(键，默认值)
            当键存在时，返回对应的值，如果不存在返回默认值
        get_param_cached
        get_param_names
        has_param
        search_param
"""
import rospy

if __name__=="__main__":
    rospy.init_node("get_param")

    #获取参数
    int_value = rospy.get_param("p_int",1000)
    string_value = rospy.get_param("string")
    p_list = rospy.get_param("p_list")
    p_dict = rospy.get_param("p_dict")

    rospy.loginfo("获取的数据:%d,%s", int_value,string_value)

    for ele in p_list:
        rospy.loginfo("ele = %s",ele)

    rospy.loginfo("name = %s , age = %d",p_dict["name"],p_dict["age"])

    #get_param_cached
    int_cached = rospy.get_param_cached("p_int")
    rospy.loginfo("缓存数据:%d",int_cached)

    #get_param_names
    names = rospy.get_param_names()
    for name in names:
        rospy.loginfo("names = %s",name)

    rospy.loginfo("-"*80)

    #has_param
    flag  = rospy.has_param("p_int")
    rospy.loginfo("包含p_int吗%d",flag)

    #search_param
    key = rospy.search_param("p_int")
    rospy.loginfo("搜索的键= %s",key)
#include "ros/ros.h"
#include "std_msgs/String.h"
/*
    订阅方实现：
        1.包含头文件;
        2.初始化ROS节点：命名（唯一）；
        3.实例化ROS句柄；
        4.实例化 订阅者对象；
        5.处理订阅到的数据；
        6.ros.spin()函数。
*/

void doMsg(const std_msgs::String::ConstPtr &msg){
    //通过msg获取并操作订阅到的数据
    ROS_INFO("翠花订阅的数据：%s",msg->data.c_str());
}

int main(int argc, char *argv[])
{
        setlocale(LC_ALL,"");
        // 2.初始化ROS节点：命名（唯一）；
        ros::init(argc,argv,"cuihua");
        // 3.实例化ROS句柄；
        ros::NodeHandle nh;
        // 4.实例化 订阅者对象；
        ros::Subscriber sub = nh.subscribe("chatter",10,doMsg);
        // 5.处理订阅到的数据；（回调函数）
        // 6.ros.spin()函数。
        ros::spin();

    return 0;
}

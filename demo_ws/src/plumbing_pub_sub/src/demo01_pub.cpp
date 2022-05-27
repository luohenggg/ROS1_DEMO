#include "ros/ros.h"
#include "std_msgs/String.h"//普通文本类型的消息
#include <sstream>
/*
    发布方实现：
        1.包含头文件;
        2.初始化ROS节点：命名（唯一）；
        3.实例化ROS句柄；
        4.实例化 发布者对象
        5.组织被发布的数据，并编写逻辑发布数据。

*/

int main(int argc, char *argv[])
{
        setlocale(LC_ALL,"");
        // 2.初始化ROS节点：命名（唯一）；
        //参数1和参数2 后期为节点传值会使用
        //参数3 是节点名称，是一个标识符，需要保证运行后，在ROS网络拓扑中唯一
        ros::init(argc,argv,"ergouzi");

        // 3.实例化ROS句柄；
        ros::NodeHandle nh;//该类封装了ROS中的一些常用功能

        // 4.实例化 发布者对象
        ros::Publisher pub = nh.advertise<std_msgs::String>("che",10);
        //泛型：发布的消息类型
        //参数1：要发布的话题
        //参数2：队列中最大保存的消息数，超出此阈值时，先进的先销毁


        // 5.组织被发布的数据，并编写逻辑发布数据。
        //节点不死
        //
        //先创建被发布的消息
        std_msgs::String msg;

        std::string msg_front  = "Hello,你好！";//消息前缀

        //逻辑（一秒10次）
        ros::Rate r(1);
        int count = 0;
        //编写循环，循环中发布数据
        while (ros::ok())
        {
           // msg.data = "hello";
            std::stringstream ss;
            ss << msg_front << count;//消息拼接
            msg.data = ss.str();
            pub.publish(msg); //发布消息
            //添加日志：
            ROS_INFO("发送的消息：%s",msg.data.c_str());
    

            r.sleep();//根据前面制定的发送频率自动休眠，休眠时间 = 1/频率。
            count++;//循环结束前，让count自增
        }
        
    return 0;
}

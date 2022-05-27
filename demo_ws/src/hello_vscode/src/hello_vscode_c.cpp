#include "ros/ros.h"
// #include <ros/ros.h>

int main(int argc, char  *argv[])
{
    // setlocale(LC_ALL,"");
    // ros::init(argc,argv,"HelloVScode");
    // ROS_INFO("Hello,VScode哈哈哈");
    // return 0;
    ros::init(argc,argv,"log_demo");
    ros::NodeHandle nh;

    ros::Rate r(0.3);
    while (ros::ok())
    {
        ROS_DEBUG("Debug message d");
        ROS_INFO("Info message oooooooooooooo");
        ROS_WARN("Warn message wwwww");
        ROS_ERROR("Erroe message EEEEEEEEEEEEEEEEEEEE");
        ROS_FATAL("Fatal message FFFFFFFFFFFFFFFFFFFFFFFFFFFFF");
        r.sleep();
    }


    return 0;
}
/*  
    ROS 节点:输出各种级别的日志信息

*/
// #include "ros/ros.h"

// int main(int argc, char *argv[])
// {
//     ros::init(argc,argv,"log_demo");
//     ros::NodeHandle nh;

//     ros::Rate r(0.3);
//     while (ros::ok())
//     {
//         ROS_DEBUG("Debug message d");
//         ROS_INFO("Info message oooooooooooooo");
//         ROS_WARN("Warn message wwwww");
//         ROS_ERROR("Erroe message EEEEEEEEEEEEEEEEEEEE");
//         ROS_FATAL("Fatal message FFFFFFFFFFFFFFFFFFFFFFFFFFFFF");
//         r.sleep();
//     }


//     return 0;
// }

# Motion Control Robot arm

## OverView
![](https://github.com/KimJiHong190/Robot-arm/blob/master/hand1.gif)

Inspired by the video https://www.youtube.com/watch?v=7KV5489rL3c from Murtazas workshop. 
This repo is structured as a catkin workspace in a ROS Noetic envivornment on Ubuntu 20.04. 

The provided ROS Catkin make build system can be utilized, but I used ```catkin tools``` instead (see catkin tools website). Compilation commands below will be given assuming ```catkin tools```. If not using catkin tools on your PC, the stock catkin_make can be used to compile the code via command such as ```catkin_make -DCMAKE_BUILD_TYPE=Release``` from the home of the catkin workspace.

-----------
### Software Checkout and Setup
The software is composed of Python nodes in a ROS framework.
* Ubuntu 20.04 + ROS1 Noetic
* OpenCV 4.5.4.60
* DYNAMIXEL-SDK

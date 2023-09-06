cmake_minimum_required(VERSION 3.0.2)
project(test_all123)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
  geometry_msgs
  urdf
  xacro
  message_generation
)
catkin_package(
  CATKIN_DEPENDS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)
find_package(roslaunch)
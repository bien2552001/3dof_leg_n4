cmake_minimum_required(VERSION 3.0.2)
project(demo_trajectory)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  moveit_msgs
  trajectory_msgs
  moveit_core
  moveit_ros_planning
  moveit_ros_planning_interface
  moveit_ros_perception
  rviz_visual_tools
  moveit_visual_tools
  pluginlib
  geometric_shapes
  pcl_ros
  pcl_conversions
  rosbag
  tf2_ros
  tf2_eigen
  tf2_geometry_msgs
)
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES demo_trajectory
 CATKIN_DEPENDS 
  roscpp rospy 
  std_msgs 
  moveit_core 
  moveit_ros_planning_interface
  moveit_visual_tools
  interactive_markers
  tf2_geometry_msgs
DEPENDS
  EIGEN3
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(direct_kinematic src/direct_kinematic.cpp)
target_link_libraries(direct_kinematic ${catkin_LIBRARIES}
)
add_executable(inverse_kinematic src/inverse_kinematic.cpp)
target_link_libraries(inverse_kinematic ${catkin_LIBRARIES}
)
add_executable(catersian_move src/catersian_move.cpp)
target_link_libraries(catersian_move ${catkin_LIBRARIES}
)


# Unlimit
add_executable(left_move src/python/unlimited/left_move.cpp)
target_link_libraries(left_move ${catkin_LIBRARIES}
)

add_executable(right_move src/python/unlimited/right_move.cpp)
target_link_libraries(right_move ${catkin_LIBRARIES}
)

# Move group CPP
add_executable(move_group1 src/move_group/move_group1.cpp)
target_link_libraries(move_group1 ${catkin_LIBRARIES}
)



install(TARGETS
  direct_kinematic
  inverse_kinematic
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
)

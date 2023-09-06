cmake_minimum_required(VERSION 2.8.3)
project(leg_gazebo)


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

  #Them phan msg
  add_message_files(
    FILES
    RobotMotion.msg
    RobotPosition.msg
  )
  find_package(roslaunch)
  foreach(dir launch script)
  install(DIRECTORY ${dir}/
  DESTINATION
  ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
  endforeach(dir)
  
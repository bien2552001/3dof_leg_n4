#include <ros/ros.h>
#include "moveit/move_group_interface/move_group_interface.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "left_group_movement");
  ros::NodeHandle nh;
  ros::AsyncSpinner spinner2(2);
  spinner2.start();

  // Left group Configuration
  moveit::planning_interface::MoveGroupInterface left_group("left_group");
  std::string left_end_effector_link = left_group.getEndEffector();
  std::string left_reference_frame = "base_link";
  left_group.setPoseReferenceFrame(left_reference_frame);
  left_group.allowReplanning(true);
  // left_group.setGoalOrientationTolerance(0.01);
  // left_group.setGoalPositionTolerance(0.001);
  // left_group.setMaxAccelerationScalingFactor(0.2);
  // left_group.setMaxVelocityScalingFactor(0.2);

  // Repeat the code five times
  for (int i = 0; i < 3; ++i)
  {
    // Moving the Left group

    // left_group.setNamedTarget("left_p0");
    // left_group.move();
    // sleep(2);

    left_group.setNamedTarget("left_p0");
    left_group.move();
    sleep(4);

    left_group.setNamedTarget("left_p1");
    left_group.move();
    sleep(4);
  }
  left_group.setNamedTarget("left_p0");
  left_group.move();
  sleep(1);

  // Clean up
  ros::shutdown();
  return 0;
}

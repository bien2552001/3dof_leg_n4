#include <ros/ros.h>
#include "moveit/move_group_interface/move_group_interface.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "right_right_movement");
  ros::NodeHandle nh;
  ros::AsyncSpinner spinner1(2);
  spinner1.start();

  // right right Configuration
  moveit::planning_interface::MoveGroupInterface right_right("right_group");
  std::string right_end_effector_link = right_right.getEndEffector();
  std::string right_reference_frame = "base_link";
  right_right.setPoseReferenceFrame(right_reference_frame);
  right_right.allowReplanning(true);
  // right_right.setGoalOrientationTolerance(0.01);
  // right_right.setGoalPositionTolerance(0.001);
  // right_right.setMaxAccelerationScalingFactor(0.2);
  // right_right.setMaxVelocityScalingFactor(0.2);

  // Repeat the code five times
  for (int i = 0; i < 3; ++i)
  {
    // Moving the right right

    right_right.setNamedTarget("right_p2");
    right_right.move();
    sleep(4);

    right_right.setNamedTarget("right_p0");
    right_right.move();
    sleep(4);
  }
  right_right.setNamedTarget("right_p0");
  right_right.move();
  sleep(1);

  // Clean up
  ros::shutdown();
  return 0;
}

#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from leg_gazebo.msg import RobotMotion  # Thay your_package_name bằng tên gói của bạn
import csv

class CsvMotionControl:
    def __init__(self):
        self.csv_file = '/home/bien/ROS1/pratice/no1_leg_robot/leg_3dof_test/src/demo/leg_gazebo/scripts/data6.csv'
        self.rate = rospy.Rate(10)  # Tốc độ xuất dữ liệu (10 Hz)

        self.motion_pub = rospy.Publisher('/robot/motion123', RobotMotion, queue_size=10)

        rospy.init_node('csv_motion_control123')

    def read_csv_and_publish(self):
        with open(self.csv_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) >= 3:
                    joint1 = float(row[0])
                    joint2 = float(row[1])
                    joint3 = float(row[2])

                    robot_motion = RobotMotion()
                    robot_motion.joint1 = joint1
                    robot_motion.joint2 = joint2
                    robot_motion.joint3 = joint3

                    self.motion_pub.publish(robot_motion)
                    self.rate.sleep()

if __name__ == '__main__':
    try:
        csv_motion_control = CsvMotionControl()
        csv_motion_control.read_csv_and_publish()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import math
import rospy
from std_srvs.srv import SetBool, SetBoolResponse
from std_msgs.msg import Float64
import time
import csv

class CsvControlService:
    def __init__(self):
        self.csv_file = '/home/bien/ROS1/pratice/no1_leg_robot/leg_3dof_test/src/demo/leg_gazebo/scripts/data6.csv'
        self.csv_publishing = False

        self.start_stop_service = rospy.Service('service_dieu_khien_no2', SetBool, self.csv_control_callback)
        self.service_active = False
        self.default_positions = [1, 1, 1]  # Trạng thái mặc định của robot
        self.default_positions_published = False


        self.LLINK1 = rospy.Publisher('leg_chuanv3/llink1_position/command', Float64, queue_size=10)
        self.LLINK2 = rospy.Publisher('leg_chuanv3/llink2_position/command', Float64, queue_size=10)
        self.LLINK3 = rospy.Publisher('leg_chuanv3/llink3_position/command', Float64, queue_size=10)
        self.RLINK1 = rospy.Publisher('leg_chuanv3/rlink1_position/command', Float64, queue_size=10)
        self.RLINK2 = rospy.Publisher('leg_chuanv3/rlink2_position/command', Float64, queue_size=10)
        self.RLINK3 = rospy.Publisher('leg_chuanv3/rlink3_position/command', Float64, queue_size=10)

        rospy.init_node('Dung_service_dieu_khien_xuat_du_lieu')

    def csv_control_callback(self, req):
        if req.data:
            self.csv_publishing = True
            self.service_active = True
            self.publish_csv_data()
            return SetBoolResponse(True, "CSV data publishing started.")
        else:
            self.csv_publishing = False
            self.service_active = False
            self.move_to_default_position()  # Di chuyển về trạng thái mặc định khi dừng service
            return SetBoolResponse(True, "CSV data publishing stopped.")

    def publish_csv_data(self):
        rate = rospy.Rate(10)  # 10hz

        while self.csv_publishing and not rospy.is_shutdown():
            if not self.service_active:
                break

            with open(self.csv_file, 'r') as csvfile:
                spamreader = csvfile.read().split('\n')
                i = 0

                for row in spamreader:
                    if i < 52:
                        q_set = row.split(',')
                        f = []
                        for item in q_set:
                            f.append(float(item))
                        lp1 = f[0]
                        lp2 = f[1]
                        lp3 = f[2]
                        rp1 = f[3]
                        rp2 = f[4]
                        rp3 = f[5]

                        self.LLINK1.publish(lp1)
                        self.LLINK2.publish(lp2)
                        self.LLINK3.publish(lp3)
                        self.RLINK1.publish(rp1)
                        self.RLINK2.publish(rp2)
                        self.RLINK3.publish(rp3)
                        i = i + 1
                    if i == 52:
                        time.sleep(0.1)
                    time.sleep(0.1)

                rate.sleep()

    def move_to_default_position(self):
        for pos in self.default_positions:
            self.LLINK1.publish(pos)
            self.LLINK2.publish(pos)
            self.LLINK3.publish(pos)
            self.RLINK1.publish(pos)
            self.RLINK2.publish(pos)
            self.RLINK3.publish(pos)
            rospy.sleep(1)
            self.default_positions_published = True

if __name__ == '__main__':
    try:
        CsvControlService()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

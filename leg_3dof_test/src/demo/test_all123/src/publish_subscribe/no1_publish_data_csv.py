#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import Float64
import time
import csv

def csv_publisher():
    LLINK1 = rospy.Publisher('leg_chuanv3/llink1_position/command', Float64, queue_size=10)
    LLINK2 = rospy.Publisher('leg_chuanv3/llink2_position/command', Float64, queue_size=10)
    LLINK3 = rospy.Publisher('leg_chuanv3/llink3_position/command', Float64, queue_size=10)
    RLINK1 = rospy.Publisher('leg_chuanv3/rlink1_position/command', Float64, queue_size=10)
    RLINK2 = rospy.Publisher('leg_chuanv3/rlink2_position/command', Float64, queue_size=10)
    RLINK3 = rospy.Publisher('leg_chuanv3/rlink3_position/command', Float64, queue_size=10)
    
    rospy.init_node('xuat_du_lieu_from_csv', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    
    csv_file = '/home/bien/ROS1/pratice/no1_leg_robot/leg_3dof_test/src/demo/leg_gazebo/scripts/data6.csv'
    
    while not rospy.is_shutdown():
        with open(csv_file, 'r') as csvfile:
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

                    LLINK1.publish(lp1)
                    LLINK2.publish(lp2)
                    LLINK3.publish(lp3)
                    RLINK1.publish(rp1)
                    RLINK2.publish(rp2)
                    RLINK3.publish(rp3)
                    i = i + 1
                if i == 52:
                    time.sleep(0.1)
                time.sleep(0.1)
                
        rate.sleep()

if __name__ == '__main__':
    try:
        csv_publisher()
    except rospy.ROSInterruptException:
        pass

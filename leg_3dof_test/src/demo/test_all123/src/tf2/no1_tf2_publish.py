#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import Float64
import time
import csv
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
import tf_conversions

def csv_publisher():
    LLINK1 = rospy.Publisher('leg_chuanv3/llink1_position/command', Float64, queue_size=10)
    LLINK2 = rospy.Publisher('leg_chuanv3/llink2_position/command', Float64, queue_size=10)
    LLINK3 = rospy.Publisher('leg_chuanv3/llink3_position/command', Float64, queue_size=10)
    RLINK1 = rospy.Publisher('leg_chuanv3/rlink1_position/command', Float64, queue_size=10)
    RLINK2 = rospy.Publisher('leg_chuanv3/rlink2_position/command', Float64, queue_size=10)
    RLINK3 = rospy.Publisher('leg_chuanv3/rlink3_position/command', Float64, queue_size=10)

    # Khởi tạo TransformBroadcaster
    tf_broadcaster = tf2_ros.TransformBroadcaster()
    
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

                    # Tạo và phát thông điệp tf2
                    transformStamped = TransformStamped()
                    transformStamped.header.stamp = rospy.Time.now()
                    transformStamped.header.frame_id = "world"  # Khung tham chiếu gốc
                    transformStamped.child_frame_id = "base_link"  # Khung tham chiếu của robot

                    # Đặt vị trí dữ liệu tương ứng
                    transformStamped.transform.translation.x = lp1
                    transformStamped.transform.translation.y = lp2
                    transformStamped.transform.translation.z = lp3

                    # Thay đổi góc Roll, Pitch, Yaw tương ứng với thực tế
                    roll = 0.0  # Góc Roll (radians)
                    pitch = 0.0  # Góc Pitch (radians)
                    yaw = 0  # Góc Yaw (radians)

                    # Tạo quaternion từ góc Roll, Pitch, Yaw thực tế
                    # quaternion = tf2_geometry_msgs.transformations.quaternion_from_euler(roll, pitch, yaw)
                    quaternion = tf_conversions.transformations.quaternion_from_euler(roll, pitch, yaw)
                    # Đặt quaternion cho transform
                    transformStamped.transform.rotation.x = quaternion[0]
                    transformStamped.transform.rotation.y = quaternion[1]
                    transformStamped.transform.rotation.z = quaternion[2]
                    transformStamped.transform.rotation.w = quaternion[3]

                    # Phát sóng thông điệp tf2
                    tf_broadcaster.sendTransform(transformStamped)
                    
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

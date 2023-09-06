#!/usr/bin/env python
import rospy
import tf2_ros
import geometry_msgs.msg
import tf_conversions

def tf_listener():
    rospy.init_node('tf_listener_from_csv', anonymous=True)
    
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    
    while not rospy.is_shutdown():
        try:
            # Lắng nghe thông điệp TF2 giữa "world" và "base_link"
            transform = tfBuffer.lookup_transform("world", "base_link", rospy.Time())
            
            # Trích xuất vị trí và hướng từ thông điệp TF2
            position = transform.transform.translation
            rotation = transform.transform.rotation
            
            # Hiển thị thông tin vị trí và hướng
            rospy.loginfo("Position: x=%f, y=%f, z=%f", position.x, position.y, position.z)
            rospy.loginfo("Rotation: x=%f, y=%f, z=%f, w=%f \n\n", rotation.x, rotation.y, rotation.z, rotation.w)
            
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            pass
        
        rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        tf_listener()
    except rospy.ROSInterruptException:
        pass

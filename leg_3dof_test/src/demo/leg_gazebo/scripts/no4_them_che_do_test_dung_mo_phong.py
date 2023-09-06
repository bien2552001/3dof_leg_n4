#!/usr/bin/env python
import rospy
import tkinter as tk
from std_msgs.msg import Float64

class DataDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ROS Data Display")

        self.llink1_label = tk.Label(root, text="LLINK1 Data:")
        self.llink1_label.pack()

        self.llink2_label = tk.Label(root, text="LLINK2 Data:")
        self.llink2_label.pack()

        rospy.init_node('data_subscriber', anonymous=True)
        rospy.Subscriber('leg_chuanv3/llink1_position/command', Float64, self.llink1_callback)
        rospy.Subscriber('leg_chuanv3/llink2_position/command', Float64, self.llink2_callback)

    def llink1_callback(self, data):
        self.llink1_label.config(text="LLINK1 Data: {:.2f}".format(data.data))

    def llink2_callback(self, data):
        self.llink2_label.config(text="LLINK2 Data: {:.2f}".format(data.data))

if __name__ == '__main__':
    
    # Kiểm tra kết nối tới ROS Master trước khi tạo giao diện
    try:
        rospy.get_master().getPid()
    except rospy.exceptions.ROSInitException:
        print("Unable to connect to ROS Master. Exiting.")
        exit(1)

    root = tk.Tk()
    app = DataDisplayApp(root)
    root.mainloop()

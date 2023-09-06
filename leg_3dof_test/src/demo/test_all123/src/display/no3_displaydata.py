#!/usr/bin/env python
import rospy
import tkinter as tk
from std_msgs.msg import Float64

class DataDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hien thi goc quay cac khop")

        self.llink1_label = tk.Label(root, text="LLINK1 Data:")
        self.llink1_label.pack()

        self.llink2_label = tk.Label(root, text="LLINK2 Data:")
        self.llink2_label.pack()

        self.llink3_label = tk.Label(root, text="LLINK3 Data:")
        self.llink3_label.pack()

        self.rlink1_label = tk.Label(root, text="RLINK1 Data:")
        self.rlink1_label.pack()

        self.rlink2_label = tk.Label(root, text="RLINK2 Data:")
        self.rlink2_label.pack()

        self.rlink3_label = tk.Label(root, text="RLINK3 Data:")
        self.rlink3_label.pack()
        # Đăng ký để nhận dữ liệu từ các topic tương ứng
        rospy.init_node('hien_thi_du_lieu_csv_no3', anonymous=True)
        rospy.Subscriber('leg_chuanv3/llink1_position/command', Float64, self.llink1_callback)
        rospy.Subscriber('leg_chuanv3/llink2_position/command', Float64, self.llink2_callback)
        rospy.Subscriber('leg_chuanv3/llink3_position/command', Float64, self.llink3_callback)
        rospy.Subscriber('leg_chuanv3/rlink1_position/command', Float64, self.rlink1_callback)
        rospy.Subscriber('leg_chuanv3/rlink2_position/command', Float64, self.rlink2_callback)
        rospy.Subscriber('leg_chuanv3/rlink3_position/command', Float64, self.rlink3_callback)

    def llink1_callback(self, data):
        self.llink1_label.config(text="LLINK1 Data: {:.6f}".format(data.data))

    def llink2_callback(self, data):
        self.llink2_label.config(text="LLINK2 Data: {:.6f}".format(data.data))
    def llink3_callback(self, data):
        self.llink3_label.config(text="LLINK3 Data: {:.6f}".format(data.data))

    def rlink1_callback(self, data):
        self.rlink1_label.config(text="RLINK1 Data: {:.6f}".format(data.data))

    def rlink2_callback(self, data):
        self.rlink2_label.config(text="RLINK2 Data: {:.6f}".format(data.data))

    def rlink3_callback(self, data):
        self.rlink3_label.config(text="RLINK3 Data: {:.6f}".format(data.data))

if __name__ == '__main__':
    root = tk.Tk()
    app = DataDisplayApp(root)
    root.mainloop()

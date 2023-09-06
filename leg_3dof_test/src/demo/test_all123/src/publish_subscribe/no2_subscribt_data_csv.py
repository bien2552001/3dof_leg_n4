#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

class PositionSubscriber:
    def __init__(self):
        self.positions = {}  # Dictionary to store positions for each link

        # List of topic names and their corresponding link names
        self.topic_link_mapping = [
            ('leg_chuanv3/llink1_position/command', 'LLINK1'),
            ('leg_chuanv3/llink2_position/command', 'LLINK2'),
            ('leg_chuanv3/llink3_position/command', 'LLINK3'),
            ('leg_chuanv3/rlink1_position/command', 'RLINK1'),
            ('leg_chuanv3/rlink2_position/command', 'RLINK2'),
            ('leg_chuanv3/rlink3_position/command', 'RLINK3')
        ]

        rospy.init_node('receive_data_from_csv', anonymous=True)
        self.setup_subscribers()
    
    def setup_subscribers(self):
        for topic, link_name in self.topic_link_mapping:
            self.positions[link_name] = None  # Initialize positions
            rospy.Subscriber(topic, Float64, self.callback, callback_args=link_name)
    
    def callback(self, data, link_name):
        self.positions[link_name] = data.data
        # rospy.loginfo("Received data for %s: %f", link_name, data.data)

    def run(self):
        rate = rospy.Rate(10)  # Loop rate (10 Hz)
        while not rospy.is_shutdown():
            # Print positions at each iteration
            rospy.loginfo("Current joints(rad): %s", self.positions)
            rate.sleep()

if __name__ == '__main__':
    try:
        position_subscriber = PositionSubscriber()
        position_subscriber.run()
    except rospy.ROSInterruptException:
        pass

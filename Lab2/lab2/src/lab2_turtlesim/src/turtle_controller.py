#!/usr/bin/env python

import rospy, sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Define the method which contains the node's main functionality
def talker():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk
    topic = sys.argv[1]+"/cmd_vel"
    print(topic)
    pub = rospy.Publisher(topic, Twist, queue_size=10)
    data = Twist()

    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    r = rospy.Rate(10) # 10hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        user_input = input()
        if user_input == "w":  # up key
            data.linear.x = 2
        elif user_input == "s":  # down key
            data.linear.x = -2
        elif user_input == "d":  # right key
            data.angular.z = -2
        elif user_input == "a": # left key
            data.angular.z = 2

     #    # Publish our string to the 'chatter_talk' topic
        pub.publish(data)
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass
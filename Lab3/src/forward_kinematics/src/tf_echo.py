#!/usr/bin/env python
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the dependencies as described in example_pub.py
import rospy, sys
import numpy as np
import tf2_ros
from sensor_msgs.msg import JointState
import example_forward_kinematics as exfk

# Define the method which contains the node's main functionality
def listener(source_frame, target_frame):

    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /chatter_talk.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(target_frame, source_frame, rospy.Time())
            x, y, z = trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z
            print("Translation: [%f, %f, %f]" %(x, y, z))
            q0, q1, q2, q3 = trans.transform.rotation.x, trans.transform.rotation.y, trans.transform.rotation.z, trans.transform.rotation.w
            print("Rotation: in Quaternion [%f, %f, %f, %f]" %(q0, q1, q2, q3))
            phi = np.arctan2(2*(q0*q1+q2*q3), 1-2*(q1**2+q2**2))
            theta = np.arcsin(2*(q0*q2-q3*q1))
            psi = np.arctan2(2*(q0*q3+q1*q2), 1-2*(q2**2+q3**2))
            print("\t in RPY(radian) [%f, %f, %f]" %(phi, theta, psi))
            
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            print("exception occurred")


    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C
    rospy.spin()


# Python's syntax for a main() method
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called
    # /listener_<id>, where <id> is a randomly generated numeric string. This
    # randomly generated name means we can start multiple copies of this node
    # without having multiple nodes with the same name, which ROS doesn't allow.
    # rospy.init_node('turtlebot_controller', anonymous=True)

    
    
    rospy.init_node('listener', anonymous=True)

    tfBuffer = tf2_ros.Buffer()
    tfListener = tf2_ros.TransformListener(tfBuffer)
    # target_frame, source_frame = sys.argv[1], sys.argv[2]
    while not rospy.is_shutdown():
        try:
            listener(sys.argv[1], sys.argv[2])
        except rospy.ROSInterruptException:
            pass
    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C
    rospy.spin()

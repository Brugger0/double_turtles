#!/usr/bin/env python
from __future__ import division
import rospy
from geometry_msgs.msg import Twist, Vector3

QUEUE_SIZE = 10

class VelocityMapping(object):
    def __init__(self):
        rospy.init_node('velocity_mapping')
        rospy.Subscriber('turtle1/cmd_vel', Twist, self.vel_callback)
        self.left_publisher = rospy.Publisher(
            'left/cmd_vel',
            Twist,
            queue_size=QUEUE_SIZE
        )
        self.right_publisher = rospy.Publisher(
            'right/cmd_vel',
            Twist,
            queue_size=QUEUE_SIZE
        )

    def vel_callback(self, data):
        linear_vel = data.linear.x
        angular_vel = data.angular.z

        if (linear_vel != 0):
            # If moving forward or backward, both turtles go together
            self.left_publisher.publish(data)
            self.right_publisher.publish(data)

        if (angular_vel != 0):
            # If changing direction, each turtle rotates in one direction
            # around the center
            left_msg = Twist(
                linear=Vector3(-angular_vel/2, 0, 0),
                angular=Vector3(0, 0, angular_vel)
            )
            right_msg = Twist(
                linear=Vector3(angular_vel/2, 0, 0),
                angular=Vector3(0, 0, angular_vel)
            )
            self.left_publisher.publish(left_msg)
            self.right_publisher.publish(right_msg)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    velocity_mapping_node = VelocityMapping()
    velocity_mapping_node.run()

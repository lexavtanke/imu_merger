#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import String


def run_server():
    global imu_pub_

    rospy.init_node('imu_merger')
    imu_sub_ = rospy.Subscriber('camera/imu', Imu, sub_callback)
    imu_pub_ = rospy.Publisher('imu', Imu, queue_size=10)

    rospy.spin()


def sub_callback(data):
    global imu_pub_

    new_imu = Imu()
    new_imu = data
    new_imu.header.frame_id = "imu_link"
    imu_pub_.publish(new_imu)


if __name__ == '__main__':
    try:
        run_server()
    except rospy.ROSInterruptException:
        pass


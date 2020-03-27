#!/usr/bin/env python
## Node to subscribe to sensor information topic and print distance data.

import rospy
from hrwros_msgs.msg import SensorInformation

# Topic callback function.
def sensorInfoCallback(data):
    rospy.loginfo('Distance reading from the sensor is: %f', data.sensor_data.range)

def sensorInfoListener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'stringListener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sensor_info_subscriber', anonymous=False)

    rospy.Subscriber('sensor_info', SensorInformation, sensorInfoCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    sensorInfoListener()

#!/usr/bin/env python
## Node to subscribe to a string topic.

import rospy
from std_msgs.msg import String

# Topic callback function.
def stringListenerCallback(data):
    rospy.loginfo('%s', data.data)

def stringListener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'stringListener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('node_2', anonymous=False)

    rospy.Subscriber('topic_1', String, stringListenerCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    stringListener()

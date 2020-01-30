#!/usr/bin/env python

import rospy
import geometry_msgs
import ublox

class liveGraph:
    def __init__(self):
        topic = rospy.get_param('topic')
        self.topicSub = rospy.Subscriber(topic, geometry_msgs.msg.PoseStamped)

    def topicCB(self, msg, cb_args=None):
        print(msg.position+"\n")

if __name__ == '__main__':
    thing = liveGraph()

    rospy.spin()

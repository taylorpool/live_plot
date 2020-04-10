#!/usr/bin/env python
import rospy
import geometry_msgs.msg as gm
#from importlib import reload
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ublox.msg as um

class liveGraph():
    def __init__(self):
        rospy.init_node('live_plot')
        self.r_x = 0
        self.r_y = 0
        self.r_z = 0

        self.rtk_x = 0
        self.rtk_y = 0
        self.rtk_z = 0
        
        self.xmin = -2
        self.xmax = 2
        self.ymin = -2
        self.ymax = 2

        self.plot_update_interval = 1
        self.fig = plt.figure(figsize =[9,9])
        self.ax1 = self.fig.add_subplot(1,1,1, projection='3d')
        topic = rospy.get_param('/plotter/plot/topic')
        rtk_topic = rospy.get_param('/plotter/plot/rtk_topic')
        self.topicSub = rospy.Subscriber(topic, gm.PoseStamped, callback=self.topicCB)
        self.rtkSub = rospy.Subscriber(rtk_topic, um.RelPos, callback=self.rtkCB)
        self.ani = animation.FuncAnimation(self.fig, self.plot_data, interval=self.plot_update_interval)

        plt.show()

    def plot_data(self, i):
        #print("plot_data")
        self.ax1.plot([self.r_x], [self.r_y], 'r*', zs=self.r_z)
        self.ax1.plot([self.rtk_x], [self.rtk_y], 'b*', zs=self.rtk_z)
        self.ax1.set_ylim(self.ymin, self.ymax)
        self.ax1.set_xlim(self.xmin, self.xmax)
        self.ax1.set_zlim(-2, 2)

    def rtkCB(self, msg, cb_args=None):

        self.rtk_x=msg.relPosNED[0]
        self.rtk_y=msg.relPosNED[1]
        self.rtk_z=msg.relPosNED[2]


    def topicCB(self, msg, cb_args=None):
        #print('topicCB')
        #print(msg.pose.position)
        self.r_x = msg.pose.position.x
        self.r_y = msg.pose.position.y
        self.r_z = msg.pose.position.z

if __name__ == '__main__':

    thing = liveGraph()

    rospy.spin()

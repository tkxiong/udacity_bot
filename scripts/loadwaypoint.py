#!/usr/bin/env python
import rospy

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped

path = Path()
path.header.frame_id = 'map'

def loadWayPoints(textfile):
    f = open(textfile)
    for line in f:
        x, y = line.split(',')
        pose = PoseStamped()
        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        path.poses.append(pose)
    path.header.stamp = rospy.Time.now()
    path_pub.publish(path)

rospy.init_node('waypoint_node')

path_pub = rospy.Publisher('/amcl_path', Path, queue_size=10, latch=True)
path.header.frame_id = 'map'

if __name__ == '__main__':
    loadWayPoints('waypoints.txt')
    rospy.spin()
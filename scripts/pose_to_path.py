#!/usr/bin/env python
import rospy

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped

path = Path()
#path_file = open("waypoints.txt", "a")

def pose_cb(data):
    global path
    path.header = data.header
    pose = PoseWithCovarianceStamped()
    pose.header = data.header
    pose.pose = data.pose.pose
    #path_file.write(str(pose.pose.position.x) + ',' + str(pose.pose.position.y) + '\n')
    path.poses.append(pose)
    path_pub.publish(path)

rospy.init_node('path_node')

pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_cb)
path_pub = rospy.Publisher('/amcl_path', Path, queue_size=10)

if __name__ == '__main__':
    rospy.spin()
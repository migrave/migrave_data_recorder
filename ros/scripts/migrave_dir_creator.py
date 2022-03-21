#!/usr/bin/env python3

import rospy
import os

if __name__ == "__main__":
    rospy.init_node("migrave_directory_creator", anonymous=True)
    node_name = rospy.get_name()
    path = rospy.get_param(node_name+'/output_directory', "/home/qtrobot/1")
    directories_list = rospy.get_param(node_name+'/directories_list', "video,audio,rosbag")
    
    for directory in directories_list.split(','):
        try:
            dir_path = os.path.join(path, directory)
            os.makedirs(dir_path)
        except FileExistsError as err:
            print(f"WARNING: Directory {dir_path} already exists")

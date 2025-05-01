from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='my_py_nodes', executable='talker_py',   name='talker'),
        Node(package='demo_nodes_py', executable='listener',  name='listener'),
    ])

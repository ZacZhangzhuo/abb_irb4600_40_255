
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

#TODO ZAC to do

  

    urdf_file_name = 'urdf/abb_irb4600_40_255.urdf'
    urdf = os.path.join(
        get_package_share_directory('abb_irb4600_40_255'),
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    rviz_file_name = 'rviz/urdf.rviz'
    rviz = os.path.join(
        get_package_share_directory('abb_irb4600_40_255'),
        rviz_file_name)
    with open(rviz, 'r') as r:
        rviz_desc = r.read()



    # model_path = launch.substitutions.LaunchConfiguration('model', default=robot_desc)

    gui = launch.substitutions.LaunchConfiguration('gui', default='true')


    # rvizconfig_path = launch.substitutions.LaunchConfiguration('rvizconfig', default='rviz/urdf.rviz')

    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}]
    )

    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_desc],
        parameters=[{'use_gui': gui}]
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('model', default_value=robot_desc),
        launch.actions.DeclareLaunchArgument('gui', default_value=gui),
        launch.actions.DeclareLaunchArgument('rvizconfig', default_value=rviz_desc),
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ])


if __name__ == '__main__':
    generate_launch_description()

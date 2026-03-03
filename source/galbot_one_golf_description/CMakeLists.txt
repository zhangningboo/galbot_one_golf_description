cmake_minimum_required(VERSION 3.0.2)
project(galbot_one_golf_description)

find_package(catkin REQUIRED COMPONENTS
  robot_state_publisher
  urdf
  xacro
  roslaunch
  rospy
  tf2_ros
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

install(DIRECTORY config launch meshes tools xacro 
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(FILES 
  # galbot_one_golf_head.srdf galbot_one_golf_head.urdf 
  # galbot_one_golf_left_arm.srdf galbot_one_golf_left_arm.urdf 
  # galbot_one_golf_right_arm.srdf galbot_one_golf_right_arm.urdf 
  # galbot_one_golf_leg.srdf galbot_one_golf_leg.urdf 
  galbot_one_golf.srdf galbot_one_golf.urdf galbot_one_golf_cali.urdf 
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

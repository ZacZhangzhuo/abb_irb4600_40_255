cmake_minimum_required(VERSION 3.22)
project(abb_irb4600_40_255)

find_package(ament_cmake REQUIRED)

ament_package()

install(DIRECTORY rviz urdf meshes launch DESTINATION share/${PROJECT_NAME})


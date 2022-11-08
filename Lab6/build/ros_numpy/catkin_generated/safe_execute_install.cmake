execute_process(COMMAND "/home/cc/ee106a/fa22/class/ee106a-aai/ros_workspaces/106a-fa22-labs-starter/Lab6/build/ros_numpy/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/cc/ee106a/fa22/class/ee106a-aai/ros_workspaces/106a-fa22-labs-starter/Lab6/build/ros_numpy/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

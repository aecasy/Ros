# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build

# Include any dependencies generated for this target.
include client_src/CMakeFiles/testSharedObject.dir/depend.make

# Include the progress variables for this target.
include client_src/CMakeFiles/testSharedObject.dir/progress.make

# Include the compile flags for this target's objects.
include client_src/CMakeFiles/testSharedObject.dir/flags.make

client_src/CMakeFiles/testSharedObject.dir/testSharedObject.C.o: client_src/CMakeFiles/testSharedObject.dir/flags.make
client_src/CMakeFiles/testSharedObject.dir/testSharedObject.C.o: /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/testSharedObject.C
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object client_src/CMakeFiles/testSharedObject.dir/testSharedObject.C.o"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/testSharedObject.dir/testSharedObject.C.o -c /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/testSharedObject.C

client_src/CMakeFiles/testSharedObject.dir/testSharedObject.C.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/testSharedObject.dir/testSharedObject.C.i"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/testSharedObject.C > CMakeFiles/testSharedObject.dir/testSharedObject.C.i

client_src/CMakeFiles/testSharedObject.dir/testSharedObject.C.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/testSharedObject.dir/testSharedObject.C.s"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/testSharedObject.C -o CMakeFiles/testSharedObject.dir/testSharedObject.C.s

# Object files for target testSharedObject
testSharedObject_OBJECTS = \
"CMakeFiles/testSharedObject.dir/testSharedObject.C.o"

# External object files for target testSharedObject
testSharedObject_EXTERNAL_OBJECTS =

client_src/testSharedObject: client_src/CMakeFiles/testSharedObject.dir/testSharedObject.C.o
client_src/testSharedObject: client_src/CMakeFiles/testSharedObject.dir/build.make
client_src/testSharedObject: libvrpn.a
client_src/testSharedObject: quat/libquat.a
client_src/testSharedObject: client_src/CMakeFiles/testSharedObject.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable testSharedObject"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/testSharedObject.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
client_src/CMakeFiles/testSharedObject.dir/build: client_src/testSharedObject

.PHONY : client_src/CMakeFiles/testSharedObject.dir/build

client_src/CMakeFiles/testSharedObject.dir/clean:
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && $(CMAKE_COMMAND) -P CMakeFiles/testSharedObject.dir/cmake_clean.cmake
.PHONY : client_src/CMakeFiles/testSharedObject.dir/clean

client_src/CMakeFiles/testSharedObject.dir/depend:
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src/CMakeFiles/testSharedObject.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : client_src/CMakeFiles/testSharedObject.dir/depend


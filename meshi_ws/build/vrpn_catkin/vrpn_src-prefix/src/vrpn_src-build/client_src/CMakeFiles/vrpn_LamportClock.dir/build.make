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
include client_src/CMakeFiles/vrpn_LamportClock.dir/depend.make

# Include the progress variables for this target.
include client_src/CMakeFiles/vrpn_LamportClock.dir/progress.make

# Include the compile flags for this target's objects.
include client_src/CMakeFiles/vrpn_LamportClock.dir/flags.make

client_src/CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.o: client_src/CMakeFiles/vrpn_LamportClock.dir/flags.make
client_src/CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.o: /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/vrpn_LamportClock.t.C
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object client_src/CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.o"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.o -c /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/vrpn_LamportClock.t.C

client_src/CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.i"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/vrpn_LamportClock.t.C > CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.i

client_src/CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.s"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src/vrpn_LamportClock.t.C -o CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.s

# Object files for target vrpn_LamportClock
vrpn_LamportClock_OBJECTS = \
"CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.o"

# External object files for target vrpn_LamportClock
vrpn_LamportClock_EXTERNAL_OBJECTS =

client_src/vrpn_LamportClock: client_src/CMakeFiles/vrpn_LamportClock.dir/vrpn_LamportClock.t.C.o
client_src/vrpn_LamportClock: client_src/CMakeFiles/vrpn_LamportClock.dir/build.make
client_src/vrpn_LamportClock: libvrpn.a
client_src/vrpn_LamportClock: quat/libquat.a
client_src/vrpn_LamportClock: client_src/CMakeFiles/vrpn_LamportClock.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable vrpn_LamportClock"
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/vrpn_LamportClock.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
client_src/CMakeFiles/vrpn_LamportClock.dir/build: client_src/vrpn_LamportClock

.PHONY : client_src/CMakeFiles/vrpn_LamportClock.dir/build

client_src/CMakeFiles/vrpn_LamportClock.dir/clean:
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src && $(CMAKE_COMMAND) -P CMakeFiles/vrpn_LamportClock.dir/cmake_clean.cmake
.PHONY : client_src/CMakeFiles/vrpn_LamportClock.dir/clean

client_src/CMakeFiles/vrpn_LamportClock.dir/depend:
	cd /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src/client_src /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src /home/meshib/meshi_ws/build/vrpn_catkin/vrpn_src-prefix/src/vrpn_src-build/client_src/CMakeFiles/vrpn_LamportClock.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : client_src/CMakeFiles/vrpn_LamportClock.dir/depend

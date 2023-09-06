# Mo ta
- **Moveit1: chan robot voi tu the cai dat san.**
- _Hien tai 2 chan chua chay bat dong bo duoc_
# Demo 
https://github.com/bien2552001/day_05_09_2023/assets/128835452/aecab23f-0d83-4aff-a1af-fcf707c19ad1

# Run
### _**Download moveit1 va thiet lap workspace:**_
- ```https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html#create-a-catkin-workspace```
### _**Run source:**_
- ```source /opt/ros/noetic/setup.bash```
- ```cd ~/.../src```
- ```rosdep install -y --from-paths . --ignore-src --rosdistro noetic```
- ```cd ..```
- ```catkin config --extend /opt/ros/${ROS_DISTRO} --cmake-args -DCMAKE_BUILD_TYPE=Release```
- ```catkin build```
- ```source devel/setup.bash```
- ```roslaunch moveit_v6 demo.launch```
- _**New terminal**_
- ```source /opt/ros/noetic/setup.bash```
- ```source devel/setup.bash```
- ```roslaunch demo_trajectory trajectory_unlimit.launch```

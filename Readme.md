S4479444 - Emanuele Giordano
########## ASSIGNMENT 2 - RESEARCH TRACK 1 - 2022 ############

# Professor. [Carmine Recchiuto](https://github.com/CarmineD8)


The task of this assignment was to implement three nodes in the robot simulation presented in the course.
The three nodes are described as following:

1) Action Client node, allowing the user to set a target position (x, y) or to cancel it;
2) Service node, that prints the number of objectives, both reached and canceled after the user's request;
3) A node that subscribes to the robot's odometry, and prints the distance from target, as well as the average velocity.

It is also required to create a launch file to start the simulation (rt1_second_assignment.launch).

########## INSTALLATION ###########

Run the following command from the shell:
```bash
$ git clone https://github.com/CarmineD8/assignment_2_2022.git
```
```bash
$ git clone https://github.com/S4479444/rt1_second_assignment.git
```
Just for be prudent , it is recommended to run the following commands if a build in the catkin workspace was done beforehand:

```bash
$ sudo rm -rf devel/
$ sudo rm -rf build/
```

Then, run:

```bash
$ catkin_make 
```
If not installed, install Konsole:
```bash
$ sudo apt-get install konsole
```

Finally, the final steps are the following:

```bash
$ sudo bash run_project.sh #inside the directory of the project.
```

######## LAUNCHING ##########

The program will open five windows:

- *Gazebo*: A 3D visualization setup will be used to depict the arena and the robot.
- *Rviz*: a ROS visualization tool is employed for robot debugging and the development of new features.
- *sub_pos.py*: the display window where mesuarment about the robot will be printed .
- *action_client.py*: twindow through which a user can enter a goal or cancel it.


######## FLOWCHART ##########

#<img src="https://github.com/Ep3896/Second-assignment/blob/main/Enrico_Piacenti_Second_Assignment_RT/image/Flowchart_Second_Assignment.png" />




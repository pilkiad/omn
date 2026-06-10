# OMN

> "Omar macht Navigation" - alle, außer Omar

## Connect to the turtle

According to [this tutorial](https://github.com/fkenghagho/rpwr-assignments/blob/main/project/RPWR_internship_01_Setup.md).

First log into the WIFI `lispcourse` with password `turtlesalltheway`.

Then connect to the turtle using:

```shell
ssh roscourse@10.0.1.35
byobu
```

And upload files using:

```shell
scp -r /directory roscourse@10.0.1.35:~/Documents/
```

Start roboclaw for movement:

```shell
ros2 launch roboclaw_node roboclaw_launch.py
ros2 launch urg_node2 urg_node2.launch.py
ros2 run topic_tools throttle messages /scan 10.0
```

## Record data

Record specific topis:
```shell
ros2 bag record --topics /topic1 /topic2
```

Record all data on all topics:
```shell
ros2 bag record -a
```

## Playback data

```shell
ros2 bag play data/BAG_NAME/ -l --clock
```

And start RVIZ2:

```shell
rviz2 --ros-args -p use_sim_time:=true
```

Remember to set

- global frame to `laser`
- reliability to `best effort`
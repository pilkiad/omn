# OMN

> "Omar macht Navigation" - alle, außer Omar

## Connect to the turtle

According to [this tutorial](https://github.com/fkenghagho/rpwr-assignments/blob/main/project/RPWR_internship_01_Setup.md).

First log into the WIFI `lispcourse` with password `turtlesalltheway`.

Then connect to the turtle using:

´´´shell
ssh roscourse@10.0.1.35
byobu
´´´

And upload files using:

´´´shell
scp -r /directory roscourse@10.0.1.35:~/Documents/
´´´

## Record data

Record specific topis:
´´´shell
ros2 bag record --topics /topic1 /topic2
´´´

Record all data on all topics:
´´´shell
ros2 bag record -a
´´´

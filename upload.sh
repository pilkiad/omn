# Will upload local ros_ws to turtlebot ~/Documents/
rm -rf ros_ws/build ros_ws/log ros_ws/install
scp -r ./ros_ws/src/navigation/navigation roscourse@10.0.1.35:/home/roscourse/Documents/

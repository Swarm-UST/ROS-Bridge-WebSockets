## ROSBridge-Websockets
---

This repo illustrates how to subscribe to topics and request service from server on a non-ROS client by using [rosbridge_suites](http://ros.org/wiki/rosbridge_suite) and [roslibpy](https://github.com/gramaziokohler/roslibpy).

With the two scripts under the [client](./client) folder, non-ROS clients can echo `\turtle\pose` and request to clean the trajectory of the turtle.

### Dependencies

- [rosbridge_suites](http://ros.org/wiki/rosbridge_suite) - A JSON interface to ROS, allowing the communication between ROS and non-ROS clients through TCP or WebSockets.

- [roslibpy](https://github.com/gramaziokohler/roslibpy) - A Python API, which communicates with rosbridge over WebSockets.

### Protocol

For information on the protocol itself, please refer to the [rosbridge protocol](https://github.com/RobotWebTools/rosbridge_suite/blob/develop/ROSBRIDGE_PROTOCOL.md).

### Usage

#### Installation - Server side

```
export ROS_DISTRO=melodic               # Set this to your distro, e.g. kinetic or melodic
source /opt/ros/$ROS_DISTRO/setup.bash  # Source your ROS distro 
mkdir -p ~/catkin_ws/src                # Make a new workspace 
cd ~/catkin_ws/src                      # Navigate to the source space
git clone <$REPO_URL>                   # Clone this repo. Please replace <$REPO_URL> with the real URL
cd ~/catkin_ws                          # Navigate to the workspace
rosdep install --from-paths src --ignore-src -r -y  # Install any missing packages
catkin_make                             # Build packages
source ./devel/setup.sh                 # set up env
```
#### Installation - Client side

with pip3 for python 3
```
pip3 install roslibpy
```
#### Starting ROSBridge server and turtlesim

```
roslaunch ros_tcp_server startRosServer.launch [port:=1234]
```
The argument `port` is optional, you can specify the WebSockets port by passing it to roslaunch.

#### Subscribing to `\turtle\pose`

> Attention: Please set the `url` and `port` inside the `config.ini` correctly before running the scripts. 

> Attention: `roscd` is necessary. Please run the scripts under the same folder as the `config.ini`. Otherwise, the interpreter is not able to resolve the path of `config.ini`.

```
roscd ros_tcp_server/../client
python3 topic_echo.py
```

#### Using services - Request ro clear the trajectory

```
python service_request.py
```

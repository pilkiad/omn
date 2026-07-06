---
title: "Ensuring security across machines"
docname: "Tutorials/Advanced/Security/Security-on-Two"
source: "Tutorials/Advanced/Security/Security-on-Two.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../../intermediate/tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../../intermediate/tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../../intermediate/urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../../intermediate/urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../../intermediate/urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="ensuring-security-across-machines"></a>
<a id="security-on-two"></a>

# Ensuring security across machines

**Goal:** Make two different machines communicate securely.

**Tutorial level:** Advanced

**Time:** 5 minutes

Contents

- [Background](#background)
- [Create the second keystore](#create-the-second-keystore)
- [Copy files](#copy-files)
- [Launch the nodes](#launch-the-nodes)

<a id="background"></a>

## Background

Before proceeding ensure you have completed the [Setting up security](introducing-ros2-security.md) tutorial.

The previous tutorials have used two ROS nodes on the same machine sending all network communications over the localhost interface.
Let’s extend that scenario to involve multiple machines, since the benefits of authentication and encryption then become more obvious.

Suppose that the machine with the keystore created in the previous demo has a hostname `Alice`, and that we want to also use another machine with hostname `Bob` for our multi-machine `talker/listener` demo.
We need to move some keys from `Alice` to `Bob` to allow SROS 2 to authenticate and encrypt the transmissions.

<a id="create-the-second-keystore"></a>

## Create the second keystore

Begin by creating an empty keystore on `Bob`; the keystore is actually just an empty directory:

Linux

```
$ ssh Bob
$ mkdir ~/sros2_demo
$ exit
```

MacOS

```
$ ssh Bob
$ mkdir ~/sros2_demo
$ exit
```

Windows

```
$ ssh Bob
$ md C:\dev\ros2\sros2_demo
$ exit
```

<a id="copy-files"></a>

## Copy files

Next copy the keys and certificates for the `talker` program from `Alice` to `Bob`.
Since the keys are just text files, we can use `scp` to copy them.

Linux

```
$ cd ~/sros2_demo/demo_keystore
$ scp -r talker USERNAME@Bob:~/sros2_demo/demo_keystore
```

MacOS

```
$ cd ~/sros2_demo/demo_keystore
$ scp -r talker USERNAME@Bob:~/sros2_demo/demo_keystore
```

Windows

```
$ cd C:\dev\ros2\sros2_demo\demo_keystore
$ scp -r talker USERNAME@Bob:/dev/ros2/sros2_demo/demo_keystore
```

> [!WARNING]
>
> Note that in this case the entire keystore is shared across the different machines which may not be the desired behavior, as it may result in a security risk.
> Please refer to [Deployment Guidelines](deployment-guidelines.md) for more information in this regard.

That will be very quick, since it’s just copying some very small text files.
Now, we’re ready to run a multi-machine talker/listener demo!

<a id="launch-the-nodes"></a>

## Launch the nodes

Once the environment is set up, run the talker on `Bob`:

```
$ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker
```

and launch the listener on `Alice`:

```
$ ros2 run demo_nodes_py listener --ros-args --enclave /talker_listener/listener
```

Alice will now be receiving encrypted messages from Bob.

With two machines successfully communicating using both encryption and authentication, you can use the same procedure to add more machines to your ROS graph.

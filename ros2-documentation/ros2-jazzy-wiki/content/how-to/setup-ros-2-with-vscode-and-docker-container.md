---
title: "Setup ROS 2 with VSCode and Docker [community-contributed]"
docname: "How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container"
source: "How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="setup-ros-2-with-vscode-and-docker-community-contributed"></a>

# Setup ROS 2 with VSCode and Docker [community-contributed]

Contents

- [Install VS Code and Docker](#install-vs-code-and-docker)

  - [Install Docker](#install-docker)
  - [Install VS Code](#install-vs-code)
  - [Install Remote Development Extension](#install-remote-development-extension)
- [Configure workspace in Docker and VS Code](#configure-workspace-in-docker-and-vs-code)

  - [Add your ROS 2 workspace](#add-your-ros-2-workspace)
  - [Edit `devcontainer.json` for your environment](#edit-devcontainer-json-for-your-environment)
  - [Edit `Dockerfile`](#edit-dockerfile)
- [Open and Build Development Container](#open-and-build-development-container)

  - [Test Container](#test-container)

<a id="install-vs-code-and-docker"></a>

## Install VS Code and Docker

Using Visual Studio Code and Docker Containers will enable you to run your favorite ROS 2 Distribution without the necessity to change your operating system or use a virtual machine.
With this tutorial you can set up a docker container, which can be used for your future ROS 2 projects.

<a id="install-docker"></a>

### Install Docker

To install docker and set the correct user rights please use the following commands.

```
$ sudo apt install docker.io git python3-pip
$ pip3 install vcstool
$ echo export PATH=$HOME/.local/bin:$PATH >> ~/.bashrc
$ source ~/.bashrc
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
```

Now you can check if the installation was successful by running the following command:

```
$ docker run hello-world
```

You might need to start the Docker Daemon first, if you cannot run hello-world out of the box:

```
$ sudo systemctl start docker
```

<a id="install-vs-code"></a>

### Install VS Code

To install VS Code please use the following commands:

```
$ sudo apt update
$ sudo apt install software-properties-common apt-transport-https wget -y
$ wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
$ sudo apt install code
```

You can run VS Code by typing `code` in a terminal.

<a id="install-remote-development-extension"></a>

### Install Remote Development Extension

Within VS Code search in Extensions (CTRL+SHIFT+X) for the “Remote Development” Extension and install it.

<a id="configure-workspace-in-docker-and-vs-code"></a>

## Configure workspace in Docker and VS Code

<a id="add-your-ros-2-workspace"></a>

### Add your ROS 2 workspace

Add a workspace in order to build and open them in a container, e.g.:

```
$ cd ~/
$ mkdir ws
$ cd ws
$ mkdir src
```

Now create a `.devcontainer` folder in the root of your workspace and add a `devcontainer.json` and `Dockerfile` to this `.devcontainer` folder.
The workspace structure should look like this:

```
ws
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── src
    ├── package1
    └── package2
```

With `File->Open Folder...` or `Ctrl+K Ctrl+O`, open the `ws` folder of your workspace in VS Code.

<a id="edit-devcontainer-json-for-your-environment"></a>

### Edit `devcontainer.json` for your environment

For the Dev Container to function properly, we have to build it with the correct user.
Therefore add the following to `.devcontainer/devcontainer.json`:

```
{
    "name": "ROS 2 Development Container",
    "privileged": true,
    "remoteUser": "YOUR_USERNAME",
    "build": {
        "dockerfile": "Dockerfile",
        "args": {
            "USERNAME": "YOUR_USERNAME"
        }
    },
    "workspaceFolder": "/home/ws",
    "workspaceMount": "source=${localWorkspaceFolder},target=/home/ws,type=bind",
    "customizations": {
        "vscode": {
            "extensions":[
                "ms-vscode.cpptools",
                "ms-vscode.cpptools-themes",
                "twxs.cmake",
                "donjayamanne.python-extension-pack",
                "eamodio.gitlens",
                "ms-iot.vscode-ros"
            ]
        }
    },
    "containerEnv": {
        "DISPLAY": "unix:0",
        "ROS_AUTOMATIC_DISCOVERY_RANGE": "LOCALHOST",
        "ROS_DOMAIN_ID": "42"
    },
    "runArgs": [
        "--net=host",
        "--pid=host",
        "--ipc=host",
        "-e", "DISPLAY=${env:DISPLAY}"
    ],
    "mounts": [
       "source=/tmp/.X11-unix,target=/tmp/.X11-unix,type=bind,consistency=cached",
       "source=/dev/dri,target=/dev/dri,type=bind,consistency=cached"
    ],
    "postCreateCommand": "sudo rosdep update && sudo rosdep install --from-paths src --ignore-src -y && sudo chown -R $(whoami) /home/ws/"
}
```

Use `Ctrl+F` to open the search and replace menu.
Search for `YOUR_USERNAME` and replace it with your `Linux username`.
If you do not know your username, you can find it by running `echo $USERNAME` in the terminal.

<a id="edit-dockerfile"></a>

### Edit `Dockerfile`

Open the Dockerfile and add the following contents:

```
FROM ros:ROS_DISTRO
ARG USERNAME=USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip
ENV SHELL /bin/bash

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME
CMD ["/bin/bash"]
```

Replace `ROS_DISTRO` with the ROS 2 distribution you wish to use as base image above, for example `rolling`.

<a id="open-and-build-development-container"></a>

## Open and Build Development Container

Use `View->Command Palette...` or `Ctrl+Shift+P` to open the command palette.
Search for the command `Dev Containers: Reopen in Container` and execute it.
This will build your development docker container for your.
It will take a while - sit back or go for a coffee.

<a id="test-container"></a>

### Test Container

To test if everything worked correctly, open a terminal in the container using `View->Terminal` or `` Ctrl+Shift+` `` and `New Terminal` in VS Code.
Inside the terminal do the following:

```
$ sudo apt install ros-$ROS_DISTRO-rviz2 -y
$ source /opt/ros/$ROS_DISTRO/setup.bash
$ rviz2
```

> [!NOTE]
>
> There might be a problem with displaying RVIZ.
> Please make sure to allow the user to access X window system with `xhost +local:<USERNAME>`.
> If no window still pops up, then check the value of `echo $DISPLAY` - if the output is 1, you can fix this problem with `echo "export DISPLAY=unix:1" >> /etc/bash.bashrc` and then test it again.
> You can also change the DISPLAY value in the devcontainer.json and rebuild it.

---
title: "IDEs and Debugging [community-contributed]"
docname: "How-To-Guides/ROS-2-IDEs"
source: "How-To-Guides/ROS-2-IDEs.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [How-To Guides hub](../../wiki/task-map.md)
> Related: [ament_cmake user documentation](ament-cmake-documentation.md) | [ament_cmake_python user documentation](ament-cmake-python-documentation.md) | [Building a custom deb package](building-a-custom-deb-package.md) | [Building ROS 2 with tracing](building-ros-2-with-tracing.md) | [Configure Zero Copy Loaned Messages](configure-zero-copy-loaned-messages.md)

<a id="ides-and-debugging-community-contributed"></a>

# IDEs and Debugging [community-contributed]

ROS 2 is not made around a specific development environment and the main focus is on building / running from the command line.
Nonetheless Integrated Development Environments (IDEs) can be used to develop, run and/or debug ROS 2 nodes.

Below are listed some IDEs and instructions on how to use them with ROS 2.

Contents

- [General](#general)

  - [Installed Python Code](#installed-python-code)
- [Visual Studio Code](#visual-studio-code)

  - [Python](#python)
- [PyCharm](#pycharm)

  - [Integrate for code inspection](#integrate-for-code-inspection)
  - [Attach to Process](#attach-to-process)
  - [Run/Debug](#run-debug)

<a id="general"></a>

## General

<a id="installed-python-code"></a>
<a id="installedpythoncode"></a>

### Installed Python Code

By default, when building workspaces with:

```
$ colcon build
```

The Python code will be coped over into the `build`/`install` directories.
So when attaching a debugger to a `ros2 run` command from within an IDE, the code being run (from the `build`/`install`) is not the same as the files opened in the IDE project.

There are 2 options to deal with this:

- Open the source files from `build`/`install` directory and place breakpoints there.
- Build the workspace with the [–symlink-install](https://colcon.readthedocs.io/en/released/reference/verb/build.html#command-line-arguments) flag to colcon, which will symlink the source files to the `build`/`install` directory instead.

<a id="visual-studio-code"></a>

## Visual Studio Code

[VSCode](https://code.visualstudio.com/) is a versatile and free development environment.

VSCode is relatively easy to use with ROS 2.
Simply activate your environment in a command line and start the VSCode application from the same terminal and use as normal.
So:

1. Create your ROS workspace as you would normally.
2. In a terminal, source both ROS 2 and your install (if it was built already).
3. Start VSCode from the same command line.
   The terminal will be blocked until the application is closed again.

Linux

```
$ source /opt/ros/jazzy/setup.bash
$ cd ~/dev_ws
$ source ./install/setup.bash
$ /usr/bin/code ./src/my_node/
```

macOS

```
$ . ~/ros2_install/ros2-osx/setup.bash
$ cd ~/dev_ws
$ . ./install/setup.bash
$ /Applications/Visual Studio Code.app/Contents/Resources/app/bin/code ./src/my_node/
```

Windows

In a Windows command line interface:

```
$ call C:\dev\ros2\local_setup.bat
$ cd C:\dev_ws
$ call .\install\local_setup.bat
$ "C:\Program Files\Microsoft VS Code\Code.exe" .\src\my_node\
```

Or in powershell:

```
$ C:\dev\ros2\local_setup.ps1
$ cd C:\dev_ws
$ .\install\local_setup.ps1
$ & "C:\Program Files\Microsoft VS Code\Code.exe" .\src\my_node\
```

VSCode and any terminal created inside VSCode will correctly inherit from the parent environment and should have ROS and installed package available.

> [!NOTE]
>
> After adding packages or making major changes you might need to source your install again.
> The simplest way to do this is to close VSCode and restart it as above.

<a id="python"></a>

### Python

In your workspace, verify the correct interpreter is used.
Through sourcing the basic command `python` should be correct, but VSCode likes to resort to an absolute path for Python.
In the bottom right corner click on “Selected Python Interpreter” to change it.

If your ROS 2 Python version is from a virtual environment, VSCode will try to source it at each run command.
But we already started VSCode from a sourced environment, so this extra step is not necessary.
You can disable this for the current workspace by finding “Settings” > “Extensions” > “Python” > “Activate Environment” and disabling the check.

Now simply run a file or create a configuration in `launch.json`.
Debugging a node is easiest by creating a configuration like a `python ...` command, instead of `ros2 run/launch ...`.
An example of `launch.json` could be:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: File",
            "type": "python",
            "request": "launch",
            "program": "my_node.py"
        },
    ]
}
```

Instead you could also create a configuration for attaching to a running process, under “Attach using Process Id”.

See [Setup ROS 2 with VSCode and Docker](setup-ros-2-with-vscode-and-docker-container.md) for full instructions on how to use VSCode, in combination with Docker.

<a id="pycharm"></a>

## PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/) is an IDE specifically for Python.

Of course it can only be meaningfully used for nodes made in Python.

With PyCharm you can either attach to an existing process (probably started by you via `ros2 run ...` or `ros2 launch ...`) or run the node directly from Python (equivalent to `python [file.py]`.

<a id="integrate-for-code-inspection"></a>

### Integrate for code inspection

You can setup your PyCharm project such that it is fully aware of ROS 2 code, allowing code completion and suggestion.

<a id="linux"></a>

#### Linux

Open a terminal, source ROS and start PyCharm:

```
$ source /opt/ros/humble/setup.bash
$ cd path/to/dev_ws
$ /opt/pycharm/bin/pycharm.sh
```

After selecting the correct interpreter, everything should work.

> [!NOTE]
>
> This is untested.

<a id="windows"></a>

#### Windows

First sourcing ROS and then starting PyCharm from the command line seems to have no effect on Windows.
Instead, some settings need to be tweaked.

1. Create your ROS workspace as you would normally.
2. Start PyCharm normally.
3. Open a project.
   This should be the root directory of the ROS node you’re developing, e.g. `C:\dev_ws\src\my_node`.
4. Click “Add new interpreter” > “Add local interpreter…”.
   Select a system interpreter (or virtual environment if you’re using one) and select the executable of your ROS Python version (typically `C:\Python38\python.exe`).

   > - If you now open one of your code files, you will see warnings about missing imports.
   >   Trying to run the file will confirm these issues.
5. Under the “Python Interpreters” window, find and select your ROS interpreter.
   Edit the name to something recognizable.
   More importantly, now click the “Show Interpreter Paths” button.
6. In the new window, you will see the paths already associated with this interpreter.
   Click the “+” button and add two more paths (according to your ROS install):

   > - `C:\dev\ros2_humble\bin`
   > - `C:\dev\ros2_humble\Lib\site-packages`

PyCharm will re-index and when finished it should correctly interpret your project, recognising the ROS 2 system packages.
You can navigate through code, get completion and read doc blurbs as expected.

If there are dependencies built alongside with your package, they are probably not yet recognized and result in invalid IDE warnings and runtime errors.

Resolve this by:

- Making sure the `PATH` override in the run/debug configuration includes both the ROS 2 install and your workspace, e.g.:

  ```
  $ C:\dev\ros2_humble\local_setup.ps1
  $ C:\dev_ws\install\local_setup.ps1
  $ echo $ENV:Path
  ```
- Adding the relevant folders from the `install/` directory to your project sources.

  Go to “Settings…” and under “Project: “ > “Project Structure” click “Add content root”.
  Add all the relevant `site-packages` folders under `install/Lib/*`.

  Finally, make sure your run/debug configuration has the option “include content roots in PYTHONPATH” enabled.

> [!TIP]
>
> Using the [–merge-install](https://colcon.readthedocs.io/en/released/user/isolated-vs-merged-workspaces.html) option with your colcon build will limit the number of depending directories, making it easier to configure PyCharm.

<a id="attach-to-process"></a>

### Attach to Process

Even without any configuration to PyCharm, you can always just attach to a running Python node.
Open your project source and simply run your node as usual:

```
$ ros2 run my_node main
```

Then in PyCharm select “Run” > “Attach to Process…”.
It might take a second, but a small window should show listing the currently running Python instances, including your node.
There can be multiple Python processes, so there may be some trial-and-error to find the right one.

After selecting an instance, the usual debugging tools are available.
You can pause it or create breakpoints in the code and step through it.

> [!NOTE]
>
> The code in your project might not be the files being executed, see [this](#installedpythoncode).

<a id="run-debug"></a>

### Run/Debug

Follow the steps for integration first.

Running your Python file from PyCharm will likely result in import errors.
This is because PyCharm extends the `PYTHONPATH` environment variable, but it leaves `PATH` untouched.
Necessary library files in `ros/bin` are not found.

Edit the run/debug configuration for your file and under “Environment Variables:” add a new variable.
It is currently not supported to extend the existing `PATH`, so we need to override it.
From a sourced ROS terminal, export the content of `PATH` with: `echo $Env:PATH`.
Copy the result.

Back in PyCharm, paste it as `PATH`, apply changes and run or debug your node.
It should work like any Python project now, allowing easy additions of breakpoints and other debug methods.

> [!NOTE]
>
> On Windows it seems the capitalization of the `PATH` variable under “Environment Variables:” must be “path” (all lowercase) in order to work.

---
title: "Using Eclipse Oxygen with rviz2 [community-contributed]"
docname: "Tutorials/Miscellaneous/Eclipse-Oxygen-with-ROS-2-and-rviz2"
source: "Tutorials/Miscellaneous/Eclipse-Oxygen-with-ROS-2-and-rviz2.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Tutorials hub](../../../wiki/tutorial-paths.md)
> Related: [Ament Lint CLI Utilities](../advanced/ament-lint-for-clean-code.md) | [Building a package with Eclipse 2021-06](building-ros2-package-with-eclipse-2021-06.md) | [Building a real-time Linux kernel [community-contributed]](building-realtime-rt-preempt-kernel-for-ros-2.md) | [Composing multiple nodes in a single process](../intermediate/composition.md) | [Configure service introspection](../demos/service-introspection.md)

<a id="using-eclipse-oxygen-with-rviz2-community-contributed"></a>

# Using Eclipse Oxygen with `rviz2` [community-contributed]

Table of Contents

- [Setup](#setup)
- [Eclipse-indexer](#eclipse-indexer)
- [Debugging with eclipse](#debugging-with-eclipse)

<a id="setup"></a>

## Setup

This tutorial assumes Eclipse Oxygen, git, and [Egit](http://www.eclipse.org/egit/download/) are already installed.

Throughout the tutorial we name the eclipse workspace the same name as the ros2 package, but this is not required.

HINT: We use nested projects and one Eclipse Workspace for each ROS-2 package.

![../../../_images/eclipse-oxygen-01.png](../../../assets/images/eclipse-oxygen-01.png)

Create a C++ Project.

![../../../_images/eclipse-oxygen-02.png](../../../assets/images/eclipse-oxygen-02.png)
![../../../_images/eclipse-oxygen-03.png](../../../assets/images/eclipse-oxygen-03.png)

Choose the ROS 2 package name as the Project Name.
Choose a Makefile Project and Other Toolchain.

![../../../_images/eclipse-oxygen-04.png](../../../assets/images/eclipse-oxygen-04.png)

Click on Finish

![../../../_images/eclipse-oxygen-05.png](../../../assets/images/eclipse-oxygen-05.png)

Our project should be shown in the “Project Explorer”.

![../../../_images/eclipse-oxygen-06.png](../../../assets/images/eclipse-oxygen-06.png)

Inside our Project create a folder called “src”.

![../../../_images/eclipse-oxygen-07.png](../../../assets/images/eclipse-oxygen-07.png)

Import a git repository.

![../../../_images/eclipse-oxygen-08.png](../../../assets/images/eclipse-oxygen-08.png)

Put in the repository URL.

![../../../_images/eclipse-oxygen-09.png](../../../assets/images/eclipse-oxygen-09.png)

IMPORTANT: Use the source folder of the project we created before as the destination folder.

HINT: If you ran into problems choosing the destination folder path, the Eclipse Dialog needs a name in the name field.

![../../../_images/eclipse-oxygen-10.png](../../../assets/images/eclipse-oxygen-10.png)

Import using the new project wizard.

![../../../_images/eclipse-oxygen-11.png](../../../assets/images/eclipse-oxygen-11.png)

Create a General->Project.

![../../../_images/eclipse-oxygen-12.png](../../../assets/images/eclipse-oxygen-12.png)

Use the git repository name as the project name.
IMPORTANT: Use the folder we cloned the git repository in as the “Location”.

![../../../_images/eclipse-oxygen-13.png](../../../assets/images/eclipse-oxygen-13.png)

The git project and the new project should be visible in the Project Explorer view.
The same files are listed multiple times, but only one project is linked with Egit.

![../../../_images/eclipse-oxygen-14.png](../../../assets/images/eclipse-oxygen-14.png)

Repeat this procedure again.
Import git repository pluginlib.

![../../../_images/eclipse-oxygen-15.png](../../../assets/images/eclipse-oxygen-15.png)

IMPORTANT: Use a folder inside the source folder as “Destination->Directory”.

![../../../_images/eclipse-oxygen-16.png](../../../assets/images/eclipse-oxygen-16.png)

IMPORTANT: Use the folder we cloned the git repository in as the location for the new project.

![../../../_images/eclipse-oxygen-17.png](../../../assets/images/eclipse-oxygen-17.png)

Run the same procedure with the tinyxml2\_vendor git repository.

![../../../_images/eclipse-oxygen-18.png](../../../assets/images/eclipse-oxygen-18.png)

IMPORTANT: Again use a folder inside the source folder.

![../../../_images/eclipse-oxygen-19.png](../../../assets/images/eclipse-oxygen-19.png)

IMPORTANT: Use the location of the folder we cloned as the new project folder.

![../../../_images/eclipse-oxygen-20.png](../../../assets/images/eclipse-oxygen-20.png)

Now all four Projects should be visible in the Project Explorer view.

![../../../_images/eclipse-oxygen-21.png](../../../assets/images/eclipse-oxygen-21.png)

Clicking in the top right cornder for the Project Explorer view allows us to change the Project Presentation to Hierarchical view.
Now it looks like a ROS-2 project as it is on the hard drive.
But this view loses the linkage to Egit, so use the Flat Project Presentation.
The Egit linkage is good if you want to see e.g. which author wrote which code-line, etc.

![../../../_images/eclipse-oxygen-22.png](../../../assets/images/eclipse-oxygen-22.png)

Go to “C/C++ build”-section and put “ament” into “Build command”.

![../../../_images/eclipse-oxygen-23.png](../../../assets/images/eclipse-oxygen-23.png)

Go to “Behavior” tab and unselect “clean” and put “build” into Build textbox.

![../../../_images/eclipse-oxygen-24.png](../../../assets/images/eclipse-oxygen-24.png)

Before “Build project” will work, we need to close Eclipse.
Open a shell and source the ROS-2 setup.bash file, then cd into the directory of the eclipse project (here: /home/ubu/rviz2\_ws/rviz2\_ws) and start Eclipse from inside this directory.

![../../../_images/eclipse-oxygen-25.png](../../../assets/images/eclipse-oxygen-25.png)

Now code completion, egit annotations, eclipse C/C++ Tools, etc. should all work.

![../../../_images/eclipse-oxygen-26.png](../../../assets/images/eclipse-oxygen-26.png)

<a id="eclipse-indexer"></a>

## Eclipse-indexer

Opening the main.cpp of rviz2 may show a lot of “unresolved inclusion” warnings.
To fix this, go to Project->Properties->C++ General->Path and Symbols.
Click on the “References” tab and select “ros2\_ws”.

![../../../_images/eclipse-oxygen-27.png](../../../assets/images/eclipse-oxygen-27.png)

Go to C/C++-General->Path-and-Symbols, click on the “Source locations” tab and click on “Link folder”.
Choose the location of qt5 includes.

![../../../_images/eclipse-oxygen-28.png](../../../assets/images/eclipse-oxygen-28.png)

The next image should be shown.
It is a good idea to add excludes to the source locations, so that some directories (like “Build” and “Install”) don’t get indexed.

![../../../_images/eclipse-oxygen-29.png](../../../assets/images/eclipse-oxygen-29.png)

Go to C++General->Preprocessor includes, select “CDT GCC Built in compiler settings [Shared]” and enter in the “command to get compiler specs” text box the following:

```
-std=c++14
```

![../../../_images/eclipse-oxygen-30.png](../../../assets/images/eclipse-oxygen-30.png)

Go to “C/C++-General->Indexer” and select the following in the image.
E.g “index unused headers as c files” to resolve e.g. QApplication, because the QApplication headers content is only “#include “qapplication.h”.

![../../../_images/eclipse-oxygen-31.png](../../../assets/images/eclipse-oxygen-31.png)

After running the indexer (which happens later, so you will see this also later), you can see what it added

![../../../_images/eclipse-oxygen-32.png](../../../assets/images/eclipse-oxygen-32.png)

After that right-click on the rviz2 project and select “Indexer->Rebuild”, which will start rebuilding the index (there is an icon in the lower right showing progress).
Once the index is finished rebuilding, it should be able to resolve all includes.

![../../../_images/eclipse-oxygen-33.png](../../../assets/images/eclipse-oxygen-33.png)

<a id="debugging-with-eclipse"></a>

## Debugging with eclipse

Go to “C/C++-Build” and add to the build command:

```
-DCMAKE_BUILD_TYPE=Debug
```

![../../../_images/eclipse-oxygen-34.png](../../../assets/images/eclipse-oxygen-34.png)

Then in eclipse go to “Run->Debug Configurations” and add the following and click on “Debug”.

![../../../_images/eclipse-oxygen-35.png](../../../assets/images/eclipse-oxygen-35.png)

---
title: "ROS Build Farms"
docname: "The-ROS2-Project/Contributing/Build-Farms"
source: "The-ROS2-Project/Contributing/Build-Farms.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "project"
tags: ["ros2", "jazzy", "project"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Project hub](../../../wiki/tooling-map.md)
> Related: [Add Your Project](../adopters/add-your-project.md) | [Code style and language versions](code-style-language-versions.md) | [Contributing to ROS 2 Documentation](contributing-to-ros-2-documentation.md) | [Quality guide: ensuring code quality](quality-guide.md) | [ROS 2 developer guide](developer-guide.md)

<a id="ros-build-farms"></a>
<a id="buildfarms"></a>

# ROS Build Farms

Table of Contents

- [Jobs and Deployment](#jobs-and-deployment)
- [Frequency Asked Questions (FAQ) and Troubleshooting](#frequency-asked-questions-faq-and-troubleshooting)
- [Further Reading](#further-reading)

The ROS build farms are an important infrastructure to support the ROS ecosystem, provided and
maintained by [Open Robotics](https://www.openrobotics.org/).
They provide building of source and binary packages, continuous integration, testing, and analysis for ROS 1 and ROS 2 packages.
There are two hosted instance for open source packages:

1. <https://build.ros.org/> for ROS 1 packages
2. <https://build.ros2.org/> for ROS 2 packages

If you are going to use any of the provided infrastructure please consider signing up for the
[build farm discussion forum](https://discourse.openrobotics.org/c/infrastructure-project/infra-buildfarm/20) in order to receive notifications,
e.g., about any upcoming changes.

<a id="jobs-and-deployment"></a>

## Jobs and Deployment

The ROS build farms perform several different jobs.
For each job type you will find a detailed description of what they do and how they work:

- [release jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/release_jobs.rst) generate binary packages, e.g., deb packages
- [devel jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/devel_jobs.rst) build and test ROS packages within a single repository on a polling basis
- [pull\_request jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/devel_jobs.rst) build and test ROS packages within a single repository triggered by webhooks
- [CI jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/ci_jobs.rst) build and test ROS packages across repositories with the option of using artifacts
  from other CI jobs to speed up the build
- [doc jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/doc_jobs.rst) generate the API documentation of packages and extract information from the manifests
- [miscellaneous jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/miscellaneous_jobs.rst) perform maintenance tasks and generate informational data to visualize the
  status of the build farm and its generated artifacts

<a id="creation-and-deployment"></a>

### Creation and Deployment

The above jobs are created and deployed when packages are [bloomed](http://wiki.ros.org/bloom), i.e. released for ROS
1 or ROS 2.
Once blooming is successful and a package is incorporated in one of the ROS
distributions (via pull request to [rosdistro](https://github.com/ros/rosdistro)), the according jobs will be spawned.
The names of the jobs encode their type and purpose: [[1]](#id5)

- release jobs:

  > - `{distro}src_{platf}__{package}__{platform}__source` build source packages of releases
  > - `{distro}bin_{platf}__{package}__{platform}__binary` build binary packages of releases
  >
  > For instance, the binary packaging job of rclcpp on ROS 2 Rolling (running on Ubuntu Noble amd64) is named `Rbin_uN64__rclcpp__ubuntu_noble_amd64__binary`.
- devel jobs:

  > - `{distro}dev__{package}__{platform}` perform a CI build for the releasing branch
- pull\_request jobs

  > - `{distro}pr__{package}__{platform}` perform a CI build for a pull request
  >
  > For instance, the PR job for rclcpp on ROS 2 Rolling (running on Ubuntu Noble amd64) is named `Rpr__rclcpp__ubuntu_noble_amd64`.

<a id="execution"></a>

### Execution

Execution of the jobs depends on the type of the job:

- [devel jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/devel_jobs.rst) will be triggered every time a commit is done to the respective branch polling based on a configured frequency.
- [pull\_request jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/devel_jobs.rst) will be triggered by webhooks from respective pull request of the upstream [[2]](#id6) repository
- [release jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/release_jobs.rst) will be triggered once every time a new package version is released, i.e. a new
  [rosdistro](https://github.com/ros/rosdistro) pull request was accepted for this package.
  The source jobs are triggered by a version
  change in the rosdistro distribution file, the binary jobs are triggered by their source counterpart.

<a id="frequency-asked-questions-faq-and-troubleshooting"></a>

## Frequency Asked Questions (FAQ) and Troubleshooting

1. **I get Jenkins mails from failing build farm jobs; What do I do?**

   Go to the job that raised the issue.
   You find the link on top of the Jenkins email.
   Once you followed the link to the build job, click *Console Output* on the left, then click *Full Log*.
   This will give you the full console output of the failing build.
   Try to find the top-most error as it is usually the most important and other errors might be follow-ups.

   The bottom of the email might read
   `'apt-src build [...]' failed. This is usually because of an error building the package.`
   This usually hints at missing dependencies, see 2.
2. **I seem to be missing a dependency, how do I find out which one?**

   You basically have two options:
   Option a is easier but may take several iterations;
   Option b is more elaborate and gives you the full insight as well as local debugging.

   1. Inspect the release job that raised the issue (see above question) and localize the cmake dependency issue.
      To do so, browse to the cmake section, e.g., navigate to the *build binarydeb*
      section through the menu on the left in case of a Ubuntu/Debian build job.
      The *CMake Error* will typically hint at a dependency required by the cmake configuration but missing in the [package manifest](http://wiki.ros.org/Manifest).
      Once you have fixed the dependency in the manifest, do a new release of your package and wait for feedback from the build farms or…
   2. To get the full insight and faster, local debugging, you can [run the release jobs locally](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/release_jobs.rst#run-the-release-job-locally).
      This allows to iterate the manifest locally until all dependencies are fixed.
3. **Why do release jobs fail when devel jobs / my github actions / my local builds succeed?**

   There are several potential reasons for this.
   First, release jobs build against a minimal ROS installation to check if all dependencies are
   properly declared in the [package manifest](http://wiki.ros.org/Manifest).
   Devel jobs / github actions / local builds may
   be performed in an environment that has the dependencies already installed, therefore does not
   notice dependency issues.
   Second, they might build different versions of the source code.
   While devel jobs / github actions / local builds usually build the latest version from the
   *upstream* [[2]](#id6) repository, [release jobs](https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/jobs/release_jobs.rst) build the source code of the latest release, i.e. the source code in the respective *upstream* branches of the *release* repository [[3]](#id7).

<a id="further-reading"></a>

## Further Reading

The following links provide more details and insights into the build farms:

- <https://github.com/ros-infrastructure/ros_buildfarm/blob/master/doc/index.rst> - General
  documentation of the build farm infrastructure and the generated build jobs
- <http://wiki.ros.org/regression_tests#Setting_up_Your_Computer_for_Prerelease>
- <http://wiki.ros.org/buildfarm> - ROS wiki entry for the ROS 1 build farm (partially *outdated*)
- <https://github.com/ros-infrastructure/cookbook-ros-buildfarm> - Installs and configures ROS build
  farm machines

[[1](#id1)]

`{distro}` is the first letter of the ROS distribution, `{platform}` (`{platf}`)
names the platform the package is built for (and its short code), and `{package}` is the
name of the ROS package being built.

[2]
([1](#id2),[2](#id3))

The *upstream* repository is the repository containing the original source code of the
respective ROS 1 / ROS 2 package.

[[3](#id4)]

The *release* repository is the repository that ROS 2 infrastructure uses for releasing
packages, see <https://github.com/ros2-gbp/>.

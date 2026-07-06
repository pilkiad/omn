---
title: "Index Your Packages"
docname: "How-To-Guides/Releasing/Index-Your-Packages"
source: "How-To-Guides/Releasing/Index-Your-Packages.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](first-time-release.md) | [Migrating a C++ Package Example](../migrating-from-ros1/migrating-cpp-package-example.md) | [Migrating a Python Package Example](../migrating-from-ros1/migrating-python-package-example.md) | [Migrating C++ Packages Reference](../migrating-from-ros1/migrating-cpp-packages.md) | [Migrating Interfaces](../migrating-from-ros1/migrating-interfaces.md)

<a id="index-your-packages"></a>

# Index Your Packages

Are you releasing a new ROS package into a ROS distribution?
Make the process faster by indexing your packages first.

<a id="put-your-ros-packages-into-a-public-repository"></a>

## Put your ROS packages into a public repository

If you haven’t done so already, put the source code of your ROS packages into a public git repository.
All packages released into ROS must be open source.
You can host code anywhere, but GitHub is recommended because it gives you the option to enable pull request jobs.
Here are some choices:

- [GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) **Recommended**
- [GitLab](https://docs.gitlab.com/ee/user/project/repository/)
- [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/create-a-git-repository/)

<a id="give-your-packages-an-osi-approved-license"></a>

## Give your packages an OSI Approved license

Choose an [OSI approved license](https://opensource.org/licenses) and give it to your ROS packages.
If you’re having trouble deciding, consider using the license used by most of the core ROS 2 packages: [Apache-2.0 license](https://opensource.org/license/apache-2-0).

For each `package.xml` in your repository, put the SPDX short identifier of the license in the `<license>` tag in your `package.xml`.

If all of your ROS packages have the same license, or if there’s only one ROS package in your repository, create a file called `LICENSE` at the root of your repository and put the text of the license you chose in it.
If the ROS packages in your repository have different licenses, create a `LICENSE` file adjacent to every `package.xml` file.

<a id="give-your-packages-rep-144-compliant-names"></a>

## Give your packages REP 144 compliant names

Packages released into a ROS distribution must have names that comply with [REP 144](https://reps.openrobotics.org/rep-0144/).
Read the full REP to understand the rules.
If one of your ROS package names doesn’t comply, then change the name before continuing.

<a id="decide-what-ros-distribution-you-want-to-release-into"></a>

## Decide what ROS distribution you want to release into

Decide what ROS distribution you want to release your packages into.
At a minimum, you should release your packages into [ROS Rolling](https://docs.ros.org/en/rolling) so that your ROS packages are automatically included in the next ROS release.
You may also want to release into any active ROS distributions, but this is up to you.

<a id="create-a-github-account"></a>

## Create a GitHub account

[Create a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) if you don’t already have one.
You don’t have to host the source code of your ROS packages on GitHub, but you will need an account to index and release packages.

<a id="fork-and-clone-ros-rosdistro"></a>

## Fork and clone ros/rosdistro

[Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the [ros/rosdistro](https://github.com/ros/rosdistro/) repository.
You only need to do this step once on your account.
The fork will be used every time you do a release.

<a id="make-changes-to-your-fork"></a>

## Make changes to your fork

Remember the ROS distributions you decided to release into?
Each ROS distribution has a folder in the [ros/rosdistro](https://github.com/ros/rosdistro/) repository.
For example, the name of the ROS Rolling folder is `rolling`.
For each ROS distribution you want to release into:

1. fill out the following template
2. put the filled-out template into the `distribution.yaml` file in the corresponding ROS distribution’s folder

```
YOUR-REPO-NAME:
  source:
    type: git
    url: https://YOUR-GIT-REPO-URL.git
    version: YOUR-BRANCH-NAME
  status: YOUR-STATUS
```

Here’s how to fill out each item:

- YOUR-REPO-NAME: This is an arbitrary human-readable name.
  For repos hosted on GitHub, use the lowercase name of your repository not including the organization.
  For example, the repository name of `https://github.com/ros2/rosidl` is `rosidl`.
- YOUR-GIT-REPO-URL: This is the https URL from which one could `git clone` your repository
  For example, the git repo URL of `https://github.com/ros2/rosidl` is `https://github.com/ros2/rosidl.git`.
  It is important that this URL ends in `.git`, or it will fail to pass the linters.
- YOUR-BRANCH-NAME: This is the git branch on your repository from which you will release your package into this ROS distribution.
  This is commonly one of: `main`, `master`, or the name of the ROS distribution itself.
  For example, the [rosidl repository](https://github.com/ros2/rosidl) uses the branch `rolling` to hold changes to be released into ROS Rolling.
- YOUR-STATUS: This is a status from the list in [REP 141](https://reps.openrobotics.org/rep-0141/#distribution-file).
  You likely want either `maintained` or `developed`.

<a id="open-a-pull-request-to-ros-rosdistro"></a>

## Open a pull request to ros/rosdistro

[Open a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to [ros/rosdistro](https://github.com/ros/rosdistro/) with the branch that you made your changes to.
Wait a few days for it to be reviewed.

<a id="what-happens-next"></a>

## What happens next

You’ve now done everything required to index your ROS packages.
One of the reviewers will look at your pull request and decide if it [satisfies the review guidelines](https://github.com/ros/rosdistro/blob/master/REVIEW_GUIDELINES.md).
The reviewer may either approve your changes as is, or give you actionable feedback.
Once the pull request meets the review guidelines it will be merged, and your packages will appear on the [ROS Index](https://index.ros.org/).

You’ve completed an important step toward releasing your package.
Proceed to the next guide: [First Time Release](first-time-release.md).

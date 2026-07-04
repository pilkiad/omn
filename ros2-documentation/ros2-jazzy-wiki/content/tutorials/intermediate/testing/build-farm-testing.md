---
title: "Testing Your Code with the ROS Build Farm"
docname: "Tutorials/Intermediate/Testing/BuildFarmTesting"
source: "Tutorials/Intermediate/Testing/BuildFarmTesting.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="testing-your-code-with-the-ros-build-farm"></a>

# Testing Your Code with the ROS Build Farm

The [ROS 2 Build Farm](https://build.ros2.org/) is incredibly powerful.
In addition to creating binaries, it will also test pull requests by compiling and running all the tests for your ROS packages before the PR is merged.

There are four prerequisites.

> - The GitHub user [@ros-pull-request-builder](https://github.com/ros-pull-request-builder) must have access to the repository.
> - The GitHub repository must have the webhooks set up.
> - [Your package must be indexed in rosdistro](../../../how-to/releasing/index-your-packages.md)
> - The `test_pull_requests` flag must be true.

<a id="github-access"></a>

## GitHub Access

You can give access to the PR Builder either at the GitHub organization level OR just to the single GitHub repository.

<a id="github-organization"></a>

### GitHub Organization

1. Open <https://github.com/orgs/%YOUR_ORG%/people>
   (while replacing `%YOUR_ORG%` with the appropriate organization)
2. Click `Invite Member` and enter `ros-pull-request-builder`

<a id="github-repository"></a>

### GitHub Repository

1. Open <https://github.com/%YOUR_ORG%/%YOUR_REPO%/settings/access>
   (while replacing `%YOUR_ORG%/%YOUR_REPO$` with the appropriate organization/repo)
2. Click `Add people` and enter `ros-pull-request-builder`
3. Select `Admin` or `Write` for their role.
   (see next section)

<a id="webhooks"></a>

## WebHooks

If you grant full administrative rights to `ros-pull-request-builder`, it will automatically setup the hooks.

Alternatively, you can avoid the need for full administrative rights by setting them up with only **write** permissions.

1. Open <https://github.com/%YOUR_ORG%/%YOUR_REPO%/settings/hooks/new>)
2. Enter `"https://build.ros2.org/ghprbhook/` as the Payload URL
3. Check the following options:
   :   - Let me select individual events.
       - Issue comments
       - Pull requests

<a id="test-pull-requests"></a>

## test\_pull\_requests

For each ROS distro that you want pull request testing for, you must enable the `test_pull_requests` flag in the appropriate section of the [rosdistro](https://github.com/ros/rosdistro/).

> - **Option 1** - You have the option when running [bloom](../../../how-to/releasing/releasing-a-package.md) to turn on pull request testing.
> - **Option 2** - You can **carefully** manually edit the appropriate file in the rosdistro repo, and make a new pull request.
>   [Example](https://github.com/ros/rosdistro/blob/3c295f76b0755989e9ed526c0b5f28a5f6a94da3/rolling/distribution.yaml#L4708).
>   [Documented in REP 143](http://docs.ros.org/en/independent/api/rep/html/rep-0143.html#distribution-file).

Note that after the pull request has been added, the job will usually not be created until the nightly Jenkins reconfiguration.

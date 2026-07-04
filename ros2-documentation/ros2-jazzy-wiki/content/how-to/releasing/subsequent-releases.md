---
title: "Subsequent Releases"
docname: "How-To-Guides/Releasing/Subsequent-Releases"
source: "How-To-Guides/Releasing/Subsequent-Releases.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "how-to"
tags: ["ros2", "jazzy", "how-to"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [How-To Guides hub](../../../wiki/task-map.md)
> Related: [First Time Release](first-time-release.md) | [Index Your Packages](index-your-packages.md) | [Migrating a C++ Package Example](../migrating-from-ros1/migrating-cpp-package-example.md) | [Migrating a Python Package Example](../migrating-from-ros1/migrating-python-package-example.md) | [Migrating C++ Packages Reference](../migrating-from-ros1/migrating-cpp-packages.md)

<a id="subsequent-releases"></a>

# Subsequent Releases

This guide explains how to release new versions of ROS packages that have already been released before.

Table of Contents

- [Be part of the release team](#be-part-of-the-release-team)
- [Install dependencies](#install-dependencies)
- [Set up a Personal Access Token](#set-up-a-personal-access-token)
- [Ensure repositories are up-to-date](#ensure-repositories-are-up-to-date)
- [Updating Changelog](#updating-changelog)
- [Bump the package version](#bump-the-package-version)
- [Bloom Release](#bloom-release)
- [Next Steps](#next-steps)

<a id="be-part-of-the-release-team"></a>

## Be part of the release team

If you are not part of the release team that has write access to the release repository, follow [Join a release team](release-team-repository.md#join-a-release-team).

<a id="install-dependencies"></a>

## Install dependencies

Install tools that you will use in the upcoming steps according to your platform:

deb (e.g. Ubuntu)

```
$ sudo apt install python3-bloom python3-catkin-pkg
```

RPM (e.g. RHEL)

```
$ sudo dnf install python3-bloom python3-catkin_pkg
```

Other

```
$ pip3 install -U bloom catkin_pkg
```

Make sure you have rosdep initialized:

```
$ sudo rosdep init
$ rosdep update
```

Note that the `rosdep init` command may fail if it has already been initialized in the past; this can safely be ignored.

<a id="set-up-a-personal-access-token"></a>

## Set up a Personal Access Token

> [!WARNING]
>
> If the file `~/.config/bloom` exists on your computer, it is likely that you have done this before so you should skip this section.

During the release process, multiple HTTPS Git operations will be performed that require password authentication.
To avoid being repeatedly asked for a password, a [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) will be set up.
If you have multi-factor authentication setup on your GitHub account, you **must** setup a Personal Access Token.

Create a Personal Access Token by:

1. Log in to GitHub and go to [Personal access tokens](https://github.com/settings/tokens).
2. Click the **Generate new token** button.
3. In the dropdown, select **Generate new token (classic)**
4. Set **Note** to something like `Bloom token`.
5. Set **Expiration** to **No expiration**.
6. Tick the `public_repo` and `workflow` checkboxes.
7. Click the **Generate token** button.

After you have created the token, you will end up back at the *Personal access tokens* page.
**Copy the alphanumeric token** that is highlighted in green.

Save your GitHub username and PAT to a new file called `~/.config/bloom`, with the format below:

```
{
   "github_user": "<your-github-username>",
   "oauth_token": "<token-you-created-for-bloom>"
}
```

Configure in your `~/.gitconfig` that your GitHub account and PAT are used for all release repositories under [ros2-gbp](https://github.com/ros2-gbp):

```
[credential "https://github.com/ros2-gbp"]
    username = x-access-token
    helper = "!f() { test \"$1\" = get && echo \"password=<token-you-created-for-bloom>\"; }; f"
```

You can additionally use different GitHub accounts and PATs for individual release repositories:

```
[credential "https://github.com/ros2-gbp/my_package-release.git"]
    username = x-access-token
    helper = "!f() { test \"$1\" = get && echo \"password=<other-token-you-created-for-bloom>\"; }; f"
```

<a id="ensure-repositories-are-up-to-date"></a>

## Ensure repositories are up-to-date

Make sure that:

- Your repository is hosted on a remote such as GitHub.
- You have a clone of the repository on your computer and are on the right branch.
- Both the remote repository and your clone are up-to-date.

<a id="updating-changelog"></a>

## Updating Changelog

For your users and for the developers, keep the changelog concise and up to date.

```
$ catkin_generate_changelog
```

Open all `CHANGELOG.rst` files in an editor.
You will see that `catkin_generate_changelog` has auto-generated a forthcoming section with notes from commit messages:

```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package your_package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* you can modify this commit message
* and this
```

Clean up the list of commit messages to concisely convey the notable changes that have been made to the packages since the last release, and **commit all the CHANGELOG.rst files.**
Do not modify the `Forthcoming` header.

<a id="bump-the-package-version"></a>

## Bump the package version

Every release of the package must have a unique version number higher than the previous release.

Run:

```
$ catkin_prepare_release
```

which performs the following:

1. increases the package version in `package.xml`
2. replaces the heading `Forthcoming` with `version (date)` (e.g. `0.0.1 (2022-01-08)`) in `CHANGELOG.rst`
3. commits those changes
4. creates a tag (e.g. `0.0.1`)
5. pushes the changes and the tag to your remote repository

> [!NOTE]
>
> By default the patch version of the package is incremented, such as from `0.0.0` to `0.0.1`.
> To increment the minor or major version instead, run `catkin_prepare_release --bump minor` or `catkin_prepare_release --bump major`.
> For more details, see `catkin_prepare_release --help`.

> [!NOTE]
>
> If your repository has a strict merge rule like `Require a pull request before merging`, you will need to create a pull request with the changes/tag generated by `catkin_prepare_release` and then merge that, since you cannot directly push to the branch.
> Depending on your repository’s pull request merge settings (such as squash merge or rebase merge), merging the pull request may change the SHA of the version commit.
> In such cases, you will need to manually re-tag the version commit after merging to ensure the tag points to the correct commit.

<a id="bloom-release"></a>

## Bloom Release

Run the following command, replacing `my_repo` with the name of your repository with the packages:

```
$ bloom-release --rosdistro jazzy my_repo
```

Bloom will automatically create a pull request for you against [rosdistro](https://github.com/ros/rosdistro).

> [!NOTE]
>
> By default, bloom will release all packages in the source repository.
> To selectively block the release of some packages for a particular `jazzy`, add `jazzy.ignored` files to the `master` branch of the release repository.
> In each file, list the name of the package, one per line, to block the release of the package.
> The [rosidl-release](https://github.com/ros2-gbp/rosidl-release) repository may serve as a useful reference for this configuration.

<a id="next-steps"></a>

## Next Steps

Once your pull request has been submitted, usually within one or two days, one of the maintainers of rosdistro will review and merge your Pull Request.
If your package build is successful, in 24-48 hours your packages will become available in the **ros-testing** repository, where you can [test your pre-release binaries](../../installation/testing.md).

Approximately every two to four weeks, the distribution’s release manager manually synchronizes the contents of ros-testing into the main ROS repository.
This is when your packages actually become available to the rest of the ROS community.
To get updates on when the next synchronization (sync) is coming, subscribe to the [Packaging and Release Management Category on Open Robotics Discourse](https://discourse.openrobotics.org/c/ros/release/16).

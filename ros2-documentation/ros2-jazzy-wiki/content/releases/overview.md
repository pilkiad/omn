---
title: "Distributions"
docname: "Releases"
source: "Releases.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "releases"
tags: ["ros2", "jazzy", "releases"]
---

> Navigation: [Wiki index](../../index.md) | [Summary](../../SUMMARY.md) | [Releases hub](../../wiki/tooling-map.md)
> Related: [About ROS](../getting-started/about-ros.md) | [Citations](../reference/citations.md) | [Concepts](../concepts/overview.md) | [Contact](../reference/contact.md) | [First steps with ROS - learning path](../getting-started/first-steps.md)

<a id="distributions"></a>
<a id="releases"></a>

# Distributions

<a id="what-is-a-distribution"></a>

## What is a Distribution?

A ROS distribution is a versioned set of ROS packages.
These are akin to Linux distributions (e.g. Ubuntu).
The purpose of the ROS distributions is to let developers work against a relatively stable codebase until they are ready to roll everything forward.
Therefore once a distribution is released, we try to limit changes to bug fixes and non-breaking improvements for the core packages (every thing under ros-desktop-full).
That generally applies to the whole community, but for “higher” level packages, the rules are less strict, and so it falls to the maintainers of a given package to avoid breaking changes.

<a id="list-of-distributions"></a>
<a id="id1"></a>

## List of Distributions

Below is a list of current and historic ROS 2 distributions.
Rows in the table marked in blue are the currently supported distributions.

/\* Targeting the cells and rows for the background and plain text \*/
.rst-content table.distros:not(.field-list) tr:nth-child(1) td,
.rst-content table.distros tr:nth-child(2),
.rst-content table.distros:not(.field-list) tr:nth-child(3) td,
.rst-content table.distros:not(.field-list) tr:nth-child(5) td {
background-color: #22314E;
color: white;
}
/\* Targeting the links inside those specific rows to force them to be not-blue \*/
.rst-content table.distros:not(.field-list) tr:nth-child(1) td a,
.rst-content table.distros tr:nth-child(2) a,
.rst-content table.distros:not(.field-list) tr:nth-child(3) td a,
.rst-content table.distros:not(.field-list) tr:nth-child(3) td a {
color: #B0B0B0 !important;
}

| Distro | Release date | Logo | EOL date | ROS Boss |
| --- | --- | --- | --- | --- |
| [Lyrical Luth](release-lyrical-luth.md) | May 22, 2026 | Lyrical logo | May 2031 | [Shane Loretz](https://github.com/sloretz) |
| [Kilted Kaiju](release-kilted-kaiju.md) | May 23, 2025 | Kilted logo | December 2026 | [Scott K Logan](https://github.com/cottsay) |
| [Jazzy Jalisco](release-jazzy-jalisco.md) | May 23, 2024 | Jazzy logo | May 2029 | [Marco A. Gutiérrez](https://github.com/marcoag) |
| [Iron Irwini](release-iron-irwini.md) | May 23, 2023 | Iron logo | December 4, 2024 | [Yadunund Vijay](https://github.com/Yadunund) |
| [Humble Hawksbill](release-humble-hawksbill.md) | May 23, 2022 | Humble logo | May 2027 | [Christophe Bédard](https://github.com/christophebedard) / [Audrow Nash](https://github.com/audrow) |
| [Galactic Geochelone](release-galactic-geochelone.md) | May 23, 2021 | Galactic logo | December 9, 2022 | [Scott Logan](https://github.com/cottsay/) |
| [Foxy Fitzroy](release-foxy-fitzroy.md) | June 5, 2020 | Foxy logo | June 20, 2023 | [Jacob Perron](https://github.com/jacobperron) / [Dharini Dutia](https://github.com/quarkytale) |
| [Eloquent Elusor](release-eloquent-elusor.md) | November 22, 2019 | Eloquent logo | November 2020 | [Michael Carroll](https://github.com/mjcarroll) |
| [Dashing Diademata](release-dashing-diademata.md) | May 31, 2019 | Dashing logo | May 2021 | [Steven! Ragnarök](https://github.com/nuclearsandwich) |
| [Crystal Clemmys](release-crystal-clemmys.md) | December 14, 2018 | Crystal logo | December 2019 | [Steven! Ragnarök](https://github.com/nuclearsandwich) |
| [Bouncy Bolson](release-bouncy-bolson.md) | July 2, 2018 | Bouncy logo | July 2019 | [Mikael Arguedas](https://github.com/mikaelarguedas) / [Steven! Ragnarök](https://github.com/nuclearsandwich) |
| [Ardent Apalone](release-ardent-apalone.md) | December 8, 2017 | Ardent logo | December 2018 | [Steven! Ragnarök](https://github.com/nuclearsandwich) |
| [beta3](beta3-overview.md) | September 13, 2017 |  | December 2017 |  |
| [beta2](beta2-overview.md) | July 5, 2017 |  | September 2017 |  |
| [beta1](beta1-overview.md) | December 19, 2016 |  | Jul 2017 |  |
| [alpha1 - alpha8](alpha-overview.md) | August 31, 2015 |  | December 2016 |  |

<a id="future-distributions"></a>

## Future Distributions

For details on upcoming features see the [roadmap](../project/roadmap.md).

There is a new ROS 2 distribution released yearly on May 23rd ([World Turtle Day](https://www.worldturtleday.org/)).

| Distro | Release date | Logo | EOL date |
| --- | --- | --- | --- |
| [Makoa Mata-mata](release-makoa-mata-mata.md) | May 2027 | TBD | Dec 2028 |

<a id="rolling-distribution"></a>
<a id="id5"></a>

## Rolling Distribution

[ROS 2 Rolling Ridley](release-rolling-ridley.md) is the rolling development distribution of ROS 2.
It is described in [REP 2002](https://reps.openrobotics.org/rep-2002/) and was first introduced in June 2020.

The Rolling distribution of ROS 2 serves two purposes:

1. it is a staging area for future stable distributions of ROS 2, and
2. it is a collection of the most recent development releases.

As the name implies, Rolling is continuously updated and **can have in-place updates that include breaking changes**.
We recommend that most people use the most recent stable distribution instead (see [List of Distributions](#list-of-distributions)).

Packages released into the Rolling distribution will be automatically released into future stable distributions of ROS 2.
[Releasing a ROS 2 package](../how-to/releasing/releasing-a-package.md) into the Rolling distribution follows the same procedures as all other ROS 2 distributions.

<a id="cross-distribution-communications"></a>

## Cross-Distribution Communications

Nodes are not guaranteed to be able to communicate across distributions.
For example, a node built & running against Humble is not guaranteed to be able to communicate correctly with a node built & running against Iron.
It may or may not work, but it is not supported and should not be relied upon.
Note that [cross-vendor (single-distro) communications are also not guaranteed](../concepts/intermediate/about-different-middleware-vendors.md#different-middleware-vendors-cross-vendor-communication).

---
title: "Nodes"
docname: "Concepts/Basic/About-Nodes"
source: "Concepts/Basic/About-Nodes.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](about-actions.md) | [Client libraries](about-client-libraries.md) | [Composition](../intermediate/about-composition.md) | [Cross-compilation](../intermediate/about-cross-compilation.md) | [Different ROS 2 middleware vendors](../intermediate/about-different-middleware-vendors.md)

<a id="nodes"></a>

# Nodes

A node is a participant in the ROS 2 graph, which uses a [client library](about-client-libraries.md) to communicate with other nodes.
Nodes can communicate with other nodes within the same process, in a different process, or on a different machine.
Nodes are typically the unit of computation in a ROS graph; each node should do one logical thing.

Nodes can [publish](about-topics.md) to named topics to deliver data to other nodes, or [subscribe](about-topics.md) to named topics to get data from other nodes.
They can also act as a [service client](about-services.md) to have another node perform a computation on their behalf, or as a [service server](about-services.md) to provide functionality to other nodes.
For long-running computations, a node can act as an [action client](about-actions.md) to have another node perform it on their behalf, or as an [action server](about-actions.md) to provide functionality to other nodes.
Nodes can provide configurable [parameters](about-parameters.md) to change behavior during run-time.

Nodes are often a complex combination of publishers, subscribers, service servers, service clients, action servers, and action clients, all at the same time.

Connections between nodes are established through a distributed [discovery](about-discovery.md) process.

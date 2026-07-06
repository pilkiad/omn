---
title: "Discovery"
docname: "Concepts/Basic/About-Discovery"
source: "Concepts/Basic/About-Discovery.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "concepts"
tags: ["ros2", "jazzy", "concepts"]
---

> Navigation: [Wiki index](../../../index.md) | [Summary](../../../SUMMARY.md) | [Concepts hub](../../../wiki/concept-map.md)
> Related: [Actions](about-actions.md) | [Client libraries](about-client-libraries.md) | [Composition](../intermediate/about-composition.md) | [Cross-compilation](../intermediate/about-cross-compilation.md) | [Different ROS 2 middleware vendors](../intermediate/about-different-middleware-vendors.md)

<a id="discovery"></a>

# Discovery

Discovery of nodes happens automatically through the underlying middleware of ROS 2.
It can be summarized as follows:

1. When a node is started, it advertises its presence to other nodes on the network with the same ROS domain (set with the ROS\_DOMAIN\_ID environment variable).
   Nodes respond to this advertisement with information about themselves so that the appropriate connections can be made and the nodes can communicate.
2. Nodes periodically advertise their presence so that connections can be made with new-found entities, even after the initial discovery period.
3. Nodes advertise to other nodes when they go offline.

Nodes will only establish connections with other nodes if they have compatible [Quality of Service](../../tutorials/demos/quality-of-service.md) settings.

Take the [talker-listener demo](../../installation/alternatives/ubuntu-development-setup.md#talker-listener) for example.
Running the C++ talker node in one terminal will publish messages on a topic,
and the Python listener node running in another terminal will subscribe to messages on the same topic.

You should see that these nodes discover each other automatically, and begin to exchange messages.

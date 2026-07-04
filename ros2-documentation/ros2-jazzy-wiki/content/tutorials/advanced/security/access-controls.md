---
title: "Setting access controls"
docname: "Tutorials/Advanced/Security/Access-Controls"
source: "Tutorials/Advanced/Security/Access-Controls.rst"
source_commit: "4b4d15e49c5eb047810c641155debe90d705056d"
topic: "tutorials"
tags: ["ros2", "jazzy", "tutorials"]
---

> Navigation: [Wiki index](../../../../index.md) | [Summary](../../../../SUMMARY.md) | [Tutorials hub](../../../../wiki/tutorial-paths.md)
> Related: [Adding a frame (C++)](../../intermediate/tf2/adding-a-frame-cpp.md) | [Adding a frame (Python)](../../intermediate/tf2/adding-a-frame-py.md) | [Adding physical and collision properties](../../intermediate/urdf/adding-physical-and-collision-properties-to-a-urdf-model.md) | [Building a movable robot model](../../intermediate/urdf/building-a-movable-robot-model-with-urdf.md) | [Building a visual robot model from scratch](../../intermediate/urdf/building-a-visual-robot-model-with-urdf-from-scratch.md)

<a id="setting-access-controls"></a>
<a id="access-controls"></a>

# Setting access controls

**Goal:** Limit the topics a node can use.

**Tutorial level:** Advanced

**Time:** 20 minutes

Contents

- [Background](#background)

  - [Modify `permissions.xml`](#modify-permissions-xml)
  - [Sign the policy file](#sign-the-policy-file)
  - [Launch the node](#launch-the-node)
  - [Use the templates](#use-the-templates)

<a id="background"></a>

## Background

Before proceeding ensure you have completed the [Setting up security](introducing-ros2-security.md) tutorial.

Permissions are quite flexible and can be used to control many behaviors within the ROS graph.

For this tutorial, we demonstrate a policy which only allows publishing messages on the default `chatter` topic.
This would prevent, for instance, remapping the topic when launching the listener or using the same security enclaves for another purpose.

In order to enforce this policy, we need to update the `permissions.xml` file and re-sign it before launching the node.
This can be done by modifying the permissions file by hand, or by using XML templates.

<a id="modify-permissions-xml"></a>

### Modify `permissions.xml`

Begin by making a backup of your permissions files, and open `permissions.xml` for editing:

```
$ cd ~/sros2_demo/demo_keystore/enclaves/talker_listener/talker
$ mv permissions.p7s permissions.p7s~
$ mv permissions.xml permissions.xml~
$ vi permissions.xml
```

We will be modifying the `<allow_rule>` for `<publish>` and `<subscribe>`.
The topics in this XML file use the DDS naming format, not the ROS name.
Find details on mapping topic names between ROS and DDS in the [Topic and Service Names design document](https://design.ros2.org/articles/topic_and_service_names.html#mapping-of-ros-2-topic-and-service-names-to-dds-concepts).

Paste the following XML content into `permissions.xml`, save the file and exit the text editor.
This shows the `chatter` and `rosout` ROS topics renamed to the DDS `rt/chatter` and `rt/rosout` topics, respectively:

```
<dds xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.omg.org/spec/DDS-SECURITY/20170901/omg_shared_ca_permissions.xsd">
  <permissions>
    <grant name="/talker_listener/talker">
      <subject_name>CN=/talker_listener/talker</subject_name>
      <validity>
        <not_before>2021-06-01T16:57:53</not_before>
        <not_after>2031-05-31T16:57:53</not_after>
      </validity>
      <allow_rule>
        <domains>
          <id>0</id>
        </domains>
        <publish>
          <topics>
            <topic>rt/chatter</topic>
            <topic>rt/rosout</topic>
            <topic>rt/parameter_events</topic>
            <topic>*/talker/*</topic>
          </topics>
        </publish>
        <subscribe>
          <topics>
            <topic>rt/parameter_events</topic>
            <topic>*/talker/*</topic>
          </topics>
        </subscribe>
      </allow_rule>
      <allow_rule>
        <domains>
          <id>0</id>
        </domains>
        <publish>
          <topics>
            <topic>ros_discovery_info</topic>
          </topics>
        </publish>
        <subscribe>
          <topics>
            <topic>ros_discovery_info</topic>
          </topics>
        </subscribe>
      </allow_rule>
      <default>DENY</default>
    </grant>
  </permissions>
</dds>
```

This policy allows the talker to publish on the `chatter` and the `rosout` topics.
It also includes publish and subscribe permissions needed for the talker node to manage parameters (a requirement for all nodes).
Discovery permissions remain unchanged from the original template.

<a id="sign-the-policy-file"></a>

### Sign the policy file

This next command creates the new S/MIME signed policy file `permissions.p7s` from the updated XML file `permissions.xml`.
The file must be signed with the Permissions CA certificate, **which requires access to the Permissions CA private key**.
If the private key has been protected, additional steps may be required to unlock and use it according to your security plan.

```
$ openssl smime -sign -text -in permissions.xml -out permissions.p7s \
  --signer permissions_ca.cert.pem \
  -inkey ~/sros2_demo/demo_keystore/private/permissions_ca.key.pem
```

<a id="launch-the-node"></a>

### Launch the node

With the updated permissions in place, we can launch the node successfully using the same command used in prior tutorials:

```
$ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker
```

However, attempting to remap the `chatter` topic prevents the node from launching (note that this requires the `ROS_SECURITY_STRATEGY` set to `Enforce`).

```
$ ros2 run demo_nodes_cpp talker --ros-args --enclave /talker_listener/talker \
  --remap chatter:=not_chatter
```

<a id="use-the-templates"></a>

### Use the templates

Security policies can quickly become confusing, so the `sros2` utilities add the ability to create policies from templates.
Do this by using the [sample policy file](https://github.com/ros2/sros2/blob/jazzy/sros2/test/policies/sample.policy.xml#L1) provided in the `sros2` repository.
Let’s create a policy for both the `talker` and the `listener` to only use the `chatter` topic.

Begin by downloading the `sros2` repository with the sample policy files:

```
$ git clone https://github.com/ros2/sros2.git /tmp/sros2
```

Then use the `create_permission` verb while pointing to the sample policy to generate the XML permission files:

```
$ ros2 security create_permission demo_keystore \
  /talker_listener/talker \
  /tmp/sros2/sros2/test/policies/sample.policy.xml
$ ros2 security create_permission demo_keystore \
  /talker_listener/listener \
  /tmp/sros2/sros2/test/policies/sample.policy.xml
```

These permission files allow nodes to only publish or subscribe to the `chatter` topic, and enable communications required for parameters.

In one terminal with security enabled as in previous security tutorials, run the `talker` demo program:

```
$ ros2 run demo_nodes_cpp talker --ros-args -e /talker_listener/talker
```

In another terminal do the same with the `listener` program:

```
$ ros2 run demo_nodes_py listener --ros-args -e /talker_listener/listener
```

At this point, your `talker` and `listener` nodes will be communicating securely using explicit access control lists.
However, the following attempt for the `listener` node to subscribe to a topic other than `chatter` will fail:

```
$ ros2 run demo_nodes_py listener --ros-args --enclave /talker_listener/listener \
  --remap chatter:=not_chatter
```

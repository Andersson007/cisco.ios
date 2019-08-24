#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for ios_lacp_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}


DOCUMENTATION = """
---
module: ios_lacp_interfaces
version_added: 2.9
short_description: Manage Link Aggregation Control Protocol (LACP) on Cisco IOS devices interface.
description: This module provides declarative management of LACP on Cisco IOS network devices lacp_interfaces.
author: Sumit Jaiswal (@justjais)
notes:
  - Tested against Cisco IOSv Version 15.2 on VIRL.
  - This module works with connection C(network_cli),
    See L(IOS Platform Options,../network/user_guide/platform_ios.html).
options:
  config:
      description: A dictionary of LACP lacp_interfaces option
      type: list
      elements: dict
      suboptions:
        name:
          description:
          - Name of the Interface for configuring LACP.
          type: str
          required: True
        port_priority:
          description:
          - LACP priority on this interface.
          - Refer to vendor documentation for valid port values.
          type: int
        fast_switchover:
          description:
          - LACP fast switchover supported on this port channel.
          type: bool
        max_bundle:
          description:
          - LACP maximum number of ports to bundle in this port channel.
          - Refer to vendor documentation for valid port values.
          type: int
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""

EXAMPLES = """

# Using merged
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown

- name: Merge provided configuration with device configuration
  ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
        port_priority: 10
      - name: GigabitEthernet0/2
        port_priority: 20
      - name: GigabitEthernet0/3
        port_priority: 30
      - name: Port-channel10
        fast_switchover: True
        max_bundle: 5
    state: merged

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
#  lacp max-bundle 5
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

# Using overridden
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: Override device configuration of all lacp_interfaces with provided configuration
  ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
        port_priority: 20
      - name: Port-channel10
        max_bundle: 2
    state: overridden

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp max-bundle 2
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown

# Using replaced
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp max-bundle 5
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: Replaces device configuration of listed lacp_interfaces with provided configuration
  ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/3
        port_priority: 40
      - name: Port-channel10
        fast_switchover: True
        max_bundle: 2
    state: replaced

# After state:
# ------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
#  lacp max-bundle 2
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 40

# Using Deleted
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  flowcontrol receive on
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: "Delete LACP attributes of given interfaces (Note: This won't delete the interface itself)"
  ios_lacp_interfaces:
    config:
      - name: GigabitEthernet0/1
    state: deleted

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured LLDP module attributes)"
#
# Before state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
#  lacp fast-switchover
# interface Port-channel20
#  lacp max-bundle 2
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
#  lacp port-priority 10
# interface GigabitEthernet0/2
#  shutdown
#  lacp port-priority 20
# interface GigabitEthernet0/3
#  shutdown
#  lacp port-priority 30

- name: "Delete LACP attributes for all configured interfaces (Note: This won't delete the interface itself)"
  ios_lacp_interfaces:
    state: deleted

# After state:
# -------------
#
# vios#show running-config | section ^interface
# interface Port-channel10
# interface Port-channel20
# interface Port-channel30
# interface GigabitEthernet0/1
#  shutdown
# interface GigabitEthernet0/2
#  shutdown
# interface GigabitEthernet0/3
#  shutdown

"""

RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface GigabitEthernet 0/1', 'lacp port-priority 30']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.argspec.lacp_interfaces.lacp_interfaces import (
    Lacp_InterfacesArgs,
)
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.config.lacp_interfaces.lacp_interfaces import (
    Lacp_Interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Lacp_InterfacesArgs.argument_spec,
        supports_check_mode=True,
    )

    result = Lacp_Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()

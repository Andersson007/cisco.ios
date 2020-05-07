#!/usr/bin/python
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
"""
The module file for ios_lldp_global
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {"metadata_version": "1.1", "supported_by": "Ansible"}
DOCUMENTATION = """module: ios_lldp_global
short_description: LLDP global resource module
description: This module configures and manages the Link Layer Discovery Protocol(LLDP)
  attributes on IOS platforms.
version_added: 1.0.0
author: Sumit Jaiswal (@justjais)
notes:
- Tested against Cisco IOSv Version 15.2 on VIRL
- This module works with connection C(network_cli), See L(IOS Platform Options,../network/user_guide/platform_ios.html).
options:
  config:
    description: A dictionary of LLDP options
    type: dict
    suboptions:
      holdtime:
        description:
        - LLDP holdtime (in sec) to be sent in packets.
        - Refer to vendor documentation for valid values.
        type: int
      reinit:
        description:
        - Specify the delay (in secs) for LLDP to initialize.
        - Refer to vendor documentation for valid values.
        - NOTE, if LLDP reinit is configured with a starting value, idempotency won't
          be maintained as the Cisco device doesn't record the starting reinit configured
          value. As such, Ansible cannot verify if the respective starting reinit
          value is already configured or not from the device side. If you try to apply
          starting reinit value in every play run, Ansible will show changed as True.
          For any other reinit value, idempotency will be maintained since any other
          reinit value is recorded in the Cisco device.
        type: int
      enabled:
        description:
        - Enable LLDP
        type: bool
      timer:
        description:
        - Specify the rate at which LLDP packets are sent (in sec).
        - Refer to vendor documentation for valid values.
        type: int
      tlv_select:
        description:
        - Selection of LLDP TLVs i.e. type-length-value to send
        - NOTE, if tlv-select is configured idempotency won't be maintained as Cisco
          device doesn't record configured tlv-select options. As such, Ansible cannot
          verify if the respective tlv-select options is already configured or not
          from the device side. If you try to apply tlv-select option in every play
          run, Ansible will show changed as True.
        type: dict
        suboptions:
          four_wire_power_management:
            description:
            - Cisco 4-wire Power via MDI TLV
            type: bool
          mac_phy_cfg:
            description:
            - IEEE 802.3 MAC/Phy Configuration/status TLV
            type: bool
          management_address:
            description:
            - Management Address TLV
            type: bool
          port_description:
            description:
            - Port Description TLV
            type: bool
          port_vlan:
            description:
            - Port VLAN ID TLV
            type: bool
          power_management:
            description:
            - IEEE 802.3 DTE Power via MDI TLV
            type: bool
          system_capabilities:
            description:
            - System Capabilities TLV
            type: bool
          system_description:
            description:
            - System Description TLV
            type: bool
          system_name:
            description:
            - System Name TLV
            type: bool
  state:
    description:
    - The state of the configuration after module completion
    type: str
    choices:
    - merged
    - replaced
    - deleted
    default: merged
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
# vios#sh running-config | section ^lldp
# vios1#


- name: Merge provided configuration with device configuration
  cisco.ios.ios_lldp_global:
    config:
      holdtime: 10
      enabled: true
      reinit: 3
      timer: 10
    state: merged

# After state:
# ------------
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run


# Using replaced

# Before state:
# -------------
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run


- name: Replaces LLDP device configuration with provided configuration
  cisco.ios.ios_lldp_global:
    config:
      holdtime: 20
      reinit: 5
    state: replaced

# After state:
# -------------
# vios#sh running-config | section ^lldp
#  lldp holdtime 20
#  lldp reinit 5


# Using Deleted without any config passed
#"(NOTE: This will delete all of configured LLDP module attributes)"

# Before state:
# -------------
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run


- name: "Delete LLDP attributes (Note: This won't delete the interface itself)"
  cisco.ios.ios_lldp_global:
    state: deleted

# After state:
# -------------
# vios#sh running-config | section ^lldp
# vios1#
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: dict
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: dict
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['lldp holdtime 10', 'lldp run', 'lldp timer 10']
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.argspec.lldp_global.lldp_global import (
    Lldp_globalArgs,
)
from ansible_collections.cisco.ios.plugins.module_utils.network.ios.config.lldp_global.lldp_global import (
    Lldp_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
    ]
    module = AnsibleModule(
        argument_spec=Lldp_globalArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Lldp_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()

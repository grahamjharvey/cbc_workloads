#!/usr/bin/env python
# *******************************************************
# Copyright (c) VMware, Inc. 2020. All Rights Reserved.
# SPDX-License-Identifier: MIT
# *******************************************************
# *
# * DISCLAIMER. THIS PROGRAM IS PROVIDED TO YOU "AS IS" WITHOUT
# * WARRANTIES OR CONDITIONS OF ANY KIND, WHETHER ORAL OR WRITTEN,
# * EXPRESS OR IMPLIED. THE AUTHOR SPECIFICALLY DISCLAIMS ANY IMPLIED
# * WARRANTIES OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY,
# * NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.

"""Example script listing Workloads"""

import sys
import csv
from cbc_sdk.helpers import build_cli_parser, get_cb_cloud_object
from cbc_sdk.workload.vm_workloads_search import ComputeResource

def main():
    """Main function of the List Workloads script."""
    parser = build_cli_parser("List Workloads")
    #parser.add_argument("-q", "--query", help="Query string for looking for Workloads")

    args = parser.parse_args()
    cbc = get_cb_cloud_object(args)

    query = cbc.select(ComputeResource)
    #if args.query:
    #    query = query.where(args.query)
    #else:
    devices = list(query)

    cols = [
    "appliance_uuid",
    "cluster_name",
    "created_at",
    "datacenter_name",
    "eligibility",
    "eligibility_code",
    "esx_host_name",
    "esx_host_uuid",
    "host_name",
    "id",
    "installation_status",
    "installation_status_code",
    "ip_address",
    "name",
    "os_architecture",
    "os_description",
    "os_type",
    "uuid",
    "vcenter_host_url",
    "vcenter_name",
    "vcenter_uuid",
    "vmwaretools_version"
    ]

    with open('vSphere_unmanaged_device_list.csv', 'w') as outfile:
        outfile = csv.writer(outfile, quoting=csv.QUOTE_ALL)
        outfile.writerow(cols)
        
        for device in devices:
            device_details = [
                device.appliance_uuid,
                device.cluster_name,
                device.created_at,
                device.datacenter_name,
                device.eligibility,
                device.eligibility_code,
                device.esx_host_name,
                device.esx_host_uuid,
                device.host_name,
                device.id,
                device.installation_status,
                device.installation_status_code,
                device.ip_address,
                device.name,
                device.os_architecture,
                device.os_description,
                device.os_type,
                device.uuid,
                device.vcenter_host_url,
                device.vcenter_name,
                device.vcenter_uuid,
                device.vmwaretools_version
            ]
            outfile.writerow(device_details)

if __name__ == "__main__":
    sys.exit(main())

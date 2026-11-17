# Network troubleshooting and evolution

[Home](../README.md) · [Current architecture](../architecture/current/README.md)

Moving the server services to Proxmox introduced a physical network path between the VMware endpoint and the monitoring VM. I worked through several configurations before validating the shared-VLAN baseline.

| Stage | Finding | What I could conclude |
|---|---|---|
| Initial VMware lab | Windows detection worked in Lab 01 | Endpoint-to-SIEM detection was possible before the later network changes |
| Migration to Proxmox | Wazuh and Shuffle ran on the mini PC; Windows connectivity became a separate issue | Linux-event automation could be tested independently |
| ER605 experiments | Proxmox-side router ping succeeded; Windows/iMac-side gateway tests failed | Partial router connectivity, not a complete routed path |
| Subnet overlap | macOS selected a VMware private bridge for the physical-router destination | Actual routing and ARP required inspection; an Up adapter was insufficient |
| Shared-VLAN baseline — 16 Nov 2026 | Ports 2/3 used untagged VLAN 122; Windows reached Wazuh and the agent became Active | A working local Windows-to-Wazuh connection |

The earlier ER605 experiments do not have a sufficiently clear relative timeline to supersede the dated baseline. I treat them as troubleshooting findings, not proof of the current routed configuration.

## Lessons learned

- Physical link, access membership and PVID need to agree before route changes are useful.
- Overlapping physical and VMware-private subnets can send traffic down the wrong path.
- A selected route does not prove ARP resolution or a router response.
- Source-bound ping can still use an unexpected egress path.
- Temporary host routes are diagnostic tools, not a substitute for a coherent addressing design.
- Local connectivity and policy-controlled segmentation require different tests.

[Read-only diagnostics](troubleshooting.md) · [Planned segmented architecture](../architecture/planned-design/README.md)

# Project history

[Home](../README.md) · [Engineering notes](engineering-notes.md)

My lab has developed from individual platform experiments into a connected monitoring and automation environment.

| Milestone | Work completed | Remaining boundary |
|---|---|---|
| Windows detection — 3 Nov 2026 | Collected Sysmon events and validated custom Wazuh rule `100101` | Negative testing and broader coverage assessment |
| SOAR webhook — 7 Nov 2026 | Submitted a synthetic alert and completed a Shuffle workflow | Automatic forwarding was outside this first test |
| Live automation — 9 Nov 2026 | Forwarded a real Linux journal alert through Wazuh into Shuffle | Windows-originated automation still requires its own test |
| Endpoint connectivity — 16 Nov 2026 | Verified Windows-to-Wazuh connectivity, an active agent and raw event collection on shared VLAN 122 | Routed segmentation remains unfinished |
| Caldera platform — dashboard record 16 Nov 2026 | Captured the 5.3.0 dashboard | No enrolled agents or operations in the recorded view |
| Portfolio documentation — 17 Nov 2026 | Organised case studies, architecture, reproduction guides and publication checks | New results will receive dated follow-up entries |

Wazuh and Shuffle were moved from VMware Fusion to Proxmox during the project. Windows 11, Caldera and Windows Server remain recorded on the iMac's VMware environment. The [network history](network-history.md) describes the connectivity issues encountered during that evolution.

The [case studies](../README.md#featured-work) contain validated outcomes. The [build guides](build-guide/README.md) explain reproduction procedures and do not imply that every setup command has a retained execution record.

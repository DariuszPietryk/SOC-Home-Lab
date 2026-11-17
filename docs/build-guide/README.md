# Build this SOC lab

[Home](../../README.md)

These guides explain how to reproduce the lab architecture and tests, with the relevant machine, prerequisites and checkpoints identified. The case studies record my dated results; a reproduction procedure does not imply that every installation command has a retained execution record. Configuration snippets use placeholders for local substitution.

| Step | Guide | Checkpoint |
|---|---|---|
| 00 | [Plan and prepare](00-preparation.md) | Equipment, capacity, snapshots and local addressing plan |
| 01 | [Proxmox host and VMs](01-proxmox.md) | Management works; guest inventory created |
| 02 | [Switch and Proxmox networking](02-networking.md) | Lab access ports and bridge agree |
| 03 | [VMware Fusion and Windows network](03-vmware.md) | Windows can connect to Wazuh TCP 1514 |
| 04 | [Wazuh installation](04-wazuh.md) | Manager, indexer and dashboard running |
| 05 | [Windows, Sysmon and Wazuh agent](05-windows-telemetry.md) | Sysmon process creation and active agent |
| 06 | [Validate event collection](06-event-collection.md) | Local event, manager ingestion and alert are checked separately |
| 07 | [Encoded PowerShell detection](07-detection.md) | Custom rule and harmless test reproduced |
| 08 | [Shuffle installation and webhook](08-shuffle.md) | Sample alert reaches completed execution |
| 09 | [Live Wazuh → Shuffle](09-live-automation.md) | Actual Linux event reaches workflow |
| 10 | [Caldera installation](10-caldera.md) | UI loads; credentials remain private |
| 11 | [Validation and maintenance](11-validation.md) | Results recorded and temporary diagnostics cleaned up |

The shared-VLAN baseline is a troubleshooting stage. Do not run emulation until segmentation and authorised targets have been verified. [Intended network policy](../../architecture/network-policy.md).

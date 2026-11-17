# Hardware and VM inventory

[Home](../README.md) · [Current architecture](current/README.md)

I use an iMac for the VMware guests and a separate mini PC for the monitoring/automation VMs. This inventory records my documented configuration as of 17 November 2026; resource values refer to the dated lab notes rather than a live hypervisor export.

## Physical equipment

| Equipment | Role | Recorded details / limitation |
|---|---|---|
| Intel iMac | macOS management and VMware Fusion host | 3 GHz six-core Intel Core i5; 40 GB DDR4 2667 MHz |
| BOSGAME mini PC | Proxmox VE host | Ryzen 5 3500U; 16 GB physical RAM and 512 GB NVMe recorded; later upgrade not verified |
| TP-Link managed switch | Physical SOC connectivity | VLANs 121/122 defined; ports 2/3 shared untagged VLAN 122 in the dated working setup |
| Dedicated iMac USB Ethernet | VMware physical lab bridge | AX88179B / TP-Link UE306 referenced during adapter troubleshooting |
| Separate Proxmox USB Ethernet | Physical uplink for `vmbr1` | Device-specific MAC-derived interface name omitted |
| TP-Link ER605 | Intended inter-VLAN routing and access policy | Partial setup tested; full Windows-side and routed connectivity unresolved |
| Synology DS118 | Possible backup/evidence storage | Personal storage is outside emulation scope; mounted shares and backup integration not verified |

The early proposal placed everything on one host. The implemented deployment splits workloads between Proxmox and VMware Fusion.

## Existing VMs — five distinct roles

| VM / ID | Host | Guest / software | Resources in historical notes | Purpose and verified boundary |
|---|---|---|---|---|
| Wazuh SIEM / 110 | Proxmox | Ubuntu; Wazuh 4.14.9 recorded in exercise evidence | Around 8 GB RAM noted; actual vCPU/disk not confirmed | Central components; rules `100101` and `100102`; Windows ingestion verified |
| Shuffle SOAR / 120 | Proxmox | Ubuntu; Docker-based Shuffle; Tools 1.2.0 used in historical tests | Around 6 GB RAM noted; actual vCPU/disk not confirmed | Simulated webhook and real Linux-event integration demonstrated |
| Windows 11 / `WIN11-SOC` | VMware Fusion | Windows 11 Pro; Sysmon; Wazuh agent 4.14.9 recorded | 2 vCPU / 6 GB RAM recorded in Lab 01 | Endpoint telemetry and encoded PowerShell test; active agent verified later |
| MITRE Caldera | VMware Fusion | Linux VM; dashboard displays Caldera 5.3.0 | Actual allocation not recorded; installation guide proposes a reproduction allocation | Dashboard loaded; screenshot has 0 agents and 0 operations |
| Windows Server 2025 | VMware Fusion | Windows Server 2025 Desktop Experience recorded | Actual allocation not confirmed | Intended AD DS and DNS; promotion, domain, address and migration not verified |

VM names and IDs are educational inventory labels. Personal usernames, machine MACs, real addresses and domain names are omitted.

## Optional future machines and services

| Addition | Intended use | Status |
|---|---|---|
| Linux endpoint | Linux authentication and persistence detection tests | Planned; no separate endpoint recorded |
| Alert queue / broker | Buffer events if a concrete reliability need appears | Optional proposal; no deployed VM/container evidenced |
| Network IDS / case management | Later packet visibility or investigation tracking | Possible future work; not deployed |

## Inventory conventions

New or changed VMs receive a dated entry with host, guest version, resource allocation and validation outcome. Proposed roles remain separate from deployed services. Actual addresses and credentials stay in private records.

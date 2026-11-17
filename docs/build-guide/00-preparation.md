# 00 — Prepare the lab

[Guide index](README.md) · [Next: Proxmox](01-proxmox.md)

1. Read the [inventory](../../architecture/inventory.md) and [current architecture](../../architecture/current/README.md). Preserve macOS on the iMac; Proxmox belongs on the separate mini PC in this implementation.
2. Back up anything needed from the intended Proxmox installation disk. The installer replaces the selected disk's contents. Keep personal storage outside the test scope.
3. Record management and lab addresses privately. Use a non-overlapping lab subnet and identify physical adapters. Do not reuse a subnet already attached to a VMware private bridge.
4. Obtain Proxmox, an Ubuntu server ISO, Windows 11 and Windows Server installation media from their official sources. Check vendor checksums and use appropriate licences/evaluation terms.
5. Review available CPU, RAM and storage. Historical Wazuh/Shuffle allocations together approach the capacity of a 16 GB mini PC. Run workloads in stages; do not assume allocation equals observed consumption.
6. Keep a working management connection and console access before network changes. Plan rollback and snapshot guests before major service/configuration changes.
7. Prepare local-only credential storage. Passwords, enrollment keys, webhook URLs and generated configuration files never belong in the public repo.

**Checkpoint:** equipment and disk identified, local address plan written, management recovery path available. No software installation is implied by finishing the plan.

Official starting points: [Proxmox downloads](https://www.proxmox.com/en/downloads), [Ubuntu Server](https://ubuntu.com/download/server), [Windows 11](https://www.microsoft.com/software-download/windows11), [Windows Server evaluation](https://www.microsoft.com/evalcenter/evaluate-windows-server-2025).

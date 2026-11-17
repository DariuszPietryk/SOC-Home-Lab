# 01 — Proxmox host and server VMs

[Guide index](README.md) · [Next: networking](02-networking.md)

**Run on:** mini PC / Proxmox console. Installation is needed only for a new host; do not reinstall a working host to follow this guide.

1. Write the official Proxmox ISO to an installation USB. Boot the mini PC from it and select the intended internal disk only after backup.
2. Follow the installer for region, time zone, a unique administrator password and a management address on the trusted management network. Do not publish installer captures or credentials.
3. Reboot into Proxmox. From a trusted management browser open `https://PROXMOX_MANAGEMENT_IP:8006`. Verify the host identity before accepting its local certificate.
4. Apply host updates using the repository configuration appropriate to your installation. Record the installed version privately; do not disable repository signature checks.
5. Upload an Ubuntu server ISO to ISO-capable storage. Create a Wazuh VM (historical ID 110) and a Shuffle VM (historical ID 120), with disk capacity suitable for logs, snapshots and Docker data. IDs are local choices.
6. Use the [Wazuh quickstart](https://documentation.wazuh.com/current/quickstart.html) for supported guest OS and sizing. Allocate capacity based on workload; the old lab notes are not official minimums. Finish the lab bridge before attaching server VMs to it.
7. Install Ubuntu in each guest. Use separate local credentials, SSH only on an intended management path, and snapshots before platform installation.

Read-only host checks:

```bash
pveversion
free -h
pvesm status
qm list
qm config 110
qm config 120
```

Inspect output locally; it can reveal MACs and configuration identifiers. Confirm the actual VM IDs before commands. If migrating existing VMs, follow the [migration checklist](../migration-and-offline-images.md) rather than creating duplicate service instances.

**Checkpoint:** Proxmox management reachable, storage checked, Ubuntu guests available. A running guest does not prove Wazuh or Shuffle is installed.

Reference: [Proxmox administration guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.html).

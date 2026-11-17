# Lab network policy and address placeholders

[Home](../README.md) · [Inventory](inventory.md)

All addresses below are symbolic. Replace values locally; do not publish a private addressing inventory. VLAN numbers, bridge labels and ports describe educational topology rather than secrets.

| Placeholder | Local meaning |
|---|---|
| `WAZUH_LAB_IP` | Wazuh manager/dashboard lab address |
| `SHUFFLE_LAB_IP` | Shuffle lab address |
| `CALDERA_LAB_IP` | Caldera VM address, after placement is verified |
| `PROXMOX_MANAGEMENT_IP` | Management-only address |
| `LAB_USB_NIC` | Actual Proxmox USB interface; obtain using `ip -br link` |
| `LAB_MAC_INTERFACE` | Actual dedicated macOS interface; obtain using `networksetup -listallhardwareports` |
| `LAB_BRIDGE_IP_CIDR` | Optional local bridge address with prefix; omit if host access is unnecessary |

## Intended minimum flows

| Source | Destination | Protocol / purpose | Status |
|---|---|---|---|
| Windows agent | Wazuh manager | TCP 1514, telemetry | Verified on shared VLAN |
| New agent during enrollment | Wazuh manager | TCP 1515 if automatic enrollment is used | Permit only as required; verify enrollment method |
| Authorised analyst | Wazuh dashboard | TCP 443 | Windows browser verified |
| Wazuh manager | Shuffle | TCP 3001 HTTP in historical local test, or configured HTTPS endpoint | Linux-event integration demonstrated historically |
| Authorised administrator | Caldera | TCP 8888 in the documented setup | UI screenshot available; cross-host path not verified |
| Approved Caldera agent | Caldera | Configured contact channel only | Planned; do not open all contact ports |
| Lab workloads | Home devices / NAS / host management | Deny unless a specific approved management path requires it | Must be tested; no completed isolation claim |

SSH and Proxmox administration belong to trusted management paths; they are not blanket allowances from attack endpoints. Wazuh API and indexer ports are not needed for normal agent event delivery. No public inbound port forwarding is part of this design.

Keep IPv4 and IPv6 policy consistent. Log outcomes, test both directions where relevant, and restore temporary outbound update access after installation.

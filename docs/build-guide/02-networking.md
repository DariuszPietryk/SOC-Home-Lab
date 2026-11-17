# 02 — Switch and Proxmox lab bridge

[Guide index](README.md) · [Next: VMware](03-vmware.md)

**Run on:** switch administration UI and Proxmox. Keep local console/recovery access and the management connection available.

## Recreate the dated shared-VLAN baseline

1. Identify the dedicated iMac lab adapter and separate Proxmox lab adapter physically. Keep Proxmox management on its existing interface / `vmbr0`.
2. In the TP-Link switch's 802.1Q VLAN page, create VLAN 122 if absent. Configure **port 2** (iMac) and **port 3** (Proxmox lab NIC) as **untagged** members.
3. Set both ports' **PVID to 122**. Review other untagged VLAN membership according to the switch model; avoid accidental dual access membership. Save the configuration.
4. On Proxmox inspect interfaces with `ip -br link`. Identify the lab USB NIC by cable/link testing. Interface names differ per device.
5. In **Node → System → Network**, create or edit Linux bridge `vmbr1`, bridge port = your dedicated lab NIC. No lab default gateway is needed for the local test. An optional bridge address enables deliberate host-to-lab diagnostics; it does not enable routing by itself.
6. Compare the [example bridge stanza](../../configs/proxmox/vmbr1.example) with your local configuration. Preserve `vmbr0` and its gateway. Apply changes from a recovery-capable session.
7. Attach Wazuh and Shuffle guest network adapters to `vmbr1`. With this untagged access-port model, do not add guest VLAN tags unless redesigning the uplink as a trunk.
8. Configure distinct guest addresses on the same chosen lab subnet. Keep the full address plan private. Verify locally with `ip -br address` and `ip route`.

**Checkpoint:** physical link, switch untagged membership, PVID, bridge uplink and guest adapter agree. Continue with Windows to test the actual path.

## Intended segmentation later

Moving Windows to VLAN 121 requires a verified router connection, gateways and explicit firewall permissions. Follow the [planned design](../../architecture/planned-design/README.md). The documented ER605 experiments did not establish working Windows-side routing. Do not copy those experimental routes as a final configuration.

Reference: [Proxmox network configuration](https://pve.proxmox.com/wiki/Network_Configuration). Switch menu names vary by hardware revision; use your exact model's official manual.

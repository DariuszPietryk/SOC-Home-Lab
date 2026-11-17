# 03 — VMware Fusion and Windows lab networking

[Guide index](README.md) · [Next: Wazuh](04-wazuh.md)

**Run on:** iMac VMware Fusion and Windows 11. Wazuh must be running for the final connectivity test; complete Step 04 first if installing from scratch.

1. Create/install Windows 11 in VMware Fusion using official media and the supported virtual hardware for your host. Retain the existing Windows guest if already configured.
2. Shut down or disconnect the guest network while changing adapters. In its network settings select a **specific bridged dedicated USB Ethernet adapter**, not automatic bridging to the home connection.
3. Connect that adapter to the switch's VLAN 122 access port. Avoid simultaneously using a host-only network with an overlapping subnet.
4. In Windows configure a unique static IPv4 address and mask within the same local subnet as Wazuh. The successful local test had **no default gateway**. Add DNS/gateway only when needed by a deliberate routed design.
5. Keep Windows Defender Firewall active. Do not disable it to solve a ping failure. Outbound TCP delivery and inbound ICMP are different paths.
6. Run in Windows PowerShell:

```powershell
Get-NetAdapter | Format-Table Name, Status, LinkSpeed
Get-NetIPConfiguration
$WazuhIp = Read-Host 'Wazuh lab address'
Test-NetConnection $WazuhIp -Port 1514
```

An optional `ping $WazuhIp` tests ICMP separately. Expected service-path result: `TcpTestSucceeded : True`. If the service is not installed yet, finish Step 04 before treating a closed port as a VLAN failure.

7. From the Windows browser open `https://WAZUH_LAB_IP` with the real address substituted locally. Verify the certificate identity and log in privately.

**Checkpoint:** Windows-to-Wazuh service path works. A VMware adapter reporting Up, or successful ping alone, does not establish Wazuh agent enrollment.

If traffic uses a VMware private bridge unexpectedly, see [network history](../network-history.md) and [diagnostics](../troubleshooting.md).

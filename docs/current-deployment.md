# Deployment snapshot

[Home](../README.md) · [Architecture](../architecture/current/README.md) · [Inventory](../architecture/inventory.md)

**Documentation date:** 17 November 2026. **Latest network baseline in this record:** 16 November 2026.

My server services run on Proxmox, while the Windows endpoint and other VMware guests are recorded on the iMac. The shared-VLAN test established Windows-to-Wazuh connectivity through the dedicated adapters.

| Area | Recorded outcome | Remaining work |
|---|---|---|
| Windows → Wazuh | TCP 1514, active agent, dashboard access and raw telemetry collection | Revalidate after routing changes |
| Application Event 101 | Event reached the manager archive | Custom alert not yet validated |
| Wazuh → Shuffle | Live Linux-event integration validated 9 Nov | Windows-originated delivery and current-runtime retest |
| Caldera | 5.3.0 dashboard access recorded 16 Nov | Agent, operation, placement and detection validation |
| Windows Server 2025 | VMware guest and Desktop Experience installation recorded | AD DS/DNS and domain tests |
| ER605 | Partial configuration and troubleshooting | Complete endpoint/server routed-policy validation |

A dated test result is not continuous service-health monitoring. [Network history](network-history.md) separates earlier router experiments from the successful shared-VLAN baseline. The [roadmap](roadmap.md) tracks the next validation steps.

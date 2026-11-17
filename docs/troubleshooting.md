# Troubleshooting index

[Home](../README.md)

| Symptom | First check | Next reference |
|---|---|---|
| Windows cannot reach Wazuh | Link → switch membership/PVID → guest bridge → local subnet → service listener | [Network setup](build-guide/02-networking.md) |
| macOS uses VMware private bridge | Inspect actual route; remove subnet overlap through a planned reconfiguration | [Network history](network-history.md) |
| Ping fails but agent works | ICMP policy differs from TCP 1514; inspect intended service path | [Network policy](../architecture/network-policy.md) |
| Agent Pending / Disconnected | Manager address, service, TCP 1514, enrollment and agent log | [Windows setup](build-guide/05-windows-telemetry.md) |
| Sysmon Event 1 absent | Start a new process and inspect local channel before server changes | [Lab 01 troubleshooting](../labs/01-encoded-powershell-detection/TROUBLESHOOTING.md) |
| Wazuh search has no results | Applied filter, time range and raw-event versus alert distinction | [Collection guide](build-guide/06-event-collection.md) |
| Rule 100101 absent | Parent 92057, command line and loaded custom rule | [Detection guide](build-guide/07-detection.md) |
| Logtest says no decoder | One event per line; correct live decoding context | [Lab 01 troubleshooting](../labs/01-encoded-powershell-detection/TROUBLESHOOTING.md) |
| Shuffle HTTP 200, execution stuck | Starting action, worker/app images and Orborus state | [Lab 02 troubleshooting](../labs/02-shuffle-webhook-test/docs/troubleshooting.md) |
| Localhost port does not respond | Localhost belongs to the current machine; distinguish SSH tunnel and VM service port | [Offline/migration notes](migration-and-offline-images.md) |
| Caldera UI blank | Build assets, configured frontend URL and private server logs | [Caldera install guide](../platforms/mitre-caldera/INSTALLATION.md) |

## Read-only diagnostics

On Proxmox/Linux:

```bash
ip -br link
ip -br address
ip route
sudo ss -lntp
```

On macOS, identify the dedicated interface and substitute the target address locally:

```bash
networksetup -listallhardwareports
route -n get TARGET_LAB_IP
```

A packet capture can help distinguish route selection, ARP and service traffic; capture only the intended lab interface/target, stop promptly, and keep the raw output private. Do not post full route, interface, Docker, journal or configuration dumps to public issues.

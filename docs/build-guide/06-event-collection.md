# 06 — Verify collection before detection

[Guide index](README.md) · [Next: detection](07-detection.md)

Verify three distinct stages: **local event → manager collection → alert**. A Dashboard with no matching alert does not prove an event was never collected.

1. On Windows, start a new benign process and confirm Sysmon Event 1 locally as in Step 05.
2. Ensure the Wazuh agent is Active and its log confirms reading the channel.
3. In Wazuh Threat Hunting use a suitable time range, apply the query, and inspect a returned event's provider/decoder. An example filter is:

```text
data.win.system.providerName: "Microsoft-Windows-Sysmon"
```

Threat Hunting normally shows alerts. Events that do not match an alerting rule may not appear there.

## Optional Application marker

From elevated Windows PowerShell:

```powershell
eventcreate /T INFORMATION /ID 101 /L APPLICATION /SO SOC-LAB-TEST /D "SOC Lab archive verification test 101"
Get-WinEvent -FilterHashtable @{LogName='Application'; Id=101} -MaxEvents 3 |
    Select-Object TimeCreated, Id, ProviderName
```

Ensure the Application channel is included in the agent's existing collection configuration. The recorded Event 101 reached the manager archive; a custom Event 101 alert remains unvalidated. Reserve a new rule ID before writing that detector.

## Temporary raw-event verification

Only when collection needs diagnosis, back up the manager configuration privately, set `<logall_json>yes</logall_json>` in the existing `<global>` block, validate with `sudo /var/ossec/bin/wazuh-analysisd -t`, then restart `wazuh-manager`. Inspect `/var/ossec/logs/archives/archives.json` locally for the marker. Raw logs contain detailed endpoint data; do not copy them here.

Return `logall_json` to its previous value after diagnosis, validate/restart, and handle existing diagnostic archives under your local retention policy. Disabling the option does not delete old archives.

**Checkpoint:** record what stage was verified. Raw archive presence is not a detection result. Never leave temporary high-volume archiving enabled accidentally.

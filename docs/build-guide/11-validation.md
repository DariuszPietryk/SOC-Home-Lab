# 11 — Validate and maintain the lab

[Guide index](README.md) · [Add another exercise](../../CONTRIBUTING.md)

## After a setup change

| Check | Where | Success means |
|---|---|---|
| Link, VLAN and bridge membership | Switch, Proxmox, VMware | Physical and virtual attachments match the intended design |
| TCP 1514 | Windows → Wazuh | Manager service reachable |
| Agent Active | Wazuh Dashboard | Agent connection established |
| Sysmon Event 1 | Windows | Local process telemetry exists |
| Manager-side collection | Wazuh local logs/archive if needed | Event arrived; not necessarily an alert |
| Positive and negative detection tests | Windows + Wazuh | Match/absence assessed against test scope |
| Real automation test | Linux + Wazuh + Shuffle | Marker correlated across alert and finished execution |
| Denied traffic | Each lab zone | Expected forbidden paths fail according to the designed policy |
| Reboot recovery | One guest at a time | Network/services return after planned restart |

Do not scan home networks as a shortcut. Test only the approved sources, destinations and ports in your own local validation plan. A failed ping alone is insufficient evidence of isolation.

## Finish the session

1. Restore temporary raw-event archiving and outbound installation access to intended settings.
2. Preserve configurations and secrets in private backups; retain only reviewed public evidence here.
3. Record software versions, test date and outcome. Note failed/unfinished tests explicitly.
4. Update [inventory](../../architecture/inventory.md), [architecture](../../architecture/current/README.md), [rule register](../rule-register.md), [roadmap](../roadmap.md) and [changelog](../../CHANGELOG.md) as relevant.
5. Run `python3 scripts/check_repo.py` from the repo root and inspect the staged Git diff before pushing.
6. If credentials were accidentally committed, rotate them and remove them from Git history; deleting the working file alone is insufficient.

Documentation checks verify file integrity and publication hygiene. Running-service validation is recorded separately in dated lab results.

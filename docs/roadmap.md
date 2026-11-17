# Roadmap

[Project home](../README.md)

## Completed milestones

- [x] Collect Windows/Sysmon telemetry and validate custom PowerShell rule `100101`.
- [x] Complete a synthetic alert workflow in Shuffle.
- [x] Forward a real Linux journal alert from Wazuh into Shuffle.
- [x] Verify Windows-to-Wazuh connectivity and collection on shared VLAN 122.
- [x] Record access to the Caldera 5.3.0 dashboard.

## Current focus

My next iterations strengthen test coverage and complete the links between the existing components.

- [ ] Run and record Lab 01's negative test and assess false positives.
- [ ] Verify the intended raw-event retention settings after diagnostic archiving.
- [ ] Revalidate service versions, runtime and reboot recovery.
- [ ] Resolve ER605/VMware overlap and validate routed VLAN 121/122 policy.
- [ ] Test lab-to-home/management deny paths before emulation.
- [ ] Validate a new Application Event 101 detection with an unused rule ID.
- [ ] Demonstrate a Windows-originated alert reaching Shuffle automatically.

## Planned case studies

| Exercise | Intended outcome | Completion evidence |
|---|---|---|
| Controlled Caldera test | Correlate one benign operation with Sysmon/Wazuh | Authorised target, actual operation record and observed detection outcome |
| Windows domain lab | Develop AD DS/DNS and authentication-monitoring skills | Verified domain configuration, client join and audit events |
| SOAR triage | Turn an alert into a useful investigation summary | Tested branching, action output and failure handling |
| Optional Linux endpoint | Expand Linux detection coverage | Separate endpoint collection and reproducible positive/negative tests |

These are planned outcomes, not completed capabilities. An alert queue remains optional and will only be introduced if a buffering/reliability requirement appears. Future work follows the [exercise conventions](../CONTRIBUTING.md).

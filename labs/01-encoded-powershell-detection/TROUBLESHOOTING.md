# Lab 01 — Troubleshooting and rule refinement

[Case study](README.md)

**Test date:** 3 November 2026. Screenshot and VM time zones may differ.

## Agent connectivity

The agent initially showed Pending. A Windows `Test-NetConnection` to manager TCP 1514 succeeded, which established a service connection but did not prove successful enrollment. The agent later became Active; I did not isolate one definitive cause for the earlier Pending state.

## Local event generation and collection

My first Sysmon Event 1 query returned no events. Running `Write-Output` inside an existing PowerShell process is not a reliable test of new process creation. Launching a new process with `Start-Process notepad.exe` produced useful local process telemetry; Event IDs 1 and 5 were later visible.

The agent configuration included the Sysmon Operational channel with `eventchannel` format. After restart, its log showed that the channel was being read. I then inspected a Wazuh alert with provider `Microsoft-Windows-Sysmon`, a process-create event and decoder `windows_eventchannel`.

Those checks established different stages: opening a channel for reading was not by itself proof of manager ingestion.

## Dashboard search issues

Some early searches showed only general Windows events. A Sysmon query was initially typed without being applied; another filter contained only `data.win.system.channel` without a value. Neither established a forwarding failure.

Applying the filter and inspecting an event confirmed the provider. Threat Hunting primarily presents alerts, so an unalerted raw event may still be absent from that view even when collected.

## Built-in match and custom-rule mismatch

The benign encoded test triggered built-in rule `92057`, level 12. My initial rule tested event-channel/provider/process fields, but I did not observe the custom alert. An intermediate variant using `<if_group>sysmon_event1</if_group>` also did not produce a recorded custom match.

Rule hierarchy was a plausible contributor, but I did not prove that it was the only cause.

## Logtest input and decoding context

Pasting formatted multi-line JSON caused separate lines to be treated as individual events and produced decoder failures. Logtest requires one complete event per line.

A synthetic one-line event decoded as `json` but did not produce a Phase 3 match. It lacked the live Windows event-channel context, so this result did not settle whether the live custom rule worked.

Configuration validation showed no visible errors, although its exit code was not retained in the original test record. Indexer retry, duplicate agent-key and content-update warnings also appeared; I did not establish that they caused the custom detection problem.

## Working refinement

I changed rule `100101` to inherit from the already observed `92057` branch, matched `-EncodedCommand` in `win.eventdata.commandLine`, and set level 13. After manager reload and another benign test, two custom alerts appeared at **20:29:20.799** and **20:29:58.277**.

[Final rule](detections/soc_lab_rules.xml) · [Recorded result](evidence/24-custom-rule-100101-success.png)

## Follow-up work

- Run the [negative test](tests/negative_test.ps1) and record the time range and outcome.
- Inspect command line, executable, parent process and ATT&CK mapping in the matched event.
- Test legitimate encoded-command use and alternate patterns to assess false positives and coverage.
- Investigate unrelated warnings separately rather than assuming they caused the mismatch.

Public screenshots are limited to the selected detection result. Raw logs and operational identifiers remain private.

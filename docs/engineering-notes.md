# Engineering notes

[Home](../README.md)

## Split-host deployment

I run the monitoring and automation services on Proxmox while keeping the Windows endpoint and the other VMware guests on the iMac. This uses the two existing hosts, but adds a physical networking dependency: virtual bridges, dedicated adapters, switch access membership and guest configuration all have to agree.

The mini PC's recorded memory capacity also makes resource planning relevant. The historic Wazuh and Shuffle allocations approach the host's physical RAM, so a proposed additional service is not treated as automatically deployable.

## Detect from observed telemetry

In [Lab 01](../labs/01-encoded-powershell-detection/README.md), the built-in rule `92057` matched before my custom rule did. I extended that confirmed branch with rule `100101` and then repeated the harmless test. The custom rule generated alerts.

That dependency defines the detector's coverage: an event must reach the parent rule as well as match the custom command-line condition. I have not established that this detects every use of encoded PowerShell, and negative/false-positive testing remains open.

## Validate ingestion and execution separately

My first Shuffle test used a manually submitted Wazuh-shaped payload. It verified the webhook/workflow path, not Wazuh integration. [Lab 03](../labs/03-live-wazuh-shuffle-automation/README.md) then used a real Linux journal marker so I could validate automatic forwarding independently.

Similarly, a Wazuh Logtest rule match does not dispatch a live integration alert, and HTTP 200 does not establish that the workflow finished. I use the expected marker and timestamps to correlate the stages.

## Investigate quiet failures

During the offline Shuffle work, an app container exited with code 0 but did no work. The app image contained an empty `/app/app.py`. After rebuilding and transferring a working image, I repeated the webhook test and obtained a finished execution.

The lesson was to inspect image contents and worker behaviour rather than treating a successful process exit as proof of a successful application action.

## Treat connectivity and segmentation as separate outcomes

Putting the two physical lab access ports in shared VLAN 122 established the Windows-to-Wazuh baseline. It did not validate routed traffic between endpoint VLAN 121 and server VLAN 122, or complete isolation from the home network.

Earlier ER605 work also exposed overlapping VMware and physical subnets. Inspecting the selected route and actual egress was more useful than assuming that an Up adapter or a source-bound ping proved the intended path.

## Make limitations part of the result

I distinguish local event creation, agent connectivity, manager collection, rule matching and completed automation. The case studies identify the stage validated and the tests still needed. My next iterations focus on negative testing, routed policy, Windows-to-Shuffle delivery and a controlled Caldera exercise.

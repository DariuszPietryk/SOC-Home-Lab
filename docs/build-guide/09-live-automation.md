# 09 — Live Wazuh to Shuffle automation

[Guide index](README.md) · [Next: Caldera](10-caldera.md)

**Prerequisites:** a working Shuffle webhook, running Wazuh manager and local Ubuntu journal collection. This is the Linux-event test actually demonstrated in Lab 03. Windows-to-Shuffle is a separate future exercise.

1. On the Wazuh VM check for rule ID `100102` conflicts, back up local rules privately, then install the lab rule from the repository root:

```bash
sudo install -m 0640 -o root -g wazuh labs/03-live-wazuh-shuffle-automation/rules/soc_lab03_rules.xml /var/ossec/etc/rules/soc_lab03_rules.xml
sudo /var/ossec/bin/wazuh-analysisd -t
sudo /var/ossec/bin/wazuh-logtest
```

2. At the Logtest prompt paste this single line, then finish the session with Ctrl+D:

```text
Nov 09 19:07:36 wazuh soclab03[4102]: SOC_LAB_03_TEST alert forwarding validation
```

Expected rule `100102`, level `10`. A rule match here does not itself dispatch an integration alert.

3. Privately back up `/var/ossec/etc/ossec.conf`. Merge [the integration example](../../configs/wazuh/shuffle-integration.example.xml) into its existing `<ossec_config>` and replace the dummy hook with the actual private webhook URL **only in the local configuration**.
4. Confirm the manager collects journald. If absent, merge [the journald example](../../configs/wazuh/journald.example.xml) without duplicating existing collection. Collection from syslog instead may require the appropriate existing localfile configuration for that system.
5. Validate and apply:

```bash
sudo /var/ossec/bin/wazuh-analysisd -t
sudo /var/ossec/bin/wazuh-integratord -t
```

Only if checks succeed, restart the manager and verify `systemctl is-active wazuh-manager`.

6. Generate the real event on the Wazuh Ubuntu VM:

```bash
logger -t soclab03 'SOC_LAB_03_TEST automatic forwarding to Shuffle'
journalctl -t soclab03 --since '5 minutes ago' --no-pager
```

7. Confirm a new `100102` alert in Wazuh, then a new Shuffle execution with the same harmless marker and expected action output. Use event times to distinguish this test from older executions.
8. If delivery fails, check the alert first, integration filter second, network access third, then Shuffle trigger/start-node/worker state. Inspect logs privately because they may contain hooks or authentication material.

[Lab 03 evidence and limitations](../../labs/03-live-wazuh-shuffle-automation/README.md). Reference: [Wazuh external API integration](https://documentation.wazuh.com/current/user-manual/manager/integration-with-external-apis.html).

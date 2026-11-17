# 07 — Encoded PowerShell detection

[Guide index](README.md) · [Next: Shuffle](08-shuffle.md)

**Prerequisite:** Steps 04–06. This exercise uses a harmless command that prints a marker; it is for the authorised disposable Windows VM.

1. Read [Lab 01](../../labs/01-encoded-powershell-detection/README.md). Its rule `100101` is a **child of built-in rule 92057**; parent-rule matching is required. It is not a standalone detector for every encoded command.
2. From the repository root on the Wazuh VM, copy the lab rule into the local rules directory after checking for an ID/file collision and backing up existing files privately:

```bash
sudo install -m 0640 -o root -g wazuh labs/01-encoded-powershell-detection/detections/soc_lab_rules.xml /var/ossec/etc/rules/soc_lab_rules.xml
sudo /var/ossec/bin/wazuh-analysisd -t
```

3. If validation exits successfully, run `sudo systemctl restart wazuh-manager` and confirm it is active. Restore the backup if validation fails; do not restart with invalid configuration.
4. Copy the two harmless test files to the Windows VM through your approved local transfer method. From their directory run:

```powershell
.\encoded_powershell_positive.ps1
```

Use an approved script-signing/execution-policy workflow if local policy blocks the file. Do not disable security controls globally.

5. Apply `rule.id: 100101` in Wazuh with the correct time range. Inspect the process command line, agent, rule ID and level. Historical evidence shows two level-13 custom matches.
6. Run `./negative_test.ps1` from PowerShell, then compare results. Record the exact time window and any unexpected matches. This is a proposed validation step, not a previously demonstrated negative result.
7. Document versions and limitations. If no custom match appears, check Sysmon Event 1, parent rule `92057`, rule loading, and command-line field content in that order.

See [Lab 01 troubleshooting](../../labs/01-encoded-powershell-detection/TROUBLESHOOTING.md). `wazuh-logtest` expects one complete event per line; a synthetic JSON object may not reproduce the live Windows event-channel decoding context.

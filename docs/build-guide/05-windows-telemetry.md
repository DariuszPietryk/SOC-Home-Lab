# 05 — Windows, Sysmon and Wazuh agent

[Guide index](README.md) · [Next: collection validation](06-event-collection.md)

**Run on:** Windows 11 lab VM, elevated PowerShell where required. Keep Windows Firewall enabled.

## Sysmon

1. Download Sysmon from [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon). Extract into a local working directory and inspect the package/signature.
2. Open an elevated PowerShell in that directory. The minimal installation below enables default monitoring, including process creation; use an appropriate reviewed policy when expanding coverage:

```powershell
.\Sysmon64.exe -accepteula -i
Get-Service Sysmon*
Start-Process notepad.exe
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1} -MaxEvents 3 |
    Select-Object TimeCreated, Id, ProviderName
```

If Sysmon is already installed, inspect its service and configuration instead of reinstalling. Do not change broad logging filters without understanding event volume and coverage.

## Wazuh agent

3. In Wazuh Dashboard select the agent-deployment flow for Windows, enter the actual manager lab address, and download/run the generated installer command **locally**. This avoids publishing a version-specific installer URL or enrollment secret. Match agent/manager compatibility using the [Windows installation guide](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html).
4. Give the disposable lab endpoint a generic role name such as `WIN11-SOC`. Privately verify that its manager address is correct.
5. Locate the installed agent's `ossec.conf` (typically under `C:\Program Files (x86)\ossec-agent\`). Back it up locally. Merge the block from [the Sysmon example](../../configs/wazuh/windows-sysmon.example.xml) inside the existing `<ossec_config>` section; avoid duplicate blocks. Preserve the existing client/enrollment configuration.
6. Restart the agent:

```powershell
Restart-Service WazuhSvc
Get-Service WazuhSvc
```

7. In Dashboard verify the agent becomes **Active**. Inspect local agent logs for collection of `Microsoft-Windows-Sysmon/Operational`. Do not publish `client.keys`, agent authentication material or full configuration exports.

**Checkpoint:** local Sysmon Event 1 exists and the agent is active. Confirm manager-side collection next.

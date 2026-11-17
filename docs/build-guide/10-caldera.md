# 10 — MITRE Caldera platform

[Guide index](README.md) · [Next: validation](11-validation.md)

Use the detailed [Caldera installation guide](../../platforms/mitre-caldera/INSTALLATION.md): prepare a dedicated Linux VM, install prerequisites, clone the 5.3.0 release and plugin submodules, create a Python virtual environment, install dependencies, build the UI, configure private credentials and verify access.

The [platform page](../../platforms/mitre-caldera/README.md) contains the reviewed login/dashboard images. The dashboard shows **version 5.3.0, 0 agents and 0 operations**. No completed emulation or Wazuh detection from Caldera is claimed.

Before the first operation:

1. Verify VM placement, allowed network paths and denied access to personal devices.
2. Snapshot the disposable authorised target.
3. Verify Sysmon and Wazuh baseline collection.
4. Choose one benign technique and define its expected telemetry, cleanup and stop condition.
5. Enroll only the intended lab endpoint using privately handled agent configuration.
6. Record actual operation outcome and observed telemetry/alerts in a new numbered lab.

Do not mark that future exercise complete based on a dashboard alone. Keep agent payload URLs, keys, operation exports and generated server configuration out of GitHub.

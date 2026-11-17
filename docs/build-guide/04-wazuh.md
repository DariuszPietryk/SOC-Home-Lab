# 04 — Install and verify Wazuh

[Guide index](README.md) · [Next: Windows telemetry](05-windows-telemetry.md)

**Run on:** a new supported Ubuntu Wazuh VM. Do not rerun the installer on the working service as a troubleshooting step. The historical exercise records 4.14.9; the reproduction uses the documented 4.14 installer family and does not assert a particular patch will be installed.

1. Read the [official quickstart](https://documentation.wazuh.com/current/quickstart.html) for compatible OS, capacity and current requirements. Provide controlled outbound access for installation; remove it afterwards according to your policy.
2. Download the installation assistant from the vendor and inspect it locally before execution:

```bash
curl --fail --show-error --location --output wazuh-install.sh https://packages.wazuh.com/4.14/wazuh-install.sh
less wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```

3. Store the generated credentials and installation archive privately. Never copy the generated password archive into this repository.
4. Verify services:

```bash
sudo systemctl is-active wazuh-manager wazuh-indexer wazuh-dashboard
sudo ss -lntp
sudo /var/ossec/bin/wazuh-analysisd -t
```

5. Open `https://WAZUH_LAB_IP` from an authorised lab browser. Validate the expected certificate identity; use your generated account credentials.
6. Record installed component versions locally. Follow vendor guidance for controlling updates; upgrades should be deliberate and snapshot-backed. Do not claim the installed patch matches old evidence without checking it.
7. Permit required telemetry/enrollment traffic only from intended endpoints. Dashboard/API/indexer access are separate permissions; see [network policy](../../architecture/network-policy.md).

**Checkpoint:** manager, indexer and dashboard active; authorised dashboard login succeeds. A running dashboard does not prove endpoint telemetry.

For existing migrated installations, preserve configuration, certificates, agent keys, indexer state and backups privately. Use the [migration notes](../migration-and-offline-images.md).

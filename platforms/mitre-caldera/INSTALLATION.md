# Installing MITRE Caldera 5.3.0 on an Ubuntu Lab VM

[← Caldera dashboard and evidence](README.md)

> **Reproduction reference:** This guide follows the Caldera 5.3.0 installation/configuration documentation and uses a Python virtual environment. The recorded lab result is the running dashboard; this page is not a retained command-by-command installation log.

## 1. Prepare the isolated VM

Create an Ubuntu Linux VM in VMware Fusion (or another supported hypervisor). Give the lab VM at least **2 vCPUs and ideally 8 GB RAM**, subject to available resources. Take a VM snapshot before installation. Assign a network connection that permits authorised local access only; **do not bridge Caldera directly to your home LAN or expose it to the Internet**.

If packages must be downloaded, provide **temporary, tightly controlled outbound access** and remove it when finished. Verify the VM's actual IP address, subnet and interface rather than reusing an address from another SOC component.

Version 5.3.0 documentation lists Linux/macOS, Python **3.8+**, Node.js **16+** for the v5 UI, `pip`, and browser support. Actual dependency requirements may evolve between releases; use the pinned version for a reproducible lab.

## 2. Install base tools and verify versions

On Ubuntu, run:

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv nodejs npm
python3 --version
node --version
npm --version
```

**Important:** Some Ubuntu releases may provide an older Node.js. If `node --version` reports a version below 16, install a supported Node.js 16+ release from its official distribution instructions before continuing. Do not assume that `apt install nodejs` always provides a sufficiently recent version.

## 3. Clone the Caldera release with plugins

Use the **5.3.0 release** (rather than a moving development branch):

```bash
git clone --recursive --branch 5.3.0 https://github.com/mitre/caldera.git
cd caldera
```

The recursive option is important because Caldera plugins use Git submodules. If the folder has already been cloned without them, in the existing Caldera checkout run:

```bash
git submodule update --init --recursive
```

## 4. Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Using a virtual environment avoids installing Caldera's Python dependencies into the system interpreter. If the dependency installation fails, keep the full error and refer to the official troubleshooting guide; do not blindly run unknown installation scripts as root.

## 5. Start Caldera and build the web UI

On the **first launch**, while inside the `caldera` directory with the virtual environment active:

```bash
python3 server.py --build
```

The `--build` flag builds the Vue UI; subsequent normal starts generally do not need it unless UI or plugin assets change:

```bash
python3 server.py
```

**Avoid `--insecure` for a lasting installation.** Caldera documents this option as using its insecure default configuration. For a personal lab, use the generated `conf/local.yml`, restrict network access, and set appropriate credentials.

**Don't use `--fresh` as a routine troubleshooting command**; it resets Caldera's non-plugin stored data.

## 6. Access the dashboard and log in

From a browser **inside the Caldera VM**, visit:

```text
http://localhost:8888
```

From a separate authorised lab computer, use:

```text
http://<CALDERA_LAB_IP>:8888
```

Replace `<CALDERA_LAB_IP>` with the VM's real private IP. The example `0.0.0.0:8888` visible in the dashboard screenshot is the server **bind address**, not a URL to use in a client browser.

Use the Caldera account configured for your installation. In its 5.3.0 documentation, Caldera describes the `red` account and a generated password in `conf/local.yml`; **read credentials locally and never publish the file**. If access or UI requests fail, inspect `conf/local.yml` only locally and check `app.frontend.api_base_url` per the official configuration guide.

## 7. Validate the service and capture evidence

While the Caldera server is running, from a terminal inside the VM:

```bash
ss -tlnp | grep ':8888'
curl -I http://127.0.0.1:8888
```

A listening process and an HTTP response support that the local web endpoint is running. After signing in, capture the dashboard showing the version and counters. The recorded dashboard shows **Caldera 5.3.0; 0 agents; 0 operations; 2109 abilities; 29 adversaries**.

Keep these screenshots free of credentials, browser profile details and sensitive URLs.

## 8. Safe operation and shutdown

- Restrict Caldera to **isolated, explicitly authorised** endpoints.
- Do not install agents on your Mac host, home router, NAS or production systems.
- Running a dashboard does **not** prove adversary operations or Wazuh integration.
- Stop a manually launched Caldera server with **Ctrl+C** in the terminal.
- Activate the virtual environment again if starting from a new terminal: `source .venv/bin/activate`.
- Do not copy `conf/local.yml` to GitHub. Keep private credentials and operation records private.

## Troubleshooting pointers

| Symptom | Check |
|---|---|
| Plugin or module missing | Confirm the recursive clone and `git submodule update --init --recursive` |
| UI blank / requests fail | Re-run first-launch `--build` if appropriate; inspect `app.frontend.api_base_url` in the private local config |
| Port 8888 not available | Confirm Caldera is running and nothing else has bound the port |
| Browser cannot open the VM IP | Check VM IP, routing, VLAN and host firewall **without opening Caldera to the home LAN** |
| Credentials unknown | Check the generated local configuration privately; do not paste its contents into a public issue |

## Authoritative references

- [Caldera 5.3.0 installation documentation](https://caldera.readthedocs.io/en/v5.3.0/Installing-Caldera.html)
- [Caldera 5.3.0 server configuration](https://caldera.readthedocs.io/en/5.3.0/Server-Configuration.html)
- [Caldera 5.3.0 troubleshooting](https://caldera.readthedocs.io/en/5.3.0/Troubleshooting.html)

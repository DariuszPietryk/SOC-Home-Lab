# 08 — Install Shuffle and test a webhook

[Guide index](README.md) · [Next: live automation](09-live-automation.md)

**Run on:** dedicated Ubuntu Shuffle VM. The original tests used Shuffle Tools 1.2.0. New installations may use a different supported Shuffle release; record it and validate the action inputs rather than claiming identical runtime behaviour.

## New installation

1. Install Docker Engine and the Compose plugin using the [official Ubuntu instructions](https://docs.docker.com/engine/install/ubuntu/). Confirm `docker --version` and `docker compose version`. Use a controlled installation/update window.
2. Read the [Shuffle install guide](https://github.com/Shuffle/Shuffle/blob/main/.github/install-guide.md) and [configuration guide](https://shuffler.io/docs/configuration). Clone upstream into a separate local service directory, outside this portfolio:

```bash
git clone https://github.com/Shuffle/Shuffle.git
cd Shuffle
git rev-parse HEAD
```

3. Review upstream `.env` and Compose files locally. Configure your actual lab hostname and private unique credentials/encryption values before first start. Do not copy those files into this repo. Record the upstream revision and image digests privately; avoid claiming a moving branch is a fixed build.
4. Follow the chosen release's database prerequisites. The documented local deployment uses a writable database directory and an increased map count:

```bash
mkdir -p shuffle-database
sudo chown -R 1000:1000 shuffle-database
sudo sysctl -w vm.max_map_count=262144
```

Review the selected release's OpenSearch swap requirements and available VM memory; apply any required swap changes deliberately inside this guest. Do not make host-wide changes on Proxmox to satisfy a guest prerequisite.

5. Start and inspect the stack:

```bash
sudo docker compose up -d
sudo docker compose ps
```

6. Open `http://SHUFFLE_LAB_IP:3001` only through your permitted lab path, or use configured HTTPS. Create your own admin account privately. Verify backend, Orborus, worker and required app image availability.

## Workflow and sample test

7. Create a workflow with a **Webhook** trigger connected to **Shuffle Tools → Repeat back to me**. Set its required input to execution data using the UI picker (`$exec` in the historical lab). Set the starting action, save and start the webhook.
8. Copy the private hook URL locally. From a Bash terminal on an authorised lab machine, read it without putting the literal secret in shell history:

```bash
read -r -s -p 'Private webhook URL: ' SHUFFLE_WEBHOOK_URL
export SHUFFLE_WEBHOOK_URL
printf '\n'
bash labs/02-shuffle-webhook-test/scripts/send-test-alert.sh
unset SHUFFLE_WEBHOOK_URL
```

Run the script from the portfolio repository root, not the upstream Shuffle directory. It uses the included harmless JSON. The historical helper accepts common local HTTP lab destinations; review it if your HTTPS endpoint needs support rather than submitting a public URL accidentally.

9. Verify the HTTP request succeeded **and** a new workflow execution finished with successful action output. HTTP 200 alone does not prove execution.

[Lab 02](../../labs/02-shuffle-webhook-test/README.md) records the successful simulated test. For offline image transfer and the empty app-image finding, see [migration/offline notes](../migration-and-offline-images.md).

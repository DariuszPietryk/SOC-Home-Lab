# Troubleshooting notes — SOC Lab 02

The following cases were encountered during the VMware-to-Proxmox migration and offline Shuffle deployment.

| Symptom | Root cause or finding | Resolution / diagnostic |
| --- | --- | --- |
| `curl: (7) Failed to connect to 127.0.0.1 port 8081` from `soar@soar` | `8081` is the iMac's SSH tunnel, not the Ubuntu VM's listener | Use `http://<SHUFFLE_LAB_IP>:3001` **from the Shuffle VM**, retaining the generated webhook path |
| Webhook returned to Uninitialized | Shuffle configuration still contained old VMware network values | Backed up `.env`, updated the known hostname references, recreated affected backend and Orborus containers, verified webhook remained Running |
| HTTP 500 `Startnode isn't defined in this workflow` | Workflow had no usable first action | Connected webhook to an action and explicitly configured the workflow start node |
| HTTP 400 with `{"success":false}` | Workflow request rejected; no specific reason in JSON body | Checked trigger state, workflow configuration and backend logs; fixed workflow and retested |
| HTTP 200 but execution `EXECUTING` | Runtime/app image problems, not ingestion | Inspected worker and app service separately |
| Orborus reports missing worker or App SDK | Images unavailable in offline Proxmox VM | Downloaded on internet-connected VM, transferred with `docker save`/`scp`/`docker load` |
| Tenzir `registry-1.docker.io` DNS failure | Optional component attempted download without internet | Treated separately from the basic webhook test; did not expose SOC network just to pull Tenzir |
| Docker Swarm service `shuffle-tools_1-2-0` at `0/3` | Tasks exited immediately with code `0` | Found the bad image's `/app/app.py` had **0 bytes** |
| App image `python app.py --log-level DEBUG` exits `0`, no logs | Python executes empty script | Rebuilt app image using source with `119112`-byte `src/app.py` and the Dockerfile, imported repaired image |
| Service `0/0` | Deliberately scaled to zero during diagnosis | Verified repaired image then re-enabled a single replica for retesting |
| Execution `ABORTED` | Prior temporary abort action or manually aborted test | Replaced it with Shuffle Tools `Repeat back to me` and retested |
| Execution `FINISHED` | Successful end-to-end synthetic event processing | Recorded start 19:42:40 / finish 19:42:42 on 2026-11-07 |

## Commands for diagnostic reference

```bash
sudo docker compose ps
sudo docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
sudo docker service ls
sudo docker service ps --no-trunc shuffle-tools_1-2-0
sudo docker service logs --tail 50 shuffle-tools_1-2-0
sudo docker logs --tail 50 shuffle-orborus
```

### Inspecting a suspected broken app image

```bash
sudo docker run --rm --entrypoint sh \
  frikky/shuffle:shuffle_tools_1.2.0 \
  -c 'wc -c /app/app.py'
```

### Check installed image tags

```bash
sudo docker images --format '{{.Repository}}:{{.Tag}}' | grep -E 'shuffle|frikky'
```

**Do not** publish real webhook URLs, API keys, `.env` files or full unredacted screenshots. **Do not** use `docker compose down -v` during troubleshooting: that risks deleting persistent data.

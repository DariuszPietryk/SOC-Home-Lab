# VM migration and offline Shuffle dependencies

[Home](../README.md)

## Migration checklist

I moved Wazuh and Shuffle from VMware Fusion to Proxmox. The checklist below captures the operational considerations; disk import/conversion depends on the actual source format and is not covered as a universal command sequence.

1. Inventory guest versions, disk formats, firmware type, CPU/memory, network adapters and dependencies locally.
2. Back up each guest and its application data before copying or importing a disk. Shut down the source guest for a consistent disk copy, or use a supported application-aware backup.
3. Check Proxmox storage capacity and snapshot headroom. Import a copy using the supported Proxmox method for the actual source disk format; preserve the original until recovery is verified.
4. Preserve Wazuh certificates, enrollment keys, rules, configurations and indexer data privately. For Shuffle preserve persistent Docker data and encryption settings; losing the encryption secret can make stored credentials unusable.
5. Start the migrated guest on the intended lab bridge; verify device names, address configuration and routes locally. Do not start old/new copies simultaneously with duplicate addresses or service identity.
6. Update only configuration that actually changed. Shuffle's old hostname references caused webhook problems during this migration; review private `.env`, backend and Orborus settings.
7. Validate the application, reboot recovery and backups before retiring the source copy.

## Controlled offline Docker transfer

Run downloads on a designated internet-enabled staging machine, then transfer only the required images. Substitute the exact image tag or digest used by the selected release. The commands below are templates, not literal image names:

```bash
docker pull IMAGE_REFERENCE
docker save --output shuffle-images.tar IMAGE_REFERENCE
shasum -a 256 shuffle-images.tar
```

Transfer privately using your approved file-transfer method. On the Shuffle VM compare the checksum, then:

```bash
sudo docker load --input shuffle-images.tar
sudo docker images --digests
sudo docker compose ps
```

Archive files are operational material, not portfolio content. Pin/record architecture and digests so the destination can run the image. No production credentials should be baked into transferred images.

## Historical app-image finding

An old Shuffle Tools image exited successfully without doing work. Inspection found an empty `/app/app.py`. The lab rebuilt/imported a repaired image and retested with one action. This was a specific historical image problem, not proof that every current image has the defect.

Inspect actual installed image names; the historical notes contain both `shuffle-tools` and `shuffle_tools` spellings, which are different tags. Use `docker images` and the service configuration rather than assuming one.

See [Lab 02 diagnostics](../labs/02-shuffle-webhook-test/docs/troubleshooting.md). Do not use `docker compose down -v` as routine diagnosis because it can destroy persistent data.

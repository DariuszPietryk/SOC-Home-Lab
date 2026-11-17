# Publication safety

- Never publish your full Shuffle webhook URL or ID: it functions like an access token. Rotate it if exposed.
- Never publish `client.keys`, `.env`, passwords, certificates, or SSH keys.
- Do not post unredacted `ossec.conf`, raw `alerts.json` dumps, terminal histories, or logs containing customer data.
- Review future screenshots for usernames, IP addresses, agent IDs, event IDs, and URLs.
- The selected images were cropped and re-encoded without original metadata. A screenshot review cannot guarantee the security of future Git commits or prior public history.
- The project intentionally excludes live IP addresses and all operational secrets.

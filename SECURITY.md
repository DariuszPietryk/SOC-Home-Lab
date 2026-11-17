# Security and evidence policy

This is an educational lab for authorised systems. Personal devices, home infrastructure and storage are outside the emulation scope.

## Public documentation

I publish generic roles, architecture concepts, harmless tests, configuration placeholders and selected reviewed evidence. Credentials, API/enrollment keys, private webhook identifiers, session tokens, personal details, operational addresses, device identifiers and raw logs remain private.

The public evidence set is described in the [privacy review](docs/publication-review.md). Full service configuration, generated password archives, Wazuh agent keys and Caldera `conf/local.yml` are not included.

## Evidence review

New screenshots require full-resolution visual inspection, metadata review and registration of their exact hash. Browser profiles, URLs, prompts, side panels and hidden metadata can disclose information beyond the intended result. Original private evidence is kept separate from public exports.

The publication checker supports this review:

```bash
python3 scripts/check_repo.py
```

It is not a complete secret scanner. `.gitignore` also does not remove files that are already tracked, and a clean working tree does not establish that existing history is free of secrets.

## Credential exposure

An exposed credential must be revoked or rotated, then removed from published material and history using the hosting provider's supported process. Deleting only the current file is insufficient. Public issues must not repeat the exposed value.

## Operational boundaries

Administrative services are restricted to intended management paths. Allowed and denied routes require explicit tests before emulation; a failed ping does not prove isolation. Temporary raw-event archiving and outbound update access are returned to their intended settings after diagnosis.

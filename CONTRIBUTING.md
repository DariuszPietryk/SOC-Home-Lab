# Documentation and contribution conventions

[Project home](README.md) · [Repository workflow](docs/github-setup-and-future-labs.md)

I maintain this repository as a record of my ongoing SOC lab work. Each exercise has a defined objective, reproducible steps, dated results and an explicit account of its limitations.

## Exercise structure

New experiments use the next unused numbered folder under `labs/`. The [exercise template](templates/new-exercise/README.md) provides the starting structure:

```bash
cp -R templates/new-exercise labs/04-short-name
```

The example number is only appropriate while it remains unused. Each lab records:

- Objective, environment, tool versions and prerequisites.
- Actions performed and commands with the relevant machine/shell identified.
- Expected and observed results, including unsuccessful attempts.
- Positive and negative tests, with unexecuted tests marked clearly.
- Reviewed evidence, limitations, cleanup and next steps.

Rules belong in `detections/` or an existing exercise's `rules/` folder; harmless tests belong in `tests/`. New custom rule IDs are recorded in the [rule register](docs/rule-register.md). Architecture and inventory changes are documented after validation.

## Evidence and privacy

Public configuration uses placeholders. Live configuration, raw telemetry, credentials, agent keys, private addressing and VM exports remain outside the repository. New screenshots require full-resolution visual and metadata review before their path and SHA-256 are registered in `docs/reviewed-images.json`.

The review hash identifies exact approved bytes; it does not redact an image or guarantee privacy. The [publication checker](scripts/check_repo.py) verifies the documented file checks:

```bash
python3 scripts/check_repo.py
```

## Historical results

Existing validation dates remain attached to their original results. Retests and changes receive dated follow-up notes rather than silently replacing previous findings. Reproduction guides describe procedures; case studies distinguish completed tests from planned work.

## Technical feedback

Useful issues identify the relevant file, lab or rule, explain the technical concern, and propose a reproducible improvement. Issue reports must exclude private endpoints, credentials and unreviewed logs or images.

## Licensing

Upstream tools retain their respective licences. This repository currently has no separate licence granting reuse of the portfolio material.

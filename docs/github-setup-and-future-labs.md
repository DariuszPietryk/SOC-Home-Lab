# Repository workflow

[Home](../README.md) · [Documentation conventions](../CONTRIBUTING.md)

I keep the lab's case studies, architecture and configuration examples in one repository so the project can grow without losing earlier results.

## Update process

1. Document the experiment and its actual outcome in a numbered lab.
2. Review new evidence and keep operational configuration private.
3. Update inventory, architecture, rule register and roadmap when relevant.
4. Record significant changes in `CHANGELOG.md`.
5. Run documentation/publication checks and inspect the staged diff.

From the repository root:

```bash
python3 scripts/check_repo.py
git diff
git diff --cached
```

Commits describe the concrete change, such as `Document Windows alert forwarding test` or `Update lab network architecture`.

## Validation scope

The local checker covers relative links, XML/JSON syntax, selected sensitive-text patterns, excluded file types and reviewed image hashes. It does not test running VMs or inspect all existing Git history. Manual evidence review remains part of the workflow.

## Repository organisation

Completed exercises retain their dated findings. New platforms receive their own pages, and deployment changes update the [inventory](../architecture/inventory.md). The [exercise template](../templates/new-exercise/README.md) keeps future work consistent with the existing case studies.

Git history is preserved when documentation changes. Credentials are kept out of remote URLs, and actual secrets or live configurations are never used as public examples.

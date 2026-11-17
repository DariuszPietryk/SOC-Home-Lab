# Public evidence and privacy review

[Home](../README.md) · [Security policy](../SECURITY.md)

**Review date:** 17 November 2026.

## Public evidence

The repository includes seven selected screenshots showing detection results, completed Shuffle executions, action output and the Caldera login/dashboard. They were inspected at full resolution and checked for PNG text/EXIF metadata. Their exact bytes are recorded in [the image review manifest](reviewed-images.json).

Generic service/test labels such as `WIN11-SOC`, `wazuh` and `wazuh-siem` remain visible. The Caldera login screen includes public vendor contact text, and its dashboard displays the wildcard bind address `0.0.0.0`. These do not disclose personal accounts or a live host address.

The architecture diagram contains role names, VLAN/bridge labels and documented paths. Configuration examples use symbolic placeholders.

## Kept private

Credentials, enrollment keys, operational addressing, device MACs/serials, detailed network captures, raw logs, full service configurations and VM exports are excluded from public documentation. Broader screenshots that reveal unnecessary operational details are not included.

## Automated checks

The local checker verifies relative Markdown links, XML/JSON syntax, selected sensitive-text patterns, excluded file types and exact reviewed-image hashes. Controlled test cases confirmed rejection of a concrete address, broken link, credential-like assignment and changed image. The sample Bash script also passed syntax checking.

These checks support manual review; they do not identify every possible secret, inspect all existing Git history or validate running services. Infrastructure outcomes are recorded separately in dated case studies.

# Repository Settings

This document records the expected GitHub-side settings for production operation.

## Branch Protection

Target branch:

- `main`

Required status checks:

- `test (3.11)`
- `test (3.12)`

Recommended protection behavior:

- Require branches to be up to date before merging.
- Enforce branch protection for administrators.
- Require linear history.
- Block force pushes.
- Block branch deletion.
- Require conversation resolution before merge.

## Why This Matters

execution-harness is an operating system for execution quality. The repository should therefore protect the quality loop itself:

1. Changes are tested before becoming the production baseline.
2. Template and prompt contracts cannot drift silently.
3. Main branch stays recoverable and audit-friendly.
4. Improvements remain connected to the weekly KPT loop.

## Verification

Local:

```bash
python3 -m pytest -q
```

Remote:

- GitHub Actions workflow: `.github/workflows/pytest.yml`
- Branch protection should require both matrix jobs to pass before merge.

## Applying via API

Use a token with repository Administration write permission:

```bash
GH_TOKEN=... python3 scripts/configure_branch_protection.py
```

Preview the payload without making changes:

```bash
python3 scripts/configure_branch_protection.py --dry-run
```

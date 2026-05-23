#!/usr/bin/env python3
"""Configure production branch protection for this repository.

Requires a GitHub token with repository Administration write permission.
Set GH_TOKEN or GITHUB_TOKEN before running.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

DEFAULT_CONTEXTS = ["test (3.11)", "test (3.12)"]


def build_payload(contexts: list[str]) -> dict[str, object]:
    return {
        "required_status_checks": {
            "strict": True,
            "contexts": contexts,
        },
        "enforce_admins": True,
        "required_pull_request_reviews": None,
        "restrictions": None,
        "required_linear_history": True,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "required_conversation_resolution": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Configure GitHub branch protection for execution-harness."
    )
    parser.add_argument("--repo", default="Ringodzilla/execution-harness")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--context", action="append", dest="contexts")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    contexts = args.contexts or DEFAULT_CONTEXTS
    payload = build_payload(contexts)

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Set GH_TOKEN or GITHUB_TOKEN with Administration write permission.", file=sys.stderr)
        return 2

    url = f"https://api.github.com/repos/{args.repo}/branches/{args.branch}/protection"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        method="PUT",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "execution-harness-branch-protection",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        print(f"GitHub API error: {error.code}", file=sys.stderr)
        print(error.read().decode(), file=sys.stderr)
        return 1

    required = result.get("required_status_checks", {}).get("contexts", [])
    print(f"Updated branch protection for {args.repo}:{args.branch}")
    print(f"Required checks: {', '.join(required)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

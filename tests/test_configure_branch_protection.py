from scripts.configure_branch_protection import DEFAULT_CONTEXTS, build_payload


def test_branch_protection_payload_requires_ci_contexts() -> None:
    payload = build_payload(DEFAULT_CONTEXTS)

    assert payload["required_status_checks"] == {
        "strict": True,
        "contexts": ["test (3.11)", "test (3.12)"],
    }


def test_branch_protection_payload_blocks_risky_main_changes() -> None:
    payload = build_payload(DEFAULT_CONTEXTS)

    assert payload["enforce_admins"] is True
    assert payload["required_linear_history"] is True
    assert payload["allow_force_pushes"] is False
    assert payload["allow_deletions"] is False
    assert payload["required_conversation_resolution"] is True

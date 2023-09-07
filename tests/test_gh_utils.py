from __future__ import annotations

from template_sync.gh_utils import get_gh_headers


def test_get_gh_headers_for_token():
    headers = get_gh_headers("token")
    assert headers == {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer token",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def test_get_gh_headers_for_token_and_version():
    headers = get_gh_headers("token", "2022-11-29")
    assert headers == {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer token",
        "X-GitHub-Api-Version": "2022-11-29",
    }

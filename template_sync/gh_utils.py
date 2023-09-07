import json
import logging
import os

from functools import lru_cache

import requests

from github import Auth
from github import Github


DEFAULT_GH_API_URL = "https://api.github.com"
DEFAULT_GH_API_VERSION = "2022-11-28"

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_token_from_env() -> str:
    if token := os.environ.get("GITHUB_TOKEN"):
        return token

    raise Exception("No GitHub token found in env vars")


@lru_cache(maxsize=1)
def get_github_user():
    auth = Auth.Token(get_token_from_env())
    g = Github(auth=auth)

    user = g.get_user()
    return user


def get_gh_headers(gh_token: str, api_version: str = DEFAULT_GH_API_VERSION) -> dict:
    """
    Returns a dict of headers for use with GitHub API requests.

    :param gh_token: GitHub personal token
    :param api_version: GitHub API version
    :return: dict of headers
    """
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {gh_token}",
        "X-GitHub-Api-Version": api_version,
    }
    return headers


def get_repo_for_user(user: str, repo_name: str) -> json:
    headers = get_gh_headers(get_token_from_env())

    logger.debug(f"Getting repo {repo_name} for user {user.login}")
    request = requests.get(
        f"{DEFAULT_GH_API_URL}/repos/{user.login}/{repo_name}", headers=headers
    )
    logger.debug(f"{request.status_code} for {request.url}")

    return json.loads(request.text)


def repo_from_template(repo_json: json) -> bool:
    return repo_json.get("template_repository") is not None


def get_respositories_to_sync():
    if not (user := get_github_user()):
        raise Exception("Could not get GitHub user")

    repos = user.get_repos()

    for repo in repos:
        repo_json = get_repo_for_user(user, repo.name)
        if repo_from_template(repo_json):
            logger.info(
                "Found template repo"
                f" {repo_json.get('template_repository').get('name')} for {repo.name}"
            )
            yield repo_json

#!/usr/bin/env python3

"""GitHub Organization Client module."""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)

class GithubOrgClient:
    """Client for interacting with GitHub organizations."""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the GithubOrgClient with an organization name."""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Retrieve and memoize the organization details."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        
        """Get the URL for the public repositories
        of the organization."""

        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Retrieve and memoize the repositories payload."""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:

        """Get the list of public repositories,
        optionally filtered by license."""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if a repository has a specific license."""
        assert license_key is not None, "license_key cannot be None"
        try:
            return access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False

""" A nice approach to to downloading GitHub repos.

Previous approaches to downloading GitHub repositories
were set up in parallel on Kubernetes using Redis. This
approach was considered too aggressive by both GitHub and
Google. This approach is meant to be nice.
"""
import csv
import logging
import os
import time
from urllib.parse import urljoin

from okra.repo_mgmt import create_parent_dir, gcloud_clone_or_fetch_repo
from okra.populate_db import persist_repo
from okra.playbooks import local_persistance
from okra.error_handling import (MissingEnvironmentVariableError,
                                 NetworkError,
                                 DirectoryNotCreatedError)


# TODO be nice

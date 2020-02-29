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

from okra.populate_db import persist_repo


# TODO be nice

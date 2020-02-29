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

from okra.repo_mgmt import clone_or_fetch_repo
from okra.populate_db import persist_repo

logger = logging.getLogger(__name__)


def batch_upsert_repos(batch:list, buffer_size:int, sleep:int, ecount_max=10):
    ecount = 0
    for args in batch:
        owner, project, dburl, repopath, repourl = args
        
        try:
            clone_or_fetch_repo(repopath,repourl)
            persist_repo(owner, project, dburl, repopath, buffer_size)
            time.sleep(sleep)
        except Exception as exc:
            print("Exception: {}".format(exc))
            time.sleep(sleep + 30) # backoff for 30 seconds
            ecount += 1

        if ecount == ecount_max:
            logger.error("Max number of errors reached: {}".format(ecount))
            break

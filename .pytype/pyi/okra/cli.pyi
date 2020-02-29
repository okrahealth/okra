# (generated with --quick)

import click.core

batch_upsert_repos: click.core.Command
cli: click.core.Group
click: module
get_latest: click.core.Command
logging: module
persist_cloned_repo: click.core.Command
upsert_repo: click.core.Command

def clone_or_fetch_repo(repo_path, repo_url) -> bool: ...
def enable_log(log_name) -> None: ...
def persist_repo(owner: str, project: str, dburl: str, repopath: str, buffer_size: int) -> None: ...

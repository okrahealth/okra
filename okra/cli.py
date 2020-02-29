""" Command Line Interface utilities for Okra """
import click
import logging

from okra.be_nice import batch_upsert_repos
from okra.repo_mgmt import clone_or_fetch_repo
from okra.populate_db import persist_repo
from okra.logging_utils import enable_log

@click.group()
def cli():
    pass

@cli.command(name='upsert')
@click.argument('owner')
@click.argument('project')
@click.argument('dburl')
@click.argument('repopath')
@click.argument('repourl')
@click.option('--buffer_size', default=int(1e4), help="number of commits before db write")
def upsert_repo(owner, project, dburl, repopath, repourl, buffer_size):
    clone_or_fetch_repo(repopath, repourl)
    persist_repo(owner, project, dburl, repopath, buffer_size)

@cli.command(name='cletch')
@click.argument('repopath')
@click.argument('repourl')
def get_latest(repopath, repourl):
    clone_or_fetch_repo(repopath, repourl)

@cli.command(name='persist')
@click.argument('owner')
@click.argument('project')
@click.argument('dburl')
@click.argument('repopath')
@click.argument('logpath')
@click.option('--buffer_size', default=int(1e4), help="number of commits before db write")
def persist_cloned_repo(owner, project, dburl, repopath, logpath, buffer_size):
    enable_log(logpath)
    persist_repo(owner, project, dburl, repopath, buffer_size)

@cli.command(name='batch-upsert')
@click.argument('batch')
@click.option('--buffer_size', default=int(1e4), help="number of commits before db write")
@click.option('--sleep', default=1, help="number of seconds to sleep between repo requests")
@click.option('--ecount_max', default=10, help="max number of errors before aborting")
def batch_upsert_repos(batch, buffer_size, sleep, ecount_max):
    batch_upsert_repos(batch, buffer_size, sleep, ecount_max)

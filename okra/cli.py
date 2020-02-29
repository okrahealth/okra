""" Command Line Interface utilities for Okra """
import click

from okra.repo_mgmt import clone_or_fetch_repo
from okra.populate_db import persist_repo

@click.group()
def cli():
    pass

@cli.command(name='upsert')
@click.argument('owner')
@click.argument('project')
@click.argument('dburl')
@click.argument('repopath')
@click.argument('repourl')
@click.option('--buffer_size', default=1e4, help="number of commits before db write")
def upsert_repo(owner, project, dburl, repopath, repourl, buffer_size):
    clone_or_fetch_repo(repourl, repopath)
    persist_repo(owner, project, dburl, repopath, buffer_size)

""" Command Line Interface utilities for Okra """
import click

from okra.populate_db import persist_repo

@click.group()
def cli():
    pass

@cli.command(name='persist')
@click.argument('owner')
@click.argument('project')
@click.argument('dburl')
@click.argument('repopath')
@click.option('--buffer_size', default=1e5, help="number of commits before db write")
def clone_pull_repo(owner, project, dburl, repopath, buffer_size):
    persist_repo(owner, project, dburl, repopath, buffer_size)

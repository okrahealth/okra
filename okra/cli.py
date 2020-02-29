""" Command Line Interface utilities for Okra """
import click

from okra.populate_db import populate_db

@click.group()
def cli():
    pass

@cli.command(name='persist')
@click.argument('dirpath')
@click.argument('repo_name')
@click.argument('dburl')
@click.option('buffer_size', default=1e5, help="number of commits before db write")
def clone_pull_repo(dirpath, repo_name, dburl, buffer_size):
    populate_db(dburl, dirpath, repo_name, buffer_size)

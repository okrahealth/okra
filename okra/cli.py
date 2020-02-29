""" Command Line Interface utilities for Okra """
import click

@click.group()
def cli():
    pass

@cli.command(name='persist')
def download_update_repos():
    pass

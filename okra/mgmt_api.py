""" Generate tables for the Okra-API management command

Strategy here is to check a directory for updates, then 
consolidate those into parquet files with datetime in file
name. Those parquet files are then uploaded into the Okra API.
"""
from datetime import datetime
import os
import logging
from urllib.parse import urljoin

import pandas as pd
import pyarrow as pa

from okra.assn4 import get_truck_factor_by_project
from okra.exceptions import UrlJoinError
from okra.models import DataAcessLayer
from okra.settings import REPO_LIST


logger = logging.getLogger(__name__)


def check_urljoin(cache: str, fname: str, fpath: str) -> bool:
    if fpath == fname:

        exp = 'cache: {}, fname: {}, fpath: {}'.\
            format(cache, fname, fpath)
        raise UrlJoinError(expression=exp, message='incorrect urljoin')

    return True


def write_parquet(rd: list, pqcache: str, fname: str) -> bool:

    try:
        df = pd.DataFrame(rd)
        table = pa.Table.from_pandas(df)
        pa.parquet.write_table(table, fname)
        return True

    except Exception as exc:
        logger.exception(exc)
        return False


def read_repolist(fpath: str):
    with open(repo_path, 'r') as infile:
        repos = infile.readlines()

    rd = []
    for repo_id in repos:
        rd.append({'repo_id': repo_id.strip()})
    return rd


def parquet_filename(name: str):
    d = datetime.now()
    ymdhm = d.strftime('%Y%m%d_%H%M')

    pq_filename = name + "_" + ymdhm + ".parquet"
    return pq_filename

# Okra API database table preparation files
#


def tbl_repository(repo_path, cache, pqcache, name='repository') -> str:
    """ Repository table (each repo id in directory) """

    try:
        rd = read_repolist(repo_path)
        pqname = parquet_filename(name=name)
        return write_parquet(rd, pqcache, pqname)

    except Exception as exc:
        logger.exception(exc)


def tbl_repository_metrics(rd: list, pqcache: str, name='repo_metrics'):
    """ RepositoryMetrics table 

    rating is the computed truck factor for a project.
    """
    try:
        dal = DataAccessLayer(dburl)
        dal.connect()
        dal.session = dal.Session()

        results = []
        for item in rd:

            repo_id = item['repo_id']
            owner, project = repo_id.split('/')
            truck_factor, _ = get_truck_factor_by_project(owner, project, dal)

            results.append({
                'repo_id': repo_id,
                'rating': truck_factor,
            })

        dal.session.close()
        pqname = parquet_filename(name=name)
        return write_parquet(results, pqcache, pqname)

    except Exception as exc:
        logger.exception(exc)


def tbl_contributor():
    """ Contributor table """
    pass

# Contributor


# Repository Info

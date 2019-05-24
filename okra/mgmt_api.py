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

from okra.assn4 import (get_truck_factor_by_project,
                        total_number_of_files_by_project,
                        total_number_of_contributors_by_project)
from okra.models import DataAccessLayer, Author, Meta
from okra.proto import okra_api_pb2


logger = logging.getLogger(__name__)

def date_toiso(datetime, timespec='minutes'):
    return datetime.isoformat(timespec=timespec)

def msg_repository_metric():
    msg = okra_api_pb2.RepositoryMetric()

def msg_repository_info(dal: DataAccessLayer):
    """ Compute RepositoryInfo message """
    
    msg = okra_api_pb2.RepositoryInfo()

    q = dal.session.query(
        Meta.owner_name, Meta.project_name, Author.commit_hash,
        Author.authored
    ).join(Author)

    qres = q.all()

    msg.owner_name = qres[0].owner_name
    msg.repo_name = qres[0].project_name
    msg.first_commit_date = date_toiso(qres[0].authored)
    msg.first_commit_hash = qres[0].commit_hash
    msg.last_commit_date = date_toiso(qres[-1].authored)
    msg.last_commit_hash = qres[-1].commit_hash

    return msg
    


    

    

    
    




def tbl_repository_metrics(dburl: str, rd: list, pqcache: str, name='repo_metrics'):
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
            total_number_of_files = total_number_of_files_by_project(owner, project, dal)
            total_number_of_contributors = total_number_of_contributors_by_project(owner, project, dal)

            results.append({
                'repo_id': repo_id,
                'rating': truck_factor,
                'total_number_of_files': total_number_of_files,
                'total_number_of_contributors': total_number_of_contributors
            })

        dal.session.close()
        return results
    
    except Exception as exc:
        logger.exception(exc)


def tbl_contributor():
    """ Contributor table """
    pass

# Contributor


# Repository Info

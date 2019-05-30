""" Generate tables for the Okra-API management command

Strategy here is to check a directory for updates, then 
consolidate those into parquet files with datetime in file
name. Those parquet files are then uploaded into the Okra API.

Metrics are targeting the 'proto/okra_api.proto' interface.
"""
from datetime import datetime
import os
import logging
from urllib.parse import urljoin

import pandas as pd
from sqlalchemy import func

from okra.assn4 import (get_truck_factor_by_project,
                        total_number_of_files_by_project,
                        total_number_of_contributors_by_project)
from okra.models import DataAccessLayer, Author, Meta, Contrib, CommitFile
from okra.proto import okra_api_pb2


logger = logging.getLogger(__name__)

def date_toiso(datetime, timespec='minutes'):
    return datetime.isoformat(timespec=timespec)

def msg_iso_date_aggregation(msg, item, status: str, yearmo: str):
    """ Compute IsoDateAggregation message """

    isodt = msg.isodates.add()
    isodt.yearmo = yearmo
    isodt.commit_hash = item.commit_hash

    isoyr, isowk, isody = item.authored.isocalendar()

    isodt.iso_week = isowk
    isodt.iso_year = isoyr
    isodt.status = status

    return msg  

def msg_repository_info(dal: DataAccessLayer, repo_id: str, yearmo: str):
    """ Compute RepositoryInfo message 

    Note that default behavior for first/last msg_iso_date_aggregation()
    is to use the same msg item for IsoDateAggregation if only one msg
    item exists for a given yearmo. An empty message except for repo_id
    and yearmo will be returned if no commits exist for a given yearmo.
    """

    msg = okra_api_pb2.RepositoryInfo()

    q = dal.session.query(
        Meta.yearmo, Author.commit_hash, Author.authored
    ).join(Author).filter(Meta.yearmo == yearmo)

    qres = q.all()

    if len(qres) == 0:
        msg.repo_id = repo_id
        msg.yearmo = yearmo
        return msg

    msg.repo_id = repo_id
    msg.yearmo = yearmo

    # Set up iso dates (first, last)

    first = qres[0]
    last = qres[-1]

    msg = msg_iso_date_aggregation(msg, item=first, status='first',
                                   yearmo=yearmo)
    msg = msg_iso_date_aggregation(msg, item=last, status='last',
                                   yearmo=yearmo)

    return msg

def msg_repository_metric(dal: DataAccessLayer, repo_id: str, yearmo: str):
    
    msg = okra_api_pb2.RepositoryMetric()

    msg.repo_id = repo_id
    msg.yearmo = yearmo

    # IsoDataAggregation

    q1 = dal.session.query(
        Meta.commit_hash, Meta.yearmo, Author.authored
    ).join(Author).filter(Meta.yearmo == yearmo)

    qres1 = q1.all()

    if len(qres1) == 0:
        return msg

    first = qres1[0]
    last = qres1[-1]

    msg = msg_iso_date_aggregation(msg, first, status='first', yearmo=yearmo)
    msg = msg_iso_date_aggregation(msg, last, status='last', yearmo=yearmo)

    # Author count

    q2 = dal.session.query(
        Meta.commit_hash, Meta.yearmo, Author.name, Author.email
    ).join(Author).filter(Meta.yearmo == yearmo)

    msg.author_count = q2.count()
    
    # Contributor count

    q3 = dal.session.query(
        Meta.commit_hash, Meta.yearmo, Contrib.name, Contrib.email
    ).join(Contrib).filter(Meta.yearmo == yearmo)

    msg.contrib_count = q3.count()

    # File level metrics

    q4 = dal.session.query(
        Meta.yearmo,
        func.count(CommitFile.modified_file).label('file_count'),
        func.sum(CommitFile.lines_added).label('lines_added'),
        func.sum(CommitFile.lines_deleted).label('lines_subtracted')
    ).join(CommitFile).filter(Meta.yearmo == yearmo).group_by(Meta.yearmo)

    qres4 = q4.first() # Should only be one yearmo
    msg.file_count = qres4.file_count
    msg.lines_added = qres4.lines_added
    msg.lines_subtracted = qres4.lines_subtracted

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

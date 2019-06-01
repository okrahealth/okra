""" Generate tables for the Okra-API management command


Metrics are targeting the 'proto/okra_api.proto' interface.
"""
from datetime import datetime
import os
import logging
from urllib.parse import urljoin

from sqlalchemy import func

from okra.assn4 import (get_truck_factor_by_project,
                        total_number_of_files_by_project,
                        total_number_of_contributors_by_project)
from okra.bus_factor import get_bus_factor
from okra.models import DataAccessLayer, Author, Meta, Contrib, CommitFile
from okra.proto import okra_api_pb2
from okra.repository_metrics import (repo_info, iso_date_aggregation,
                                     find_author_count,
                                     find_contributor_count,
                                     find_file_metrics,
                                     hist_start_yearmo)

logger = logging.getLogger(__name__)

def date_toiso(datetime, timespec='minutes'):
    return datetime.isoformat(timespec=timespec)

def msg_iso_date_aggregation(msg, item, status: str, yearmo: str):
    """ Compute IsoDateAggregation message """

    isodt = msg.isodates.add()
    isodt.yearmo = yearmo
    isodt.commit_hash = item.commit_hash

    isoyr, isowk, isody = item.contributed.isocalendar()

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

    qres = repo_info(dal, yearmo)

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

    qres1 = iso_date_aggregation(dal, yearmo)

    if len(qres1) == 0:
        return msg

    first = qres1[0]
    last = qres1[-1]

    msg = msg_iso_date_aggregation(msg, first, status='first', yearmo=yearmo)
    msg = msg_iso_date_aggregation(msg, last, status='last', yearmo=yearmo)

    # Author count

    msg.author_count = find_author_count(dal, yearmo)
    
    # Contributor count

    msg.contrib_count = find_contributor_count(dal, yearmo)

    # File level metrics

    qres4 = find_file_metrics(dal, yearmo)
    msg.file_count = qres4.file_count
    msg.lines_added = qres4.lines_added
    msg.lines_subtracted = qres4.lines_subtracted

    # Truck factor

    member_count, members = get_bus_factor(dal, yearmo)
    msg.truck_factor = member_count

    return msg

def msg_repo_history_metric(dal: DataAccessLayer, repo_id: str, yearmo: str):

    msg = okra_api_pb2.RepositoryHistoryMetric()

    msg.repo_id = repo_id
    msg.current_yearmo = yearmo

    # IsoDataAggregation
        
    qres1 = iso_date_aggregation(dal)

    if len(qres1) == 0:
        return msg

    first = qres1[0]
    last = qres1[-1]

    msg = msg_iso_date_aggregation(msg, first, status='first',
                                   yearmo=first.yearmo)
    msg = msg_iso_date_aggregation(msg, last, status='last',
                                   yearmo=last.yearmo)

    # Find start yearmo

    msg.start_yearmo = first.yearmo

    # Find last commit info

    msg.last_commit_yearmo = last.yearmo
    msg.last_commit_hash = last.commit_hash

    # Total lines added/subtracted

    fimet = find_file_metrics(dal)
    msg.total_lines_added = fimet.lines_added
    msg.total_lines_subtracted = fimet.lines_subtracted

    # Total truck factor

    member_count, members = get_bus_factor(dal)
    msg.total_truck_factor = member_count

    # Total days in project

    time_elapsed = last.contributed - first.contributed
    msg.total_days = time_elapsed.days

    return msg

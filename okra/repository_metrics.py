""" Repository metrics for okra_api.proto """
import logging

from sqlalchemy import func

from okra.models import DataAccessLayer, Meta, Author, Contrib, CommitFile

logger = logging.getLogger(__name__)

def repo_info(dal: DataAccessLayer, yearmo=''):
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.yearmo, Contrib.commit_hash, Contrib.contributed
        ).join(Contrib).filter(Meta.yearmo == yearmo)
        return q.all()

    q = dal.session.query(Contrib.commit_hash, Contrib.contributed).\
        join(Contrib)
    return q.all()

def owner_info(dal: DataAccessLayer):
    q = dal.session.query(Meta.owner_name, Meta.project_name, Meta.commit_hash)
    return q.order_by(Meta.yearmo.desc()).first()

def iso_date_aggregation(dal: DataAccessLayer, yearmo=''):
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.commit_hash, Meta.yearmo, Contrib.contributed
        ).join(Contrib).filter(Meta.yearmo == yearmo)
        return q.all()

    q = dal.session.query(
        Meta.commit_hash, Meta.yearmo, Contrib.contributed
    ).join(Contrib)
    return q.all()

def find_author_count(dal: DataAccessLayer, yearmo=''):
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.commit_hash, Meta.yearmo, Contrib.name, Contrib.email
        ).join(Contrib).filter(Meta.yearmo == yearmo)
        return q.count()

    q = dal.session.query(
        Meta.commit_hash, Contrib.name, Contrib.email
    ).join(Contrib)
    return q.count()

def find_contributor_count(dal: DataAccessLayer, yearmo=''):
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.commit_hash, Meta.yearmo, Contrib.name, Contrib.email
        ).join(Contrib).filter(Meta.yearmo == yearmo)
        return q.count()

    q = dal.session.query(
        Meta.commit_hash, Meta.yearmo, Contrib.name, Contrib.email
    ).join(Contrib)
    return q.count()

def find_file_metrics(dal: DataAccessLayer, yearmo=''):
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.yearmo,
            func.count(CommitFile.modified_file).label('file_count'),
            func.sum(CommitFile.lines_added).label('lines_added'),
            func.sum(CommitFile.lines_subtracted).label('lines_subtracted')
        ).join(CommitFile).filter(Meta.yearmo == yearmo).\
        group_by(Meta.yearmo)
        return q.first()

    q = dal.session.query(
        Meta.project_name,
        Meta.yearmo,
        func.count(CommitFile.modified_file).label('file_count'),
        func.sum(CommitFile.lines_added).label('lines_added'),
        func.sum(CommitFile.lines_subtracted).label('lines_subtracted')
    ).join(CommitFile).group_by(Meta.project_name)
    return q.first()

def hist_start_yearmo(dal: DataAccessLayer):
    """ Start yearmo """
    q = dal.session.query(
        Meta.yearmo, Author.authored
        ).join(Author)
    return q.first()

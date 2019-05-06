""" Turns out that joins are less than ideal in Spark. 

Instead of using a central database, we'll solve the problem in a
distributed way. Each function returns an immutable type. We'll just
use one server with like 32 cores or whatever. Need to throw out the
parquet files and use the SQLite databases.

Reference:
    tbonza/EDS19/project/PredictRepoHealth.ipynb
"""
from collections import defaultdict
from datetime import datetime
import logging
from multiprocessing import Pool
import os
import re

import numpy as np
import pandas as pd

from okra.models import Meta, Author, Contrib, CommitFile, Info
from okra.models import DataAccessLayer


logger = logging.getLogger(__name__)


def run_distributed_pool(n_cores:int, func, work: list):
    """ Run distributed pool across n_cores

    :param n_cores: number of cores in available in server
    :param func: immutable function to execute work
    :param work: input for immutable function
    :return: func output from work
    :rtype: meta
    """
    with Pool(n_cores) as p:
        result = p.map(func, work)
    return result

def create_working_table(dal: DataAccessLayer):
    """ Create a base table to derive all other features and aggregations

    :param dal: okra.models.DataAccessLayer, session must be instantiated
    :return: base table for analysis
    :rtype: pd.DataFrame
    """
    if dal.session is None:
        raise TypeError("Session must be instantiated")

    q = dal.session.query(
        Meta.commit_hash, Meta.owner_name, Meta.project_name,
        CommitFile.file_id, CommitFile.modified_file,
        CommitFile.lines_added, CommitFile.lines_deleted,
        Author.name, Author.email, Author.authored)\
        .join(Author).join(CommitFile)

    items = []
    for item in q.all():
        r = {
            'commit_hash': item.commit_hash,
            'owner_name': item.owner_name,
            'project_name': item.project_name,
            'file_id': item.file_id,
            'modified_file': item.modified_file,
            'lines_added': item.lines_added,
            'lines_deleted': item.lines_deleted,
            'name': item.name,
            'email': item.name,
            'authored': item.authored,
        }
        items.append(r)

    df = pd.DataFrame(items)
    df['ts'] = pd.to_datetime(df.authored)

    return df

def num_authors(df, period: str):
    """ Number of authors in a given time period. 

    :param df: pd.DataFrame, base table
    :param period: str, 'Y', year
    :return: df aggregated by period
    :rtype: pd.DataFrame
    """
    per = df.ts.dt.to_period(period)
    
    cols = ['name','owner_name', 'project_name']
    grp = [per, 'owner_name', 'project_name']
    result = df[cols].groupby(grp).count()
    result.columns = ['num_authors']
    result = result.reset_index()
    return result

def num_mentors(df, period:str, subperiod:str, k:int):
    """ 
    Number of authors in a larger time period who have also
    made commits in k number of smaller time periods. 
    
    For example, number of authors in a year who have also 
    committed changes in each month of that year.

    :param df: pd.DataFrame, base table
    :param period: 'Y', year
    :param subperiod: 'M', month
    :param k: int, authors exist at least k subperiods
    :return: df aggregated by period
    :rtype: pd.DataFrame
    """
    subper = df.ts.dt.to_period(subperiod)
    subcols = ['owner_name', 'project_name',
               'name', 'email']
    subgrp = [subper, 'owner_name', 'project_name', 'name', 'email']
    ok = df[subcols].groupby(subgrp).count()
    ok = ok.reset_index()

    if period == 'Y':

        ok['year'] = ok.ts.apply(lambda x: x.year)
        cols = ['year', 'owner_name', 'project_name', 'name', 'email']
        grp = ['year','owner_name','project_name', 'name']
        ok = ok[cols].groupby(grp).count()

        ok = ok.reset_index()
        ok = ok[['year', 'owner_name', 'project_name', 'email']]
        ok.columns = ['ts', 'owner_name', 'project_name', 'mentor_count']
        result = ok[ok.mentor_count >= k].groupby(['ts', 'owner_name',
                                                   'project_name']).count()
        
        result = result.reset_index()
        return result

    else:
        raise Exception("Period '{}' not found".format(period))

    return df


def num_orgs(df, period):
    """ Number of organizations commiting to a repo in a time period

    Organizations are found by extracting the domain of email 
    addresses used by authors.

    :param df: pd.DataFrame, base table
    :param period: str, 'Y' year time period
    :return: df aggregated by period
    :rtype: pd.DataFrame
    """
    email_suffix = ['com','org','ru','edu','dk','id.au','ac',
                    'de','uk','cz','fr','jp','il','me','net',
                    'eu', 'pw', 'ch','cn','io','nu','it','ai',
                    'fi', 'info', 'sk', 'ie', 'ca', 'at', 'pl',
                    'hu', 'nl', 'works', 'hr', 'se','no', 'blue',
                    '(none)', 'lt', 'cc', 'si', 'la', 'us', 'gr',
                    'De','br', 'ro', 'li', 'gov', 'pt', 'is', 'sg',
                    'vin', 'in', 'be', 'bzh', 'pm', 'xyz', 'fun',
                    'es', 'systems', 'cx', 'tw','cl', 'lv', 'ne',
                    'co', 'st', 'ma', 'ws', 'su', 'ORG', 'tk', 'cu',
                    'COM', 'kr', 'vpc', 'ip', 'danix', 'Com', 're',
                    'EDU']

    pattern = '[A-Za-z\-\._0-9\+]+@(.*)?.({})'.format('|'.join(email_suffix))
    pat = re.compile(pattern)

    df['org_name'] = df.email.apply(lambda x: pat.match(x).group(1)
                                    if pat.match(x) else np.NaN)
    
    per = df.ts.dt.to_period(period)
    cols = ['owner_name', 'project_name', 'org_name']

    result = df[cols].groupby([per, 'owner_name', 'project_name']).count()
    result = result.reset_index()

    return result

def create_features_target(df, k=6):
    """ Create dataset from train/test/val and Y """

    ## Features
    
    X_1 = num_authors(df, 'Y')
    X_2 = num_mentors(df, 'Y', 'M', k)
    X_3 = num_orgs(df, 'Y')

    X_13 = pd.merge(X_1, X_3)
    X_13.ts  = X_13.ts.apply(lambda x: x.year)
    assert X_13.shape[0] == X_1.shape[0]

    cols = ['ts','owner_name', 'project_name', 'mentor_count']
    join_cols = ['ts','owner_name', 'project_name']
    df_features = X_13.merge(X_2[cols], how='left', on=join_cols)

    logger.debug('X_2 head: {}'.format(X_2.head()))
    logger.debug('df_features head: {}'.format(df_features.head()))

    ## Target

    per = df.ts.dt.to_period('Y')
    cols = ['owner_name', 'project_name', 'lines_added', 'lines_deleted']
    grp = [per, 'owner_name', 'project_name']
    df_target = df[cols].groupby(grp).sum()

    df_target['velocity'] = df_target.lines_added - \
        df_target.lines_deleted

    ## Reset indices
    
    df_features = df_features.reset_index()
    df_target = df_target.reset_index()

    ## Recast pandas specific types

    df_target.ts = df_target.ts.apply(lambda x: x.year)

    return df_features, df_target

def write_features_target(dbinfo: tuple, k=6) -> bool:
    """ Write out features and target dataframes to parquet. 
    
    :param dburl: SQLite database url
    :return: write out feature, target dataframes as parquet
    :rtype: bool
    """
    try:
        dburl, repo_name, cache = dbinfo
        
        dal = DataAccessLayer(dburl)
        dal.connect()
        dal.session = dal.Session()

        df = create_working_table(dal)
        df_features, df_target = create_features_target(df, k)
        
        logger.debug("target dtypes: {}".format(df_target.dtypes))
        logger.debug("features dtypes: {}".format(df_features.dtypes))

        logger.debug("target shape: {}".format(df_target.shape))
        logger.debug("features shape: {}".format(df_features.shape))

        feature_path = "{}features_{}.parquet".format(cache, repo_name)
        target_path = "{}target_{}.parquet".format(cache, repo_name)

        df_features.to_parquet(feature_path, 'pyarrow')
        df_target.to_parquet(target_path, 'pyarrow')
        logger.info("Wrote features: {}".format(feature_path))
        logger.info("Wrote target: {}".format(target_path))
        return True

    except Exception as exc:
        logger.exception(exc)
        return False

def getwork_dbinfo(cache: str):
    """ Defines work for immutable function, write_features_target 

    :param cache: str, full path to cache
    :return: dbinfo, (dburl, repo_name, cache)
    :rtype: list of tuples
    """
    work = []
    try:
        dbs = [i for i in os.listdir(cache) if i[-3:] == ".db"]

        for db in dbs:

            dburl = "sqlite:///" + cache + db
            repo_name = db[:-3].replace("__REPODB__", "__LOGDF__")

            dbinfo = (dburl, repo_name, cache)
            work.append(dbinfo)

        return work

    except Exception as exc:
        logger.exception(exc)
        return []

def consolidate_features_target(cache: str, repo_id: str, report=100):
    """ Consolidates distributed computations in cache

    We're going to have n feature tables, n target tables. We
    need to consolidate them into one feature and one target
    table. This is the 'reduce' part of a 'map/reduce' pattern. 
    To avoid confusion with Hadoop, let's call this a 
    'hack/reduce' pattern.
    
    :param cache: str, full path to cache
    :return: X_features, X_target written to disk
    :rtype: None
    """
    date_today = datetime.now().strftime("%Y%m%d")        
    df_names = [i for i in os.listdir(cache) if repo_id in i]

    feature_names = [i for i in df_names if 'features_' in i]
    target_names = [i for i in df_names if 'target_' in i]

    first = True
    fcount = 0
    for feature_name in feature_names:

        fpath = cache + feature_name
        if first:
            featdf = pd.read_parquet(fpath, 'pyarrow')
            first = False

        else:
            fdf = pd.read_parquet(fpath, 'pyarrow')
            featdf = featdf.append(fdf)

        if fcount % report == 0:
            logger.info("Processed {} feature dataframes".format(fcount))
        fcount += 1

    feat_path = '{}df_features_{}.parquet'.format(cache, date_today)
    featdf.to_parquet(feat_path, 'pyarrow')
    logger.info('Wrote df_features, {}, to {}'.\
                format(featdf.shape,feat_path))

    first = True
    tcount = 0
    for target_name in target_names:

        fpath = cache + target_name
        if first:
            targdf = pd.read_parquet(fpath, 'pyarrow')
            first = False

        else:
            tdf = pd.read_parquet(fpath, 'pyarrow')
            targdf = targdf.append(tdf)

        if tcount % report == 0:
            logger.info("Processed {} target dataframes".format(tcount))
        tcount += 1

    targ_path = '{}df_target_{}.parquet'.format(cache, date_today)
    targdf.to_parquet(targ_path, 'pyarrow')
    logger.info('Wrote df_target, {}, to {}'.\
                format(targdf.shape, targ_path))

    
    

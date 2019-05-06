""" Playbooks for running full analyses """
import os
import logging
import shutil
from urllib.parse import urljoin

from okra.assn4 import get_truck_factor_by_project
from okra.error_handling import (MissingEnvironmentVariableError,
                                 NetworkError,
                                 DirectoryNotCreatedError)
from okra.models import DataAccessLayer
from okra.populate_db import populate_db
from okra.repo_mgmt import (create_parent_dir, clone_repo, update_repo,
                            compress_repo, decompress_repo)

logger = logging.getLogger(__name__)


def local_persistance(repo_name: str, parent_dir: str, buffer_size=4096):
    """ Collect relevant data for locally cloned repos. 

    :param repo_name: name of git repository, <linux>
    :param parent_dir: parent directory path, </home/user/code/>
    :param buffer_size: number of records processed before db commit
    :return: populate sqlite database for a repo
    :rtype: None
    """
    logger.info("STARTED -- local persistance")
    repodb = "__REPODB__".join(repo_name.split("/"))
    cache = parent_dir

    dburl = "sqlite:///" + cache + repodb + ".db"
    populate_db(dburl, cache, repo_name, buffer_size)

    logger.info("FINISHED -- local perisistance")

def simple_version_truck_factor(repos: list, dirpath: str, dburl: str, b:int):
    """ Simple version of the truck factor analysis.

    This is a basic version of the truck factor which 
    does not attempt to run the analysis at scale. It's
    just a proof of concept version. Writes out a csv file with
    the truck factor of each repository. You can use this csv file
    to do further analysis in R.

    :param repos: repo queue with value format '<repo owner>/<repo name>'
    :param dirpath: path to working directory to store git repos
    :param dburl: database url (ex. 'sqlite:///:memory')
    :param b: batch size (ex. 1024)
    :return: outputs truck factor analysis as csv file 
    :rtype: None, writes out csv file
    """
    logger.info("STARTED -- simple-version truck factor")

    # Retrieve or update git repos
    
    for repo_name in repos:

        rpath = urljoin(dirpath, repo_name)
        create_parent_dir(repo_name, dirpath)

        if os.path.exists(rpath):
            update_repo(repo_name, dirpath)

        else:
            clone_repo(repo_name, dirpath)

    # Populate database

    populate_db(dburl, dirpath, repos, b)

    # Compute truck factor for each project

    dal = DataAccessLayer(dburl)
    dal.connect()
    dal.session = dal.Session()

    results = []
    for repo_name in repos:

        owner, project = repo_name.split("/")
        truck_factor, _ = get_truck_factor_by_project(owner, project, dal)

        results.append((repo_name, truck_factor))

    dal.session.close()
    logger.info("COMPLETED -- simple-version truck factor")
    return results
    

def retrieve_or_clone(repo_name: str, dirpath: str) -> bool:
    
    # check s3 bucket for repo
    repopath = urljoin(dirpath, repo_name)

    if os.path.exists(repopath): # may already exist
        return True

    return clone_repo(repo_name, dirpath)

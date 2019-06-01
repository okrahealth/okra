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

def retrieve_or_clone(repo_name: str, dirpath: str) -> bool:
    
    # check s3 bucket for repo
    repopath = urljoin(dirpath, repo_name)

    if os.path.exists(repopath): # may already exist
        return True

    return clone_repo(repo_name, dirpath)

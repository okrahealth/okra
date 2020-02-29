""" GitHub Repo Managment

Related to downloading and updating GitHub repos. See
the 'assn1' script in bin/assn1 to handle get and update
features.
"""
import logging
import os
import subprocess
from urllib.parse import urljoin

from okra.error_handling import DirectoryNotCreatedError, NetworkError

logger = logging.getLogger(__name__)

def update_repo(repopath):
    c1 = ["git", "fetch"]
    res = subprocess.run(c1, cwd=repopath, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    if res.returncode == 0:
        return True
    return False

def clone_repo(repo_url, repo_path):
    try:
        res = subprocess.run(["git", "clone", repo_url, repo_path],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and os.path.exists(repo_path):
            return True
        raise NetworkError(
                expression=res.stderr,
                message = "Issue with git clone"
        )
    except Exception as exc:
        raise exc

def clone_or_fetch_repo(repo_path, repo_url):
    if os.path.exists(repo_path):
        return update_repo(repo_path)
    return clone_repo(repo_url, repo_path)

def compress_repo(repo_name: str, cache: str, repo_comp: str) -> bool:
    """ Compress repo for upload.

    :param repo_name: git repo name with owner included; 
                      tensorflow/tensorflow
    :param dirpath: directory path to git repo
    :return: creates a compressed file of github repo
    :rtype: True if git repo successfully compressed
    """
    c1 = ["tar", "-zcf", repo_comp, repo_name]
    res = subprocess.run(c1, cwd=cache, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    if res.returncode == 0:
        return True
    else:
        logger.error(res.stderr)
        return False

def decompress_repo(repo_comp: str, cache) -> bool:
    """ Decompress repo to a directory.

    :param repo_name: git repo name with owner included; 
                      tensorflow/tensorflow
    :param dirpath: directory path to place uncompressed 
                    file with repo owner
    :param filepath: path to file to be decompressed
    :return: Uncompresses file and writes 
             'git_owner_name/git_repo_name' to the 
             specified directory.
    :rtype: boolean
    :raises: :class:`okra.error_handling.DirectoryNotCreatedError`
    """
    c2 = ["tar", "-zxf", repo_comp, "-C", cache]
    res = subprocess.run(c2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if res.returncode == 0:
        return True
    else:
        logger.error(res.stderr)
        return False

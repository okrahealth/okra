""" Place log information into objects 

This is going to generate items for each specified model object
based on git log commands. 
"""
from datetime import datetime
import logging
import os
import re
from urllib.parse import urljoin

from rfc3339 import parse_datetime

from okra.error_handling import DirectoryNotCreatedError
from okra.models import Meta, Author, Contrib, CommitFile, Info, Inventory
from okra.gitlogs import (parse_commits, parse_messages,
                          parse_committed_files)

logger = logging.getLogger(__name__)

def make_digit(numstr, desc):
    try:
        d = int(numstr)
        return d
    
    except ValueError:
        d = 0
        if numstr.strip() != '-':
            logger.error("ValueError for {}: {}".format(desc, numstr))
        return d

def repo_to_objects(repo_name: str, cache: str, last_commit=""):
    """ Retrieve objects from last commit if exists

    This function is a generator so we can specify a buffer size
    when making commits to the database. Otherwise, the I/O would
    slow things way down.

    :param repo_name: git user/git repo name, 'tbonza/EDS19'
    :param dirpath: path to directory storing repo information
    :param last_commit: string of git commit hash last stored in database
    :return: generator of populated model database objects
    :rtype: sqlalchemy database objects
    """
    repopath = urljoin(cache, repo_name)

    if len(last_commit) == 0:
        
        cmts = parse_commits(repopath)
        msgs = parse_messages(repopath)
        fobjs = parse_committed_files(repopath)

    else:
        # retrieve from last commit HEAD
        # need to set 'c1' lists

        cmts = parse_commits(repopath, chash=last_commit)
        msgs = parse_messages(repopath, chash=last_commit)
        fobjs = parse_committed_files(repopath, chash=last_commit)

    # map objects to database objects

    m = re.compile(r"Co-authored-by\:(.*?)<(.*?)>")
    for msg, cmt in zip(msgs, cmts):
        contrib_id = 0

        msg_item = Info(
            commit_hash=msg.hash_val,
            subject=msg.subject,
            message=msg.message_body,
            created=parse_datetime(msg.timestamp)
        )

        o,p = repo_name.split('/')
        meta_item = Meta(
            commit_hash=msg.hash_val,
            owner_name=o,
            project_name=p
        )
        
        author_item = Author(
            commit_hash=cmt.hash_val,
            name=cmt.author,
            email=cmt.author_email,
            authored=parse_datetime(cmt.author_timestamp)
        )

        contrib_item = Contrib(
            contrib_id=contrib_id,
            commit_hash=cmt.hash_val,
            name=cmt.committer,
            email=cmt.committer_email,
            contributed=parse_datetime(cmt.committer_timestamp)
        )        
        yield msg_item
        yield meta_item
        yield author_item
        yield contrib_item

        # some commits will have multiple contributors
        
        if m.match(msg.message_body):

            contrib_id += 1
            for item in m.findall(msg.message_body):

                contrib_item = Contrib(
                    contrib_id=contrib_id,
                    commit_hash=msg.hash_val,
                    name=item[0].strip(),
                    email=item[1].strip(),
                    contributed=parse_datetime(msg.timestamp)
                )
                yield contrib_item
                contrib_id += 1

    file_id = 0
    for fobj in fobjs:

        cf_item = CommitFile(
            file_id=file_id,
            commit_hash=fobj.hash_val,
            modified_file=fobj.file_path,
            lines_added=make_digit(fobj.added, "fobj.added"),
            lines_deleted=make_digit(fobj.deleted, "fobj.deleted")
        )
        yield cf_item

        file_id += 1





    



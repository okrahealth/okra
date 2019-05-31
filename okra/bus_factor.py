""" Compute Truck Factor

The truck factor assignment includes several factors. We're just
going to focus on the actual truck factor computation from a database
in this file.

References:
  Assignment: http://janvitek.org/events/NEU/6050/a4.html
  Paper: http://janvitek.org/events/NEU/6050/Ps/truck.pdf

Modified version of okra/assn4.py for yearmo 
"""
from collections import defaultdict

from sqlalchemy import func
from okra.assn4 import author_number_of_files_owned, smallest_owner_set
from okra.models import (Meta, Author, Contrib, CommitFile, Info)

def number_of_files(dal, yearmo=''):
    """ Compute the number of files by project

    If yearmo, computation only applies to the last
    yearmo.

    :param dal: okra.models.DataAccessLayer
    :param yearmo: str, year month
    :return: the number of files in a project
    :rtype: int
    """
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.yearmo, CommitFile.modified_file
        ).join(CommitFile).filter(Meta.yearmo == yearmo).\
        group_by(CommitFile.modified_file)
        return q.count()

    q = dal.session.query(CommitFile.modified_file).\
        group_by(CommitFile.modified_file)
    return q.count()

def number_of_contributors(dal, yearmo=''):
    """
    :param dal: okra.models.DataAccessLayer
    :param yearmo: str, year month
    :return: the number of contributors in a project
    :rtype: int
    """
    if len(yearmo) > 0:
        q = dal.session.query(
            Meta.yearmo, Contrib.name, Contrib.email
        ).filter(Meta.yearmo == yearmo).join(Contrib).\
        group_by(Contrib.name, Contrib.email)
        return q.count()

    q = dal.session.query(Contrib.name, Contrib.email)
    return q.count()

def max_lines_perfile(res):
    """ Author with max number of lines added per file (owner) """
    
    owner = {}
    for item in res:

        fname = item.modified_file
        if fname in owner:

            if owner[fname].total_lines_added > item.total_lines_added:
                owner[fname] = item

        else:
            owner[fname] = item

    results = list(owner.values())
    return results

def file_author_owner(dal, yearmo=''):
    """ Compute file ownership by each author. 

    :param dal: okra.models.DataAccessLayer
    :param yearmo: str, year month
    :return: list of file owners based on max number of lines written
    :rtype: list of sqlalchemy objects
    """
    if len(yearmo) > 0:
        
        # Number of lines added by each author per file, yearmo filter

        q = dal.session.query(
            Meta.commit_hash, Meta.yearmo, Author.name, Author.email,
            CommitFile.modified_file,
            func.sum(CommitFile.lines_added).label("total_lines_added")
        ).filter(Meta.yearmo == yearmo).\
        join(Author).join(CommitFile).\
        group_by(Author.name, Author.email, CommitFile.modified_file)

        res = q.all()
        return max_lines_perfile(res)

    # Number of lines added by each author per file

    q = dal.session.query(
        Meta.commit_hash, Meta.yearmo, Author.name, Author.email,
        CommitFile.modified_file,
        func.sum(CommitFile.lines_added).label("total_lines_added")
    ).join(Author).join(CommitFile).\
    group_by(Author.name, Author.email, CommitFile.modified_file)
    
    res = q.all()
    return max_lines_perfile(res)

def get_bus_factor(dal, yearmo=''):
    """ Get the 'bus factor'. 

    1. For each project, and each file, compute how many lines were 
       added by each unique user.
    2. For each project, and each file, find which user created the file.
    3. Given the above two results compute the ownership of each file.
    4. For each project, and each file pick an owner.
    5. For each project, rank the users by the number of files they own.
    6. Given all of the above compute the Truck Factor as the smallest set 
       of users such that they own more than half of the files in the project

    :param dal: okra.models.DataAccessLayer
    :param yearmo: str, year month
    :return: Truck factor score for a GitHub project, Truck set members
    :rtype: tuple (int, list)
    """
    total_files = number_of_files(dal, yearmo)
    owners = file_author_owner(dal, yearmo)
    authors = author_number_of_files_owned(owners)
    member_count, members = smallest_owner_set(authors, total_files)

    return (member_count, members)

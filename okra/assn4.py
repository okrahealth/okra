""" Compute Truck Factor

The truck factor assignment includes several factors. We're just
going to focus on the actual truck factor computation from a database
in this file.

References:
  Assignment: http://janvitek.org/events/NEU/6050/a4.html
  Paper: http://janvitek.org/events/NEU/6050/Ps/truck.pdf
"""
from collections import defaultdict

from sqlalchemy import func
from okra.models import (Meta, Author, Contrib, CommitFile, Info)

def total_number_of_files_by_project(owner, project, dal):
    """ Compute the total number of files by project. 
    
    :param owner: name of owner
    :param project: name of project
    :param dal: okra.models.DataAccessLayer
    :return: the number of files in a project
    :rtype: int
    """
    q = dal.session.query(
        Meta.owner_name, Meta.project_name, CommitFile.modified_file
    ).\
    join(CommitFile).\
    filter(
        Meta.owner_name == owner, Meta.project_name == project
    ).\
    group_by(CommitFile.modified_file).all()
    return len(q)

def author_file_owned(owner, project, dal):
    """ Compute file ownership by each author. 

    :param owner: name of owner
    :param project: name of project    
    :param dal: okra.models.DataAccessLayer
    :return: list of file owners based on max number of lines written
    :rtype: list of sqlalchemy objects
    """

    # Number of lines added by each author per file
    
    q = dal.session.\
        query(
            Meta.owner_name, Meta.project_name, Meta.commit_hash,
            Author.name, Author.email, CommitFile.modified_file,
            func.sum(CommitFile.lines_added).label("total_lines_added")
        ).\
        filter(Meta.owner_name == owner, Meta.project_name == project).\
        join(Author).join(CommitFile).\
        group_by(Author.name, CommitFile.modified_file)

    # Author with max number of lines added per file (owner)

    res = q.all()

    owner = {}
    for item in res:

        fname = item.modified_file
        if fname in owner:

            if owner[fname].total_lines_added > item.total_lines_added:
                owner[fname] = item

        else:
            owner[fname] =  item

    results = [i for i in owner.values()]
    return results

def author_number_of_files_owned(results):
    """ Number of files owned by author. 

    :param results: results from author_file_owned() 
    :return: {author:  number of files owned}
    :rtype: dict
    """
    authors = defaultdict(int)
    for item in results:

        authors[item.name] += 1

    return authors

def smallest_owner_set(authors, total, size=0.5):
    """ Smallest set of authors owning more than half of project files. 

    :param authors: author_number_of_files_owned() output
    :param total: total_number_of_files_by_project() output
    :return: (number of members in smallest set, smallest set)
    :rtype: tuple
    """
    items = sorted(authors.items(), key=lambda k_v: k_v[1], reverse=True)
    threshold = round(total * size)
    agg = 0
    members = []
    member_count = 0
    for k,v in items:

        if agg <= threshold:

            members.append((k,v))
            member_count += 1
            agg += v

        else:
            break

    return (member_count, members)

def get_truck_factor_by_project(owner, project, dal):
    """ Get the 'truck factor' by project.

    1. For each project, and each file, compute how many lines were 
       added by each unique user.
    2. For each project, and each file, find which user created the file.
    3. Given the above two results compute the ownership of each file.
    4. For each project, and each file pick an owner.
    5. For each project, rank the users by the number of files they own.
    6. Given all of the above compute the Truck Factor as the smallest set 
       of users such that they own more than half of the files in the project

    :param owner: name of owner
    :param project: name of project
    :param dal: okra.models.DataAccessLayer
    :return: Truck factor score for a GitHub project, Truck set members
    :rtype: tuple (int, list)
    """
    total_files = total_number_of_files_by_project(owner, project, dal)
    owners = author_file_owned(owner, project, dal)
    authors = author_number_of_files_owned(owners)
    member_count, members = smallest_owner_set(authors, total_files)

    return (member_count, members)

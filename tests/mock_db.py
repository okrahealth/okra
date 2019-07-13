""" Mock database for testing """

from datetime import datetime

from okra.models import Meta, Author, Contrib, CommitFile, Info

def mock_meta(session):
    meta_commits = [
        Meta(commit_hash="1", owner_name="Tyler", project_name="okra",
             yearmo='2015-01'),
        Meta(commit_hash="2", owner_name="Tyler", project_name="okra",
             yearmo='2015-06'),
        Meta(commit_hash="3", owner_name="Tyler", project_name="okra",
             yearmo='2015-06'),
        Meta(commit_hash="4", owner_name="Tyler", project_name="okra",
             yearmo='2017-01'),
        Meta(commit_hash="5", owner_name="Tyler", project_name="okra",
             yearmo='2017-06'),
    ]

    session.bulk_save_objects(meta_commits)
    session.commit()
    return session

def mock_author(session):
    author_commits = [
        Author(commit_hash="1", name="Tyler",
               authored=datetime(2015, 1, 1, 12, 30, 59, 0)),
        Author(commit_hash="2", name="Tyler",
               authored=datetime(2015, 6, 1, 12, 30, 59, 0)),
        Author(commit_hash="3", name="Chaitya",
               authored=datetime(2015, 6, 3, 12, 30, 59, 0)),
        Author(commit_hash="4", name="Angela",
               authored=datetime(2017, 1, 1, 12, 30, 59, 0)),
        Author(commit_hash="5", name="Chris",
               authored=datetime(2017, 6, 1, 12, 30, 59, 0)),
    ]

    session.bulk_save_objects(author_commits)
    session.commit()
    return session

def mock_contrib(session):
    contrib_commits = [
        Contrib(contrib_id=1, commit_hash="1",
                name="Tyler",
                contributed=datetime(2015, 1, 1, 12, 30, 59, 0)),
        Contrib(contrib_id=2, commit_hash="1",
                name="Diego",
                contributed=datetime(2015, 1, 1, 12, 30, 59, 0)),
        Contrib(contrib_id=3, commit_hash="2",
                name="Tyler",
                contributed=datetime(2015, 6, 1, 12, 30, 59, 0)),
        Contrib(contrib_id=4, commit_hash="3",
                name="Chaitya",
                contributed=datetime(2015, 6, 3, 12, 30, 59, 0)),
        Contrib(contrib_id=5, commit_hash="4",
                name="Angela",
                contributed=datetime(2017, 1, 1, 12, 30, 59, 0)),
        Contrib(contrib_id=6, commit_hash="5",
                name="Chris",
                contributed=datetime(2017, 6, 1, 12, 30, 59, 0)),
    ] # note that truck factor will exclude multiple contributors

    session.bulk_save_objects(contrib_commits)
    session.commit()
    return session

def mock_commit_file(session):

    commit_files = [
        # commit hash '1'

        CommitFile(file_id=1, commit_hash="1", modified_file="a1.R",
                   lines_added=20, lines_subtracted=0),
        CommitFile(file_id=2, commit_hash="1", modified_file="b1.R",
                   lines_added=20, lines_subtracted=0),
        CommitFile(file_id=3, commit_hash="1", modified_file="c1.R",
                   lines_added=20, lines_subtracted=0),

        # commit hash '2'

        CommitFile(file_id=4, commit_hash="2", modified_file="a1.R",
                   lines_added=20, lines_subtracted=0),
        CommitFile(file_id=5, commit_hash="2", modified_file="b1.R",
                   lines_added=20, lines_subtracted=0),

        # commit hash '3'

        CommitFile(file_id=6, commit_hash="3", modified_file="d1.R",
                   lines_added=20, lines_subtracted=0),
        CommitFile(file_id=7, commit_hash="3", modified_file="e1.R",
                   lines_added=20, lines_subtracted=0),

        # commit hash '4'

        CommitFile(file_id=8, commit_hash="4", modified_file="f1.R",
                   lines_added=20, lines_subtracted=0),
        CommitFile(file_id=9, commit_hash="4", modified_file="g1.R",
                   lines_added=20, lines_subtracted=0),

        # commit hash '5'

        CommitFile(file_id=10, commit_hash="5", modified_file="h1.R",
                   lines_added=20, lines_subtracted=0),
        CommitFile(file_id=11, commit_hash="5", modified_file="i1.R",
                   lines_added=20, lines_subtracted=0),

    ]

    session.bulk_save_objects(commit_files)
    session.commit()

    return session

def mock_commit_info(session):

    commit_info = [
        Info(commit_hash="1", created=datetime(2015, 1, 1, 12, 30, 59, 0)),
        Info(commit_hash="2", created=datetime(2015, 6, 1, 12, 30, 59, 0)),
        Info(commit_hash="3", created=datetime(2015, 6, 3, 12, 30, 59, 0)),
        Info(commit_hash="4", created=datetime(2017, 1, 1, 12, 30, 59, 0)),
        Info(commit_hash="5", created=datetime(2017, 6, 1, 12, 30, 59, 0)),
    ]

    session.bulk_save_objects(commit_info)
    session.commit()

    return session

def mock_github_project_db(session):
    session = mock_meta(session)
    session = mock_author(session)
    session = mock_contrib(session)
    session = mock_commit_file(session)
    session = mock_commit_info(session)
    return session

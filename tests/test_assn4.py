""" Validating data models using in Assignment 4

Mocking up a GitHub project then testing that the computation
works. 
"""
from datetime import datetime
import unittest

from okra.models import (DataAccessLayer, Meta, Author, Contrib,
                         CommitFile, Info)
from okra.assn4 import (total_number_of_files_by_project,
                        author_file_owned, author_number_of_files_owned,
                        smallest_owner_set,
                        get_truck_factor_by_project)

def mock_github_project_db(session):
    """ 
    Mock up a database that can be used to compute the truck factor
    of a project.
    """

    meta_commits = [
        Meta(commit_hash="1", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="2", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="3", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="4", owner_name="Tyler", project_name="okra"),
        Meta(commit_hash="5", owner_name="Tyler", project_name="okra"),
    ]
    
    session.bulk_save_objects(meta_commits)
    session.commit()

    author_commits = [
        Author(commit_hash="1", name="Tyler", authored=datetime.now()),
        Author(commit_hash="2", name="Tyler", authored=datetime.now()),
        Author(commit_hash="3", name="Chaitya", authored=datetime.now()),
        Author(commit_hash="4", name="Angela", authored=datetime.now()),
        Author(commit_hash="5", name="Chris", authored=datetime.now()),
    ]

    session.bulk_save_objects(author_commits)
    session.commit()

    contrib_commits = [
        Contrib(contrib_id=1, commit_hash="1",
                name="Tyler", contributed=datetime.now()),
        Contrib(contrib_id=2, commit_hash="1",
                name="Diego", contributed=datetime.now()),
        Contrib(contrib_id=3, commit_hash="2",
                name="Tyler", contributed=datetime.now()),
        Contrib(contrib_id=4, commit_hash="3",
                name="Chaitya", contributed=datetime.now()),
        Contrib(contrib_id=5, commit_hash="4",
                name="Angela", contributed=datetime.now()),
        Contrib(contrib_id=6, commit_hash="5",
                name="Chris", contributed=datetime.now()),
    ] # note that truck factor will exclude multiple contributors

    session.bulk_save_objects(contrib_commits)
    session.commit()

    commit_files = [
        
        # commit hash '1'
        
        CommitFile(file_id=1, commit_hash="1", modified_file="a1.R",
                   lines_added=20, lines_deleted=0),
        CommitFile(file_id=2, commit_hash="1", modified_file="b1.R",
                   lines_added=20, lines_deleted=0),
        CommitFile(file_id=3, commit_hash="1", modified_file="c1.R",
                   lines_added=20, lines_deleted=0),

        # commit hash '2'

        CommitFile(file_id=4, commit_hash="2", modified_file="a1.R",
                   lines_added=20, lines_deleted=0),
        CommitFile(file_id=5, commit_hash="2", modified_file="b1.R",
                   lines_added=20, lines_deleted=0),

        # commit hash '3'

        CommitFile(file_id=6, commit_hash="3", modified_file="d1.R",
                   lines_added=20, lines_deleted=0),
        CommitFile(file_id=7, commit_hash="3", modified_file="e1.R",
                   lines_added=20, lines_deleted=0),

        # commit hash '4'

        CommitFile(file_id=8, commit_hash="4", modified_file="f1.R",
                   lines_added=20, lines_deleted=0),
        CommitFile(file_id=9, commit_hash="4", modified_file="g1.R",
                   lines_added=20, lines_deleted=0),

        # commit hash '5'
        
        CommitFile(file_id=10, commit_hash="5", modified_file="h1.R",
                   lines_added=20, lines_deleted=0),
        CommitFile(file_id=11, commit_hash="5", modified_file="i1.R",
                   lines_added=20, lines_deleted=0),
    ]

    session.bulk_save_objects(commit_files)
    session.commit()

    commit_info = [
        Info(commit_hash="1", created=datetime.now()),
        Info(commit_hash="2", created=datetime.now()),
        Info(commit_hash="3", created=datetime.now()),
        Info(commit_hash="4", created=datetime.now()),
        Info(commit_hash="5", created=datetime.now()),
    ]

    session.bulk_save_objects(commit_info)
    session.commit()


class TestAssn4(unittest.TestCase):
    """ Verifying model behavior. """

    @classmethod
    def setUpClass(cls):
        cls.dal = DataAccessLayer('sqlite:///:memory:')
        cls.dal.connect()
        cls.dal.session = cls.dal.Session()
        mock_github_project_db(cls.dal.session)
        cls.dal.session.close()

    def setUp(self):
        self.dal.session = self.dal.Session()
        
    def tearDown(self):
        self.dal.session.rollback()
        self.dal.session.close()

    def test_total_number_of_files_by_project(self):
        result = total_number_of_files_by_project("Tyler", "okra", self.dal)

        assert result == 9

    def test_author_file_owned(self):
        result = author_file_owned("Tyler", "okra", self.dal)

        assert result[-2].modified_file == "b1.R"
        assert result[-2].total_lines_added == 40
        assert len(result) == 9

    def test_author_number_of_files_owned(self):
        afo = author_file_owned("Tyler", "okra", self.dal)
        result = author_number_of_files_owned(afo)

        assert len(result) == 4
        assert result["Tyler"] == 3
        assert result["Angela"] == 2

    def test_smallest_owner_set(self):
        afo = author_file_owned("Tyler", "okra", self.dal)
        authors = author_number_of_files_owned(afo)
        total = total_number_of_files_by_project("Tyler", "okra", self.dal)

        result = smallest_owner_set(authors, total)

        res_count, res_members = result

        assert res_count == 2
        assert res_members[0] == ("Tyler", 3)
        assert res_members[1] == ("Angela", 2)

    def test_get_truck_factor_by_project(self):

        result = get_truck_factor_by_project("Tyler", "okra", self.dal)

        res_count, res_members = result

        assert res_count == 2
        assert res_members[0] == ("Tyler", 3)
        assert res_members[1] == ("Angela", 2)

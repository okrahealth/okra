""" Validating data models using in Assignment 4

Mocking up a GitHub project then testing that the computation
works. 
"""
from datetime import datetime
import unittest

from okra.models import (DataAccessLayer)
from okra.assn4 import (total_number_of_files_by_project,
                        total_number_of_contributors_by_project,
                        author_file_owned, author_number_of_files_owned,
                        smallest_owner_set,
                        get_truck_factor_by_project)
from .mock_db import mock_github_project_db


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

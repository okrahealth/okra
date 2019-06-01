""" Validate bus factor with and without yearmo """
from datetime import datetime
import unittest

from okra.models import DataAccessLayer
from okra.bus_factor import (number_of_files, number_of_contributors,
                             file_author_owner, get_bus_factor)
from .mock_db import mock_github_project_db


class TestBusFactor(unittest.TestCase):

    yearmo = '2015-01'

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

    def test_number_of_files(self):
        result = number_of_files(self.dal)
        assert result == 9

    def test_number_of_files_yearmo(self):
        result = number_of_files(self.dal, self.yearmo)
        assert result == 3

    def test_number_of_contributors(self):
        result = number_of_contributors(self.dal)
        assert result == 6

    def test_number_of_contributors_yearmo(self):
        result = number_of_contributors(self.dal, self.yearmo)
        assert result == 2

    def test_file_author_owner(self):
        result = file_author_owner(self.dal)

        assert result[-2].modified_file == "b1.R"
        assert result[-2].total_lines_added == 40
        assert len(result) == 9

    def test_file_author_owner_yearmo(self):
        result = file_author_owner(self.dal, self.yearmo)

        assert result[-2].modified_file == "b1.R"
        assert result[-2].total_lines_added == 20
        assert len(result) == 3

    def test_get_bus_factor(self):
        result = get_bus_factor(self.dal)

        res_count, res_members = result

        assert res_count == 2
        assert res_members[0] == ("Tyler", 3)
        assert res_members[1] == ("Angela", 2)

    def test_get_bus_factor_yearmo(self):
        result = get_bus_factor(self.dal, self.yearmo)

        res_count, res_members = result

        assert res_count == 1
        assert res_members[0] == ("Tyler", 3)
        



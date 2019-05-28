""" Validate interface for batch updates to Okra API """
import unittest

from okra.models import DataAccessLayer
from okra.assn4 import total_number_of_contributors_by_project
from okra.mgmt_api import msg_repository_info

from .mock_db import mock_github_project_db


class TestMgmtApi(unittest.TestCase):

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

    def test_msg_repository_info(self):
        out = msg_repository_info(self.dal, 'Tyler/okra', '2017-06')

        assert out.repo_id == 'Tyler/okra'
        assert out.yearmo == '2017-06'

        assert len(out.isodates) == 1
        assert out.isodates[0].yearmo == '2017-06'
        assert out.isodates[0].commit_hash == '5'
        assert out.isodates[0].iso_week == 22
        assert out.isodates[0].iso_year == 2017
        assert out.isodates[0].status == ''

    def test_msg_repository_metric(self):
        pass

    def test_msg_iso_date_aggregation(self):
        pass

    def test_total_number_of_contributors_by_project(self):
        result = total_number_of_contributors_by_project("Tyler",
                                                         "okra", self.dal)
        assert result == 4


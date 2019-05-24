""" Validate interface for batch updates to Okra API """
import unittest

from okra.models import DataAccessLayer
from okra.assn4 import total_number_of_contributors_by_project
from okra.mgmt_api import msg_repository_info



from tests.test_assn4 import mock_github_project_db


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
        out = msg_repository_info(self.dal)

        assert out.owner_name == "Tyler"
        assert out.repo_name == "okra"
        assert out.first_commit_hash == '1'
        assert out.first_commit_date == '2015-01-01T12:30'
        assert out.last_commit_hash == '5'
        assert out.last_commit_date == '2017-06-01T12:30'

    def test_total_number_of_contributors_by_project(self):
        result = total_number_of_contributors_by_project("Tyler",
                                                         "okra", self.dal)
        assert result == 4


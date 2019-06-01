""" Validate interface for batch updates to Okra API """
import unittest

from okra.models import DataAccessLayer
from okra.assn4 import total_number_of_contributors_by_project
from okra.mgmt_api import (msg_repository_info, msg_repository_metric,
                           msg_repo_history_metric)

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
        self.repo_id = 'Tyler/okra'
        self.yearmo = '2017-06'
        
    def tearDown(self):
        self.dal.session.rollback()
        self.dal.session.close()

    def test_msg_repository_info(self):
        out = msg_repository_info(self.dal, self.repo_id, self.yearmo)

        assert out.repo_id == self.repo_id
        assert out.yearmo == self.yearmo

        assert len(out.isodates) == 2
        assert out.isodates[0].yearmo == self.yearmo
        assert out.isodates[0].commit_hash == '5'
        assert out.isodates[0].iso_week == 22
        assert out.isodates[0].iso_year == 2017
        assert out.isodates[0].status == 'first'

        assert out.isodates[1].commit_hash == '5'
        assert out.isodates[1].status == 'last'

    def test_msg_repository_metric(self):
        out = msg_repository_metric(self.dal, self.repo_id, self.yearmo)

        # Meta info
        
        assert out.repo_id == self.repo_id
        assert out.yearmo == self.yearmo

        # IsoDateAggregation
        
        assert len(out.isodates) == 2
        assert out.isodates[0].yearmo == self.yearmo
        assert out.isodates[0].commit_hash == '5'
        assert out.isodates[0].iso_week == 22

        # Author

        assert out.author_count == 1

        # Contrib

        assert out.contrib_count == 1

        # File metrics

        assert out.file_count == 2
        assert out.lines_added == 40
        assert out.lines_subtracted == 0

        # Truck factor

        assert out.truck_factor == 1

    def test_repository_history_metric(self):
        out = msg_repo_history_metric(self.dal, self.repo_id, self.yearmo)

        assert out.repo_id == self.repo_id
        assert out.current_yearmo == self.yearmo

""" Validate repository metrics,

Several of these tests are being handled in okra/tests/mgmt_api.py
"""
import unittest

from okra.models import DataAccessLayer
from okra.repository_metrics import (hist_start_yearmo)

from .mock_db import mock_github_project_db



class TestRepositoryMetrics(unittest.TestCase):

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

    def test_hist_start_yearmo(self):
        out = hist_start_yearmo(self.dal)
        assert out.yearmo == '2015-01'


    

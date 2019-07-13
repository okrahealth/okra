""" Validating associated jupyter helper functions

Mocking up a GitHub project then testing that the computation
works.
"""

import unittest
from okra.models import (DataAccessLayer)
from okra.repository_metrics import owner_info
from okra.jupyter import create_playbook
from .mock_db import mock_github_project_db

class TestJupyter(unittest.TestCase):
    """ Verifying jupyter notebook methods. """

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

    def test_create_playbook(self):
        owner = owner_info(self.dal)
        result = create_playbook(owner, ".")
        assert result == "./Tyler_okra_5.ipynb"


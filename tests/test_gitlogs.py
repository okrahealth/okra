""" Validate assignment 1 data processing. """
import os
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from okra.gitlogs import (parse_committed_files, parse_commits,
                          parse_messages, parse_inventory)
from okra.playbooks import retrieve_or_clone

class TestAssn1Data(unittest.TestCase):

    repo_name = "tbonza/tiny_dancer"
    total_commits = 4

    @classmethod
    def setUpClass(cls):
        cls.tmpdir = tempfile.TemporaryDirectory()
        cls.repo_path = urljoin(cls.tmpdir.name, cls.repo_name)

    @classmethod
    def tearDownClass(cls):

        cls.tmpdir.cleanup()
        if os.path.exists(cls.tmpdir.name):
            shutil.rmtree(cls.tmpdir.name)

        #if os.path.exists(cls.repo_path):
        #    shutil.rmtree(cls.repo_path)
        # caching repo path for time being, faster tests, less network

    def setUp(self):
        retrieve_or_clone(self.repo_name, self.tmpdir.name)

    def test_parse_commits(self):
        
        results = [i for i in parse_commits(self.repo_path)]
        
        assert len(results) == self.total_commits

        r = results[1]

        assert r.hash_val == 'ed4dd8e797db7d6c1ce23980c24d94228d66b1d6'
        assert r.author == 'tbonza'
        assert r.author_email == 'tylers.pile@gmail.com'
        assert r.author_timestamp == '2019-02-26T09:55:26-05:00'
        assert r.committer == 'tbonza'
        assert r.committer_email == 'tylers.pile@gmail.com'
        assert r.committer_timestamp == '2019-02-26T09:55:26-05:00'

    def test_new_parse_commits(self):
        """ Parse from last commit """
        chash = '35d8e493ef66bd8c01c15a519c15d9a6d31cb2f4'
        results = [i for i in parse_commits(self.repo_path, chash)]

        assert len(results) == self.total_commits - 1

        r = results[1]

        assert r.hash_val == 'ed4dd8e797db7d6c1ce23980c24d94228d66b1d6'
        assert r.author == 'tbonza'
        assert r.author_email == 'tylers.pile@gmail.com'
        assert r.author_timestamp == '2019-02-26T09:55:26-05:00'
        assert r.committer == 'tbonza'
        assert r.committer_email == 'tylers.pile@gmail.com'
        assert r.committer_timestamp == '2019-02-26T09:55:26-05:00'

    def test_parse_messages(self):

        results = [i for i in parse_messages(self.repo_path)]

        assert len(results) == self.total_commits

        r = results[0]

        assert r.hash_val == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r.subject == 'added a function with friends.'
        assert r.message_body == 'Co-authored-by: johnbaldwin <john@appsembler.com>\nCo-authored-by: awong <angela@angela.com\n'
        assert r.timestamp == '2019-02-26T18:22:54-05:00'

    def test_new_parse_messages(self):
        chash = '35d8e493ef66bd8c01c15a519c15d9a6d31cb2f4'
        results = [i for i in parse_messages(self.repo_path, chash)]

        assert len(results) == self.total_commits - 1
        
        r = results[0]

        assert r.hash_val == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r.subject == 'added a function with friends.'
        assert r.message_body == 'Co-authored-by: johnbaldwin <john@appsembler.com>\nCo-authored-by: awong <angela@angela.com\n'
        assert r.timestamp == '2019-02-26T18:22:54-05:00'

    def test_basic_parse_commited_files(self):

        results = [i for i in parse_committed_files(self.repo_path)]

        assert len(results) == 8
        r = results[1]

        assert r.hash_val == 'ed4dd8e797db7d6c1ce23980c24d94228d66b1d6'
        assert r.added == '2'
        assert r.deleted == '1'
        assert r.file_path == 'hello.py'

        r2 = results[2]

        assert r2.hash_val == 'ed4dd8e797db7d6c1ce23980c24d94228d66b1d6'
        assert r2.file_path == 'hello1.py'
        assert r2.added == '1'
        assert r2.deleted == '2'

    def test_parse_inventory(self):

        r = parse_inventory(self.repo_path, self.repo_name)

        assert r.owner == 'tbonza'
        assert r.project == 'tiny_dancer'
        assert r.last_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'

        

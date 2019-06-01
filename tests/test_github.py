""" Validate log parsing to database model objects conversion. 

We're going to mock a git clone by copying a repo from the tests/data
folder.
"""
from datetime import datetime
import os
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from rfc3339 import parse_datetime

from okra.github import repo_to_objects
from okra.playbooks import retrieve_or_clone

class TestGithub(unittest.TestCase):

    repo_name = "tbonza/tiny_dancer"
    data_loc = 'tests/data/'
    total_commits = 4

    def test_repo_to_objects_last_commit(self):
        last_commit = "ed4dd8e797db7d6c1ce23980c24d94228d66b1d6"

        results = [i for i in repo_to_objects(self.repo_name,
                                              self.data_loc,
                                              last_commit=last_commit)]

        assert len(results) == 6

        # Info
        
        r0 = results[0]
        assert r0.__tablename__ == 'info'
        assert r0.commit_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r0.subject == "added a function with friends."
        assert r0.message == 'Co-authored-by: johnbaldwin <john@appsembler.com>\nCo-authored-by: awong <angela@angela.com\n'
        assert r0.created == parse_datetime('2019-02-26T18:22:54-05:00')

        # Meta

        r1 = results[1]
        assert r1.__tablename__ == 'meta'
        assert r1.commit_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r1.owner_name == 'tbonza'
        assert r1.project_name == 'tiny_dancer'

        # Author

        r2 = results[2]
        assert r2.__tablename__ == 'author'
        assert r2.commit_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r2.name == 'tbonza'
        assert r2.email == 'tylers.pile@gmail.com'
        assert r2.authored == parse_datetime('2019-02-26T18:22:54-05:00')

        # Contributor0

        r3 = results[3]
        assert r3.__tablename__ == 'contrib'
        assert r3.contrib_id == 0
        assert r3.commit_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r3.name == 'tbonza'
        assert r3.email == 'tylers.pile@gmail.com'
        assert r3.contributed ==  parse_datetime('2019-02-26T18:22:54-05:00')

        # Contributor1

        r4 = results[4]
        assert r4.__tablename__ == 'contrib'
        assert r4.contrib_id == 1
        assert r4.commit_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r4.name == 'johnbaldwin'
        assert r4.email == 'john@appsembler.com'
        assert r4.contributed == parse_datetime('2019-02-26T18:22:54-05:00')

        # CommitFile

        r5 = results[5]
        assert r5.__tablename__ == 'commit_file'
        assert r5.file_id == 0
        assert r5.commit_hash == 'b6ca6229284e18b0ce8defeb4b240aa2f26223b4'
        assert r5.modified_file == 'friends.py'
        assert r5.lines_added == 2
        assert r5.lines_subtracted == 0


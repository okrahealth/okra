""" Validate behaviors from playbooks. 

The playbooks are the last level of abstraction before an application
is run as a pipeline. Each play in the playbook is meant to be chained
together so we can complete a task.
"""
import os
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from okra.playbooks import (retrieve_or_clone)

class TestPlaybooks(unittest.TestCase):

    repo_name = "tbonza/tiny_dancer"

    @classmethod
    def setUpClass(cls):

        cls.tmpdir = tempfile.TemporaryDirectory()

    @classmethod
    def tearDownClass(cls):

        cls.tmpdir.cleanup()
        if os.path.exists(cls.tmpdir.name):
            shutil.rmtree(cls.tmpdir.name)


    def test_temp_directory_roundtrip(self):
        dirname = self.tmpdir.name
        fpath = urljoin(dirname, "hello.txt")

        with open(fpath, "w") as outfile:
            outfile.write("hello world\n")

        assert os.path.exists(fpath)

        with open(fpath, "r") as infile:
            data = infile.read().strip()

        assert data == "hello world"

    def test_retrieve_or_clone(self):

        result = retrieve_or_clone(self.repo_name, self.tmpdir.name)
        assert result


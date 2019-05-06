""" Validate some functions associated with git repo management. """
import os
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from okra.playbooks import retrieve_or_clone
from okra.repo_mgmt import (compress_repo, decompress_repo)

class TestRepoMgmt(unittest.TestCase):

    repo_name = "tbonza/tiny_dancer"

    @classmethod
    def setUpClass(cls):

        cls.tmpdir = tempfile.TemporaryDirectory()
        cls.tmpdirname = cls.tmpdir.name + "/"
        
        cls.repo_path = urljoin(cls.tmpdirname, cls.repo_name)
        cls.repodb = "__REPODB__".join(cls.repo_name.split("/"))
        cls.repodb_path = urljoin(cls.tmpdirname, cls.repodb)
        
        shutil.copy(urljoin("tests/data/", cls.repodb) + ".db",
                    urljoin(cls.tmpdirname, cls.repodb) + ".db")
        shutil.copytree(urljoin("tests/data/", cls.repo_name),
                        urljoin(cls.tmpdirname, cls.repo_name))

        
    @classmethod
    def tearDownClass(cls):

        cls.tmpdir.cleanup()
        if os.path.exists(cls.tmpdir.name):
            shutil.rmtree(cls.tmpdir.name)

        #if os.path.exists(cls.repo_path):
        #    shutil.rmtree(cls.repo_path)
        # caching repo path for time being, faster tests, less network

    def setUp(self):
        self.repo = "__REPO__".join(self.repo_name.split("/"))

    def test_compress_repo(self):

        repo_comp = self.repo + ".tar.gz"
        rpath = urljoin(self.tmpdirname, repo_comp)
        
        res = compress_repo(
            repo_name=self.repo_name,
            cache=self.tmpdirname,
            repo_comp=repo_comp
        )

        assert res
        assert os.path.exists(rpath)

    def test_db_compress_repo(self):

        repo_comp = self.repodb + ".tar.gz"
        repo_db_name = self.repodb + ".db"
        rpath = urljoin(self.tmpdirname, repo_comp)

        res = compress_repo(
            repo_name=repo_db_name,
            cache=self.tmpdirname,
            repo_comp=repo_comp
        )

        assert res
        assert os.path.exists(rpath)

    def test_decompress_repo(self):

        repo_comp = self.repo + ".tar.gz"
        rpath = urljoin(self.tmpdirname, repo_comp)
        assert os.path.exists(rpath)

        decompress_repo(rpath, self.tmpdirname)

        assert os.path.exists(urljoin(self.tmpdirname, self.repo_name))

    def test_db_decompress_repo(self):

        repo_comp = self.repodb + ".tar.gz"
        rpath = urljoin(self.tmpdirname, repo_comp)
        assert os.path.exists(rpath)

        decompress_repo(rpath, self.tmpdirname)

        assert os.path.exists(urljoin(self.tmpdirname, self.repodb + ".db"))

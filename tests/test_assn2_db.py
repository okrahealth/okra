""" Validate assn2_db functions """
import unittest

from sqlalchemy import Table, Column, Integer, MetaData

from okra.assn2_db import metadata_tosql

class TestAssn2Db(unittest.TestCase):

    def setUp(self):
        metadata = MetaData()
        mock_table = Table('mock_table', metadata,
                           Column('id', Integer, primary_key=True),
        )
        self.metadata = metadata

    def tearDown(self):
        pass

    def test_metadata_tosql(self):
        db_url = 'sqlite:///:memory:'
        output = metadata_tosql(self.metadata, db_url)

        stmt = """\nCREATE TABLE mock_table (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)\n)\n\n\n"""
        print(output)
        assert len(output) > 0
        assert output == stmt

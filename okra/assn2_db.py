"""
Database Schemata

http://janvitek.org/events/NEU/6050/a2.html
"""
import io
from contextlib import redirect_stdout
from sqlalchemy import create_engine
from sqlalchemy import (Table, Column, Integer, String, MetaData,
                        ForeignKey, DateTime)

def config_assn2_schema():
    """ Configure the database schema for assignment 2 """
    metadata = MetaData()

    commit_meta = Table('commit_meta', metadata,
                        Column('id', Integer, primary_key=True, nullable=False),
                       Column('owner_name', String, nullable=False),
                       Column('project_name', String, nullable=False),
                       Column('commit_hash', String,
                              ForeignKey("commit_info.commit_hash"),
                              ForeignKey("commit_author.commit_hash"),
                              ForeignKey("commit_contribs.commit_hash"),
                              ForeignKey("commit_file.commit_hash"),
                              nullable=False, index=True, unique=True),
    )

    commit_author = Table('commit_author', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('commit_hash', String, nullable=False,
                                 index=True, unique=True),
                          Column('author_name', String, nullable=False,
                                 index=True),
                          Column('author_email', String, nullable=True),
                          Column('author_datetime', DateTime, nullable=False),
    )

    commit_contribs = Table('commit_contribs', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('commit_hash', String, nullable=False,
                                   index=True, unique=True),
                            Column('contrib_name', String, nullable=False,
                                   index=True),
                            Column('contrib_email', String, nullable=True),
                            Column('contrib_datetime', DateTime,
                                   nullable=False),
    )

    commit_file = Table('commit_file', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('commit_hash', String, nullable=False,
                               index=True, unique=True),
                        Column('modified_file', String, nullable=False),
                        Column('modified_add_lines', Integer, nullable=False),
                        Column('modified_subtract_lines', Integer,
                               nullable=False),
    )

    commit_info = Table('commit_info', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('commit_hash', String, nullable=False,
                               index=True, unique=True),
                        Column('subject', String, nullable=False),
                        Column('message', String, nullable=False),
    )

    return metadata

def metadata_tosql(metadata: MetaData, db_url: str):
    """ Convert Database metadata into SQL statements. 
    
    Generate SQL for any database supported by SQLAlchemy.
    No commands are executed on a database by this function
    so the db_url can be a mock.

    :param metadata: MetaData object from sqlalchemy containing db schema
    :param db_url: database url, can be a mock
    :return: SQL database schema for db_url database type
    :rtype: string
    """

    def metadata_dump(sql, *multiparams, **params):
        """ print or write to log or file etc """
        print(sql.compile(dialect=engine.dialect))

    engine = create_engine(db_url, strategy='mock', executor=metadata_dump)

    f = io.StringIO()
    with redirect_stdout(f):
        metadata.create_all(engine)
    out = f.getvalue()
    return out
    

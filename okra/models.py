""" SQL Database Models 

This is the database schema used for accessing the SQL database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import (Table, Column, Integer, String, MetaData, Numeric,
                        ForeignKey, DateTime, create_engine)

Base = declarative_base()


class Inventory(Base):

    __tablename__ = 'inventory'

    owner_name = Column('owner_name', String(100), nullable=False,
                        primary_key=True, index=True)
    project_name = Column('project_name', String(150), nullable=False,
                        primary_key=True, index=True)
    last_commit = Column('last_commit', String(40), nullable=True)

class Meta(Base):

    __tablename__ = 'meta'

    commit_hash = Column('commit_hash', String(40), 
                         ForeignKey('author.commit_hash'),
                         ForeignKey('contrib.commit_hash'),
                         ForeignKey('commit_file.commit_hash'),
                         ForeignKey('info.commit_hash'),
                         primary_key=True,
                         index=True)
    owner_name = Column('owner_name', String(100), nullable=False)
    project_name = Column('project_name', String(150), nullable=False)

class Author(Base):
    """ 
    Author email is false, not all authors require a github account,
    so an email is not going to be required. 
    """
    __tablename__ = 'author'

    commit_hash = Column('commit_hash', String(40), primary_key=True,
                         index=True)
    name = Column('name', String(150), nullable=False,
                         index=True)
    email = Column('email', String(200), nullable=True)
    authored = Column('authored', DateTime, nullable=False)

class Contrib(Base):

    __tablename__ = 'contrib'
    contrib_id = Column('contrib_id', Integer, primary_key=True)
    commit_hash = Column('commit_hash', String(40), index=True,
                         nullable=False, primary_key=True)
    name = Column('name', String(150), index=True,
                          nullable=False)
    email = Column('email', String(200), nullable=True)
    contributed = Column('contributed', DateTime, nullable=False)

class CommitFile(Base):
    __tablename__ = 'commit_file'

    file_id = Column('file_id', Integer, primary_key=True)
    commit_hash = Column('commit_hash', String(40), index=True,
                         nullable=False,primary_key=True)
    modified_file = Column('modified_file', String(500), nullable=False)
    lines_added = Column('lines_added', Integer, nullable=False)
    lines_deleted = Column('lines_subtracted', Integer, nullable=False)

class Info(Base):
    __tablename__ = 'info'

    commit_hash = Column('commit_hash', String(40), primary_key=True,
                         index=True)
    subject = Column('subject', String(250), nullable=True)
    message = Column('message', String(1500), nullable=True)
    created = Column('created', DateTime, nullable=False)

    
class DataAccessLayer(object):

    def __init__(self, conn_string):
        self.engine = None
        self.session = None
        self.conn_string = conn_string

    def connect(self):
        self.engine = create_engine(self.conn_string)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


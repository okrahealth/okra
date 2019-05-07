# (generated with --quick)

from typing import Any

Base: Any
Column: Any
DateTime: Any
ForeignKey: Any
Integer: Any
MetaData: Any
Numeric: Any
String: Any
Table: Any
create_engine: Any
declarative_base: Any
relationship: Any
sessionmaker: Any

class Author(Any):
    __doc__: str
    __tablename__: str
    authored: Any
    commit_hash: Any
    email: Any
    name: Any

class CommitFile(Any):
    __tablename__: str
    commit_hash: Any
    file_id: Any
    lines_added: Any
    lines_deleted: Any
    modified_file: Any

class Contrib(Any):
    __tablename__: str
    commit_hash: Any
    contrib_id: Any
    contributed: Any
    email: Any
    name: Any

class DataAccessLayer(object):
    Session: Any
    conn_string: Any
    engine: Any
    session: None
    def __init__(self, conn_string) -> None: ...
    def connect(self) -> None: ...

class Info(Any):
    __tablename__: str
    commit_hash: Any
    created: Any
    message: Any
    subject: Any

class Inventory(Any):
    __tablename__: str
    last_commit: Any
    owner_name: Any
    project_name: Any

class Meta(Any):
    __tablename__: str
    commit_hash: Any
    owner_name: Any
    project_name: Any

# (generated with --quick)

import datetime
import logging
from typing import Optional, Type, TypeVar

datetime: Type[datetime.datetime]
logger: logging.Logger
logging: module
os: module
pa: module
pd: module
pq: module

AnyStr = TypeVar('AnyStr', str, bytes)

def sqlite_to_parquet(tables: list, db_dir, batch_size) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
def write_parquet_table(table_name: str, query: str, db_dir: str, dbs: list, batch_size: int) -> None: ...

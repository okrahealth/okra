# (generated with --quick)

import logging
import okra.models
from typing import Any, Type

Author: Type[okra.models.Author]
CommitFile: Type[okra.models.CommitFile]
Contrib: Type[okra.models.Contrib]
DataAccessLayer: Type[okra.models.DataAccessLayer]
Meta: Type[okra.models.Meta]
func: Any
logger: logging.Logger
logging: module

def find_author_count(dal: okra.models.DataAccessLayer, yearmo = ...) -> Any: ...
def find_contributor_count(dal: okra.models.DataAccessLayer, yearmo = ...) -> Any: ...
def find_file_metrics(dal: okra.models.DataAccessLayer, yearmo = ...) -> Any: ...
def hist_start_yearmo(dal: okra.models.DataAccessLayer) -> Any: ...
def iso_date_aggregation(dal: okra.models.DataAccessLayer, yearmo = ...) -> Any: ...
def repo_info(dal: okra.models.DataAccessLayer, yearmo = ...) -> Any: ...

# (generated with --quick)

import collections
import okra.models
from typing import Any, List, Tuple, Type

Author: Type[okra.models.Author]
CommitFile: Type[okra.models.CommitFile]
Contrib: Type[okra.models.Contrib]
Info: Type[okra.models.Info]
Meta: Type[okra.models.Meta]
defaultdict: Type[collections.defaultdict]
func: Any

def author_file_owned(owner, project, dal) -> Any: ...
def author_number_of_files_owned(results) -> collections.defaultdict: ...
def get_truck_factor_by_project(owner, project, dal) -> Tuple[Any, Any]: ...
def smallest_owner_set(authors, total, size = ...) -> Tuple[int, List[Tuple[Any, Any]]]: ...
def total_number_of_files_by_project(owner, project, dal) -> int: ...

from typing import Union

from .DataResponse import DataResponse as DataResponse
from .ErrorResponse import ErrorResponse as ErrorResponse
from .DeleteResponse import DeleteResponse as DeleteResponse
from .CreateResponse import CreateResponse as CreateResponse

Response = Union[DataResponse, ErrorResponse, DeleteResponse]

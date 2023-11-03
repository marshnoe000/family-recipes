from typing import Union

from .DataResponse import DataResponse as DataResponse
from .ErrorResponse import ErrorResponse as ErrorResponse

Response = Union[DataResponse, ErrorResponse]

from audiotool.genre.v1 import genre_pb2 as _genre_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListGenresRequest(_message.Message):
    __slots__ = ("filter", "page_size", "page_token", "order_by")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListGenresResponse(_message.Message):
    __slots__ = ("genres", "next_page_token")
    GENRES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    genres: _containers.RepeatedCompositeFieldContainer[_genre_pb2.Genre]
    next_page_token: str
    def __init__(self, genres: _Optional[_Iterable[_Union[_genre_pb2.Genre, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetGenreRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetGenreResponse(_message.Message):
    __slots__ = ("genre",)
    GENRE_FIELD_NUMBER: _ClassVar[int]
    genre: _genre_pb2.Genre
    def __init__(self, genre: _Optional[_Union[_genre_pb2.Genre, _Mapping]] = ...) -> None: ...

from audiotool.track.v1 import track_pb2 as _track_pb2
from audiotool.track.v1 import track_listen_by_user_pb2 as _track_listen_by_user_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTracksRequest(_message.Message):
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

class ListTracksResponse(_message.Message):
    __slots__ = ("tracks", "next_page_token")
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tracks: _containers.RepeatedCompositeFieldContainer[_track_pb2.Track]
    next_page_token: str
    def __init__(self, tracks: _Optional[_Iterable[_Union[_track_pb2.Track, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetTrackRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetTrackResponse(_message.Message):
    __slots__ = ("track",)
    TRACK_FIELD_NUMBER: _ClassVar[int]
    track: _track_pb2.Track
    def __init__(self, track: _Optional[_Union[_track_pb2.Track, _Mapping]] = ...) -> None: ...

class DeleteTrackRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteTrackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTrackListenByUserRequest(_message.Message):
    __slots__ = ("track_name", "filter", "page_size", "page_token", "order_by")
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    track_name: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, track_name: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListTrackListenByUserResponse(_message.Message):
    __slots__ = ("listens", "next_page_token")
    LISTENS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    listens: _containers.RepeatedCompositeFieldContainer[_track_listen_by_user_pb2.TrackListenByUser]
    next_page_token: str
    def __init__(self, listens: _Optional[_Iterable[_Union[_track_listen_by_user_pb2.TrackListenByUser, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

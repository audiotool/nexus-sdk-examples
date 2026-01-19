import datetime

from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "description", "num_tracks", "num_albums", "num_followers", "num_following", "tags", "avatar_url", "links")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NUM_TRACKS_FIELD_NUMBER: _ClassVar[int]
    NUM_ALBUMS_FIELD_NUMBER: _ClassVar[int]
    NUM_FOLLOWERS_FIELD_NUMBER: _ClassVar[int]
    NUM_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    description: str
    num_tracks: int
    num_albums: int
    num_followers: int
    num_following: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    avatar_url: str
    links: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., num_tracks: _Optional[int] = ..., num_albums: _Optional[int] = ..., num_followers: _Optional[int] = ..., num_following: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., avatar_url: _Optional[str] = ..., links: _Optional[_Iterable[str]] = ...) -> None: ...

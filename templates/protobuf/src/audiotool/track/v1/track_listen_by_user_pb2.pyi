import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrackListenByUser(_message.Message):
    __slots__ = ("name", "track_name", "user_name", "listen_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    LISTEN_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    track_name: str
    user_name: str
    listen_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., track_name: _Optional[str] = ..., user_name: _Optional[str] = ..., listen_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

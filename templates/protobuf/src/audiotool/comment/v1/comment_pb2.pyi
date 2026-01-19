import datetime

from audiotool.comment.v1 import reaction_pb2 as _reaction_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Comment(_message.Message):
    __slots__ = ("name", "create_time", "creator_name", "text", "update_time", "deleted", "reactions", "from_muted_user")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    FROM_MUTED_USER_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    creator_name: str
    text: str
    update_time: _timestamp_pb2.Timestamp
    deleted: bool
    reactions: _containers.RepeatedCompositeFieldContainer[_reaction_pb2.Reaction]
    from_muted_user: bool
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., creator_name: _Optional[str] = ..., text: _Optional[str] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: _Optional[bool] = ..., reactions: _Optional[_Iterable[_Union[_reaction_pb2.Reaction, _Mapping]]] = ..., from_muted_user: _Optional[bool] = ...) -> None: ...

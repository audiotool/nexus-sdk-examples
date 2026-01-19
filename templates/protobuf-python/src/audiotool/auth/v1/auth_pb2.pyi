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

class Whoami(_message.Message):
    __slots__ = ("user_name", "roles", "is_email_verified", "granted_scopes")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    IS_EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    GRANTED_SCOPES_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    is_email_verified: bool
    granted_scopes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_name: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., is_email_verified: _Optional[bool] = ..., granted_scopes: _Optional[_Iterable[str]] = ...) -> None: ...

class PersonalAccessToken(_message.Message):
    __slots__ = ("name", "display_name", "user_name", "access_token", "create_time", "expire_time", "last_use_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_USE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    user_name: str
    access_token: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    last_use_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., user_name: _Optional[str] = ..., access_token: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_use_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

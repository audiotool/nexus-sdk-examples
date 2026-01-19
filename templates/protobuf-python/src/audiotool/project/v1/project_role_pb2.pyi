import datetime

from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectRoleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROJECT_ROLE_TYPE_UNSPECIFIED: _ClassVar[ProjectRoleType]
    PROJECT_ROLE_TYPE_OWNER: _ClassVar[ProjectRoleType]
    PROJECT_ROLE_TYPE_OWNER_UNPUBLISHED: _ClassVar[ProjectRoleType]
    PROJECT_ROLE_TYPE_EDITOR: _ClassVar[ProjectRoleType]
    PROJECT_ROLE_TYPE_EDITOR_UNPUBLISHED: _ClassVar[ProjectRoleType]
    PROJECT_ROLE_TYPE_VIEWER: _ClassVar[ProjectRoleType]
PROJECT_ROLE_TYPE_UNSPECIFIED: ProjectRoleType
PROJECT_ROLE_TYPE_OWNER: ProjectRoleType
PROJECT_ROLE_TYPE_OWNER_UNPUBLISHED: ProjectRoleType
PROJECT_ROLE_TYPE_EDITOR: ProjectRoleType
PROJECT_ROLE_TYPE_EDITOR_UNPUBLISHED: ProjectRoleType
PROJECT_ROLE_TYPE_VIEWER: ProjectRoleType

class ProjectRole(_message.Message):
    __slots__ = ("name", "user_name", "role_type", "create_time", "update_time", "creator_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_name: str
    role_type: ProjectRoleType
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    creator_name: str
    def __init__(self, name: _Optional[str] = ..., user_name: _Optional[str] = ..., role_type: _Optional[_Union[ProjectRoleType, str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., creator_name: _Optional[str] = ...) -> None: ...

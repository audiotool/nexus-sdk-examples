import datetime

from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPLICATION_MODE_UNSPECIFIED: _ClassVar[ApplicationMode]
    APPLICATION_MODE_DEVELOPMENT: _ClassVar[ApplicationMode]
    APPLICATION_MODE_PUBLISHED: _ClassVar[ApplicationMode]
APPLICATION_MODE_UNSPECIFIED: ApplicationMode
APPLICATION_MODE_DEVELOPMENT: ApplicationMode
APPLICATION_MODE_PUBLISHED: ApplicationMode

class Application(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time", "website_url", "redirect_uris", "creator_name", "logo_uri", "mode", "scopes", "client_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URI_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    website_url: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    creator_name: str
    logo_uri: str
    mode: ApplicationMode
    scopes: _containers.RepeatedScalarFieldContainer[str]
    client_id: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., website_url: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., creator_name: _Optional[str] = ..., logo_uri: _Optional[str] = ..., mode: _Optional[_Union[ApplicationMode, str]] = ..., scopes: _Optional[_Iterable[str]] = ..., client_id: _Optional[str] = ...) -> None: ...

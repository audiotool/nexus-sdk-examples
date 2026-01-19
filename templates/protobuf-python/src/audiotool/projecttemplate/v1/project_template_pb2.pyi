import datetime

from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectTemplateUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROJECT_TEMPLATE_USAGE_UNSPECIFIED: _ClassVar[ProjectTemplateUsage]
    PROJECT_TEMPLATE_USAGE_PUBLIC: _ClassVar[ProjectTemplateUsage]
    PROJECT_TEMPLATE_USAGE_UNLISTED: _ClassVar[ProjectTemplateUsage]
    PROJECT_TEMPLATE_USAGE_PRIVATE: _ClassVar[ProjectTemplateUsage]
PROJECT_TEMPLATE_USAGE_UNSPECIFIED: ProjectTemplateUsage
PROJECT_TEMPLATE_USAGE_PUBLIC: ProjectTemplateUsage
PROJECT_TEMPLATE_USAGE_UNLISTED: ProjectTemplateUsage
PROJECT_TEMPLATE_USAGE_PRIVATE: ProjectTemplateUsage

class ProjectTemplate(_message.Message):
    __slots__ = ("name", "creator_name", "copy_of_project_name", "copy_of_project_commit_index", "display_name", "description", "usage", "tags", "bpm", "favorited_by_user", "num_favorites", "num_usages", "create_time", "update_time", "snapshot_url", "play_duration", "genre_name", "project_data_url", "visual_state_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_OF_PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_OF_PROJECT_COMMIT_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    BPM_FIELD_NUMBER: _ClassVar[int]
    FAVORITED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    NUM_FAVORITES_FIELD_NUMBER: _ClassVar[int]
    NUM_USAGES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    PLAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    GENRE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    VISUAL_STATE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    creator_name: str
    copy_of_project_name: str
    copy_of_project_commit_index: int
    display_name: str
    description: str
    usage: ProjectTemplateUsage
    tags: _containers.RepeatedScalarFieldContainer[str]
    bpm: float
    favorited_by_user: bool
    num_favorites: int
    num_usages: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    snapshot_url: str
    play_duration: _duration_pb2.Duration
    genre_name: str
    project_data_url: str
    visual_state_url: str
    def __init__(self, name: _Optional[str] = ..., creator_name: _Optional[str] = ..., copy_of_project_name: _Optional[str] = ..., copy_of_project_commit_index: _Optional[int] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., usage: _Optional[_Union[ProjectTemplateUsage, str]] = ..., tags: _Optional[_Iterable[str]] = ..., bpm: _Optional[float] = ..., favorited_by_user: _Optional[bool] = ..., num_favorites: _Optional[int] = ..., num_usages: _Optional[int] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., snapshot_url: _Optional[str] = ..., play_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., genre_name: _Optional[str] = ..., project_data_url: _Optional[str] = ..., visual_state_url: _Optional[str] = ...) -> None: ...

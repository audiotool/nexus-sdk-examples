import datetime

from audiotool.project.v1 import project_pb2 as _project_pb2
from audiotool.project.v1 import project_service_pb2 as _project_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SyncTrackStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYNC_TRACK_STATUS_UNSPECIFIED: _ClassVar[SyncTrackStatus]
    SYNC_TRACK_STATUS_STARTED: _ClassVar[SyncTrackStatus]
    SYNC_TRACK_STATUS_AUDIO_RENDERING: _ClassVar[SyncTrackStatus]
    SYNC_TRACK_STATUS_AUDIO_RENDERED: _ClassVar[SyncTrackStatus]
    SYNC_TRACK_STATUS_AUDIO_CONVERTING: _ClassVar[SyncTrackStatus]
    SYNC_TRACK_STATUS_AUDIO_CONVERTED: _ClassVar[SyncTrackStatus]
    SYNC_TRACK_STATUS_FINISHED: _ClassVar[SyncTrackStatus]
SYNC_TRACK_STATUS_UNSPECIFIED: SyncTrackStatus
SYNC_TRACK_STATUS_STARTED: SyncTrackStatus
SYNC_TRACK_STATUS_AUDIO_RENDERING: SyncTrackStatus
SYNC_TRACK_STATUS_AUDIO_RENDERED: SyncTrackStatus
SYNC_TRACK_STATUS_AUDIO_CONVERTING: SyncTrackStatus
SYNC_TRACK_STATUS_AUDIO_CONVERTED: SyncTrackStatus
SYNC_TRACK_STATUS_FINISHED: SyncTrackStatus

class SyncTrackInfo(_message.Message):
    __slots__ = ("project", "mode", "commit_index", "track_name", "user_name", "create_time", "status")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_INDEX_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    mode: _project_service_pb2.SyncTrackMode
    commit_index: int
    track_name: str
    user_name: str
    create_time: _timestamp_pb2.Timestamp
    status: SyncTrackStatus
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ..., mode: _Optional[_Union[_project_service_pb2.SyncTrackMode, str]] = ..., commit_index: _Optional[int] = ..., track_name: _Optional[str] = ..., user_name: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[SyncTrackStatus, str]] = ...) -> None: ...

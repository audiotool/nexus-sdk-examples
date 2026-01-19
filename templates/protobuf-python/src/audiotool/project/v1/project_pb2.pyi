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

class TrackLicense(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACK_LICENSE_UNSPECIFIED: _ClassVar[TrackLicense]
    TRACK_LICENSE_NO_RIGHTS_RESERVED: _ClassVar[TrackLicense]
    TRACK_LICENSE_CREATIVE_COMMONS: _ClassVar[TrackLicense]
    TRACK_LICENSE_CREATIVE_COMMONS_NON_COMMERCIAL: _ClassVar[TrackLicense]
    TRACK_LICENSE_ALL_RIGHTS_RESERVED: _ClassVar[TrackLicense]
    TRACK_LICENSE_ROYALTY_FREE: _ClassVar[TrackLicense]
TRACK_LICENSE_UNSPECIFIED: TrackLicense
TRACK_LICENSE_NO_RIGHTS_RESERVED: TrackLicense
TRACK_LICENSE_CREATIVE_COMMONS: TrackLicense
TRACK_LICENSE_CREATIVE_COMMONS_NON_COMMERCIAL: TrackLicense
TRACK_LICENSE_ALL_RIGHTS_RESERVED: TrackLicense
TRACK_LICENSE_ROYALTY_FREE: TrackLicense

class Project(_message.Message):
    __slots__ = ("name", "user_names", "creator_name", "track_name", "remix_of_track_name", "copy_of_project_name", "copy_of_project_commit_index", "display_name", "description", "create_time", "update_time", "play_duration", "tags", "cover_url", "snapshot_url", "bpm", "genre_name", "download_allowed", "copy_allowed", "license")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAMES_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    REMIX_OF_TRACK_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_OF_PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_OF_PROJECT_COMMIT_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PLAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    COVER_URL_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    BPM_FIELD_NUMBER: _ClassVar[int]
    GENRE_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    COPY_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_names: _containers.RepeatedScalarFieldContainer[str]
    creator_name: str
    track_name: str
    remix_of_track_name: str
    copy_of_project_name: str
    copy_of_project_commit_index: int
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    play_duration: _duration_pb2.Duration
    tags: _containers.RepeatedScalarFieldContainer[str]
    cover_url: str
    snapshot_url: str
    bpm: float
    genre_name: str
    download_allowed: bool
    copy_allowed: bool
    license: TrackLicense
    def __init__(self, name: _Optional[str] = ..., user_names: _Optional[_Iterable[str]] = ..., creator_name: _Optional[str] = ..., track_name: _Optional[str] = ..., remix_of_track_name: _Optional[str] = ..., copy_of_project_name: _Optional[str] = ..., copy_of_project_commit_index: _Optional[int] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., play_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., cover_url: _Optional[str] = ..., snapshot_url: _Optional[str] = ..., bpm: _Optional[float] = ..., genre_name: _Optional[str] = ..., download_allowed: _Optional[bool] = ..., copy_allowed: _Optional[bool] = ..., license: _Optional[_Union[TrackLicense, str]] = ...) -> None: ...

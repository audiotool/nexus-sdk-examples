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

class Track(_message.Message):
    __slots__ = ("name", "project_name", "remix_of", "project_commit_index", "display_name", "description", "contributor_names", "create_time", "update_time", "play_duration", "tags", "cover_url", "snapshot_url", "favorited_by_user", "bpm", "genre_name", "download_allowed", "license", "num_downloads", "num_plays", "num_favorites", "num_comments", "mp3_url", "ogg_url", "wav_url", "hls_url", "remix_allowed")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    REMIX_OF_FIELD_NUMBER: _ClassVar[int]
    PROJECT_COMMIT_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTOR_NAMES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PLAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    COVER_URL_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_URL_FIELD_NUMBER: _ClassVar[int]
    FAVORITED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    BPM_FIELD_NUMBER: _ClassVar[int]
    GENRE_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    NUM_DOWNLOADS_FIELD_NUMBER: _ClassVar[int]
    NUM_PLAYS_FIELD_NUMBER: _ClassVar[int]
    NUM_FAVORITES_FIELD_NUMBER: _ClassVar[int]
    NUM_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    MP3_URL_FIELD_NUMBER: _ClassVar[int]
    OGG_URL_FIELD_NUMBER: _ClassVar[int]
    WAV_URL_FIELD_NUMBER: _ClassVar[int]
    HLS_URL_FIELD_NUMBER: _ClassVar[int]
    REMIX_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_name: str
    remix_of: str
    project_commit_index: int
    display_name: str
    description: str
    contributor_names: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    play_duration: _duration_pb2.Duration
    tags: _containers.RepeatedScalarFieldContainer[str]
    cover_url: str
    snapshot_url: str
    favorited_by_user: bool
    bpm: float
    genre_name: str
    download_allowed: bool
    license: TrackLicense
    num_downloads: int
    num_plays: int
    num_favorites: int
    num_comments: int
    mp3_url: str
    ogg_url: str
    wav_url: str
    hls_url: str
    remix_allowed: bool
    def __init__(self, name: _Optional[str] = ..., project_name: _Optional[str] = ..., remix_of: _Optional[str] = ..., project_commit_index: _Optional[int] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., contributor_names: _Optional[_Iterable[str]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., play_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., cover_url: _Optional[str] = ..., snapshot_url: _Optional[str] = ..., favorited_by_user: _Optional[bool] = ..., bpm: _Optional[float] = ..., genre_name: _Optional[str] = ..., download_allowed: _Optional[bool] = ..., license: _Optional[_Union[TrackLicense, str]] = ..., num_downloads: _Optional[int] = ..., num_plays: _Optional[int] = ..., num_favorites: _Optional[int] = ..., num_comments: _Optional[int] = ..., mp3_url: _Optional[str] = ..., ogg_url: _Optional[str] = ..., wav_url: _Optional[str] = ..., hls_url: _Optional[str] = ..., remix_allowed: _Optional[bool] = ...) -> None: ...

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

class SampleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_TYPE_UNSPECIFIED: _ClassVar[SampleType]
    SAMPLE_TYPE_ONE_SHOT: _ClassVar[SampleType]
    SAMPLE_TYPE_LOOP: _ClassVar[SampleType]

class SampleClearance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_CLEARANCE_UNSPECIFIED: _ClassVar[SampleClearance]
    SAMPLE_CLEARANCE_SAFE: _ClassVar[SampleClearance]
    SAMPLE_CLEARANCE_UNSAFE: _ClassVar[SampleClearance]

class SampleUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_USAGE_UNSPECIFIED: _ClassVar[SampleUsage]
    SAMPLE_USAGE_PUBLIC: _ClassVar[SampleUsage]
    SAMPLE_USAGE_UNLISTED: _ClassVar[SampleUsage]
    SAMPLE_USAGE_PRIVATE: _ClassVar[SampleUsage]
SAMPLE_TYPE_UNSPECIFIED: SampleType
SAMPLE_TYPE_ONE_SHOT: SampleType
SAMPLE_TYPE_LOOP: SampleType
SAMPLE_CLEARANCE_UNSPECIFIED: SampleClearance
SAMPLE_CLEARANCE_SAFE: SampleClearance
SAMPLE_CLEARANCE_UNSAFE: SampleClearance
SAMPLE_USAGE_UNSPECIFIED: SampleUsage
SAMPLE_USAGE_PUBLIC: SampleUsage
SAMPLE_USAGE_UNLISTED: SampleUsage
SAMPLE_USAGE_PRIVATE: SampleUsage

class Sample(_message.Message):
    __slots__ = ("name", "display_name", "description", "owner_name", "favorited_by_user", "num_favorites", "num_usages", "bpm", "sample_type", "play_duration", "create_time", "update_time", "clearance", "usage", "tags", "mp3_url", "wav_url", "preview_mp3_url", "flac_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    FAVORITED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    NUM_FAVORITES_FIELD_NUMBER: _ClassVar[int]
    NUM_USAGES_FIELD_NUMBER: _ClassVar[int]
    BPM_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLEARANCE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MP3_URL_FIELD_NUMBER: _ClassVar[int]
    WAV_URL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_MP3_URL_FIELD_NUMBER: _ClassVar[int]
    FLAC_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    owner_name: str
    favorited_by_user: bool
    num_favorites: int
    num_usages: int
    bpm: float
    sample_type: SampleType
    play_duration: _duration_pb2.Duration
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    clearance: SampleClearance
    usage: SampleUsage
    tags: _containers.RepeatedScalarFieldContainer[str]
    mp3_url: str
    wav_url: str
    preview_mp3_url: str
    flac_url: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., owner_name: _Optional[str] = ..., favorited_by_user: _Optional[bool] = ..., num_favorites: _Optional[int] = ..., num_usages: _Optional[int] = ..., bpm: _Optional[float] = ..., sample_type: _Optional[_Union[SampleType, str]] = ..., play_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., clearance: _Optional[_Union[SampleClearance, str]] = ..., usage: _Optional[_Union[SampleUsage, str]] = ..., tags: _Optional[_Iterable[str]] = ..., mp3_url: _Optional[str] = ..., wav_url: _Optional[str] = ..., preview_mp3_url: _Optional[str] = ..., flac_url: _Optional[str] = ...) -> None: ...

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

class PresetDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESET_DEVICE_TYPE_UNSPECIFIED: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_AUTO_FILTER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_BAND_SPLITTER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_BASSLINE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_BEATBOX8: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_BEATBOX9: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_CROSSFADER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_CURVE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_EXCITER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_GRAPHICAL_EQ: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_GRAVITY: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_HEISENBERG: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_HELMHOLTZ: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_MACHINISTE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_MATRIX: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_NOTE_SPLITTER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_PANORAMA: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_PULSAR: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_PULVERISATEUR: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_QUANTUM: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_QUASAR: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_RASSELBOCK: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_SPACE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STEREO_ENHANCER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_CHORUS: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_COMPRESSOR: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_CRUSHER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_DELAY: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_FLANGER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_GATE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_PARAMETRIC_EQUALIZER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_PHASER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_PITCH_DELAY: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_REVERB: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_SLOPE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_STEREO_DETUNE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_STOMPBOX_TUBE: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_TONEMATRIX: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_WAVESHAPER: _ClassVar[PresetDeviceType]
    PRESET_DEVICE_TYPE_GAKKI: _ClassVar[PresetDeviceType]

class PresetUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESET_USAGE_UNSPECIFIED: _ClassVar[PresetUsage]
    PRESET_USAGE_PUBLIC: _ClassVar[PresetUsage]
    PRESET_USAGE_UNLISTED: _ClassVar[PresetUsage]
    PRESET_USAGE_PRIVATE: _ClassVar[PresetUsage]
PRESET_DEVICE_TYPE_UNSPECIFIED: PresetDeviceType
PRESET_DEVICE_TYPE_AUTO_FILTER: PresetDeviceType
PRESET_DEVICE_TYPE_BAND_SPLITTER: PresetDeviceType
PRESET_DEVICE_TYPE_BASSLINE: PresetDeviceType
PRESET_DEVICE_TYPE_BEATBOX8: PresetDeviceType
PRESET_DEVICE_TYPE_BEATBOX9: PresetDeviceType
PRESET_DEVICE_TYPE_CROSSFADER: PresetDeviceType
PRESET_DEVICE_TYPE_CURVE: PresetDeviceType
PRESET_DEVICE_TYPE_EXCITER: PresetDeviceType
PRESET_DEVICE_TYPE_GRAPHICAL_EQ: PresetDeviceType
PRESET_DEVICE_TYPE_GRAVITY: PresetDeviceType
PRESET_DEVICE_TYPE_HEISENBERG: PresetDeviceType
PRESET_DEVICE_TYPE_HELMHOLTZ: PresetDeviceType
PRESET_DEVICE_TYPE_MACHINISTE: PresetDeviceType
PRESET_DEVICE_TYPE_MATRIX: PresetDeviceType
PRESET_DEVICE_TYPE_NOTE_SPLITTER: PresetDeviceType
PRESET_DEVICE_TYPE_PANORAMA: PresetDeviceType
PRESET_DEVICE_TYPE_PULSAR: PresetDeviceType
PRESET_DEVICE_TYPE_PULVERISATEUR: PresetDeviceType
PRESET_DEVICE_TYPE_QUANTUM: PresetDeviceType
PRESET_DEVICE_TYPE_QUASAR: PresetDeviceType
PRESET_DEVICE_TYPE_RASSELBOCK: PresetDeviceType
PRESET_DEVICE_TYPE_SPACE: PresetDeviceType
PRESET_DEVICE_TYPE_STEREO_ENHANCER: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_CHORUS: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_COMPRESSOR: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_CRUSHER: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_DELAY: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_FLANGER: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_GATE: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_PARAMETRIC_EQUALIZER: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_PHASER: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_PITCH_DELAY: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_REVERB: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_SLOPE: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_STEREO_DETUNE: PresetDeviceType
PRESET_DEVICE_TYPE_STOMPBOX_TUBE: PresetDeviceType
PRESET_DEVICE_TYPE_TONEMATRIX: PresetDeviceType
PRESET_DEVICE_TYPE_WAVESHAPER: PresetDeviceType
PRESET_DEVICE_TYPE_GAKKI: PresetDeviceType
PRESET_USAGE_UNSPECIFIED: PresetUsage
PRESET_USAGE_PUBLIC: PresetUsage
PRESET_USAGE_UNLISTED: PresetUsage
PRESET_USAGE_PRIVATE: PresetUsage

class Preset(_message.Message):
    __slots__ = ("name", "display_name", "description", "owner_name", "favorited_by_user", "num_favorites", "num_usages", "create_time", "update_time", "usage", "tags", "device_type", "data_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    FAVORITED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    NUM_FAVORITES_FIELD_NUMBER: _ClassVar[int]
    NUM_USAGES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    owner_name: str
    favorited_by_user: bool
    num_favorites: int
    num_usages: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    usage: PresetUsage
    tags: _containers.RepeatedScalarFieldContainer[str]
    device_type: PresetDeviceType
    data_url: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., owner_name: _Optional[str] = ..., favorited_by_user: _Optional[bool] = ..., num_favorites: _Optional[int] = ..., num_usages: _Optional[int] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., usage: _Optional[_Union[PresetUsage, str]] = ..., tags: _Optional[_Iterable[str]] = ..., device_type: _Optional[_Union[PresetDeviceType, str]] = ..., data_url: _Optional[str] = ...) -> None: ...

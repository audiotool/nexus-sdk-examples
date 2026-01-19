from audiotool.audiograph.v1 import audiograph_pb2 as _audiograph_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAudiographResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GET_AUDIOGRAPH_RESOLUTION_UNSPECIFIED: _ClassVar[GetAudiographResolution]
    GET_AUDIOGRAPH_RESOLUTION_120: _ClassVar[GetAudiographResolution]
    GET_AUDIOGRAPH_RESOLUTION_240: _ClassVar[GetAudiographResolution]
    GET_AUDIOGRAPH_RESOLUTION_480: _ClassVar[GetAudiographResolution]
    GET_AUDIOGRAPH_RESOLUTION_960: _ClassVar[GetAudiographResolution]
    GET_AUDIOGRAPH_RESOLUTION_1920: _ClassVar[GetAudiographResolution]
    GET_AUDIOGRAPH_RESOLUTION_3840: _ClassVar[GetAudiographResolution]

class GetAudiographChannels(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GET_AUDIOGRAPH_CHANNELS_UNSPECIFIED: _ClassVar[GetAudiographChannels]
    GET_AUDIOGRAPH_CHANNELS_MONO: _ClassVar[GetAudiographChannels]
    GET_AUDIOGRAPH_CHANNELS_STEREO: _ClassVar[GetAudiographChannels]
GET_AUDIOGRAPH_RESOLUTION_UNSPECIFIED: GetAudiographResolution
GET_AUDIOGRAPH_RESOLUTION_120: GetAudiographResolution
GET_AUDIOGRAPH_RESOLUTION_240: GetAudiographResolution
GET_AUDIOGRAPH_RESOLUTION_480: GetAudiographResolution
GET_AUDIOGRAPH_RESOLUTION_960: GetAudiographResolution
GET_AUDIOGRAPH_RESOLUTION_1920: GetAudiographResolution
GET_AUDIOGRAPH_RESOLUTION_3840: GetAudiographResolution
GET_AUDIOGRAPH_CHANNELS_UNSPECIFIED: GetAudiographChannels
GET_AUDIOGRAPH_CHANNELS_MONO: GetAudiographChannels
GET_AUDIOGRAPH_CHANNELS_STEREO: GetAudiographChannels

class GetAudiographsRequest(_message.Message):
    __slots__ = ("resource_names", "resolution", "channels")
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    resource_names: _containers.RepeatedScalarFieldContainer[str]
    resolution: GetAudiographResolution
    channels: GetAudiographChannels
    def __init__(self, resource_names: _Optional[_Iterable[str]] = ..., resolution: _Optional[_Union[GetAudiographResolution, str]] = ..., channels: _Optional[_Union[GetAudiographChannels, str]] = ...) -> None: ...

class GetAudiographsResponse(_message.Message):
    __slots__ = ("audiographs",)
    AUDIOGRAPHS_FIELD_NUMBER: _ClassVar[int]
    audiographs: _containers.RepeatedCompositeFieldContainer[_audiograph_pb2.Audiograph]
    def __init__(self, audiographs: _Optional[_Iterable[_Union[_audiograph_pb2.Audiograph, _Mapping]]] = ...) -> None: ...

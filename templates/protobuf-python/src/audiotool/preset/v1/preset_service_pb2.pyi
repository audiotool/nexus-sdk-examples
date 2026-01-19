from audiotool.preset.v1 import preset_pb2 as _preset_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPresetsRequest(_message.Message):
    __slots__ = ("filter", "page_size", "page_token", "order_by", "text_search")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    TEXT_SEARCH_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page_size: int
    page_token: str
    order_by: str
    text_search: str
    def __init__(self, filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., text_search: _Optional[str] = ...) -> None: ...

class ListPresetsResponse(_message.Message):
    __slots__ = ("presets", "next_page_token")
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    presets: _containers.RepeatedCompositeFieldContainer[_preset_pb2.Preset]
    next_page_token: str
    def __init__(self, presets: _Optional[_Iterable[_Union[_preset_pb2.Preset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetPresetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetPresetResponse(_message.Message):
    __slots__ = ("preset",)
    PRESET_FIELD_NUMBER: _ClassVar[int]
    preset: _preset_pb2.Preset
    def __init__(self, preset: _Optional[_Union[_preset_pb2.Preset, _Mapping]] = ...) -> None: ...

class CreatePresetRequest(_message.Message):
    __slots__ = ("preset", "data")
    PRESET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    preset: _preset_pb2.Preset
    data: _any_pb2.Any
    def __init__(self, preset: _Optional[_Union[_preset_pb2.Preset, _Mapping]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class CreatePresetResponse(_message.Message):
    __slots__ = ("preset",)
    PRESET_FIELD_NUMBER: _ClassVar[int]
    preset: _preset_pb2.Preset
    def __init__(self, preset: _Optional[_Union[_preset_pb2.Preset, _Mapping]] = ...) -> None: ...

class UpdatePresetRequest(_message.Message):
    __slots__ = ("preset", "update_mask", "data")
    PRESET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    preset: _preset_pb2.Preset
    update_mask: _field_mask_pb2.FieldMask
    data: _any_pb2.Any
    def __init__(self, preset: _Optional[_Union[_preset_pb2.Preset, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class UpdatePresetResponse(_message.Message):
    __slots__ = ("preset",)
    PRESET_FIELD_NUMBER: _ClassVar[int]
    preset: _preset_pb2.Preset
    def __init__(self, preset: _Optional[_Union[_preset_pb2.Preset, _Mapping]] = ...) -> None: ...

class DeletePresetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeletePresetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

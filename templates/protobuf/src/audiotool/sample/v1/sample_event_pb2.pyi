import datetime

from audiotool.sample.v1 import sample_pb2 as _sample_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleConvertDoneErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_CONVERT_DONE_ERROR_TYPE_UNSPECIFIED: _ClassVar[SampleConvertDoneErrorType]
    SAMPLE_CONVERT_DONE_ERROR_TYPE_NONE: _ClassVar[SampleConvertDoneErrorType]
    SAMPLE_CONVERT_DONE_ERROR_TYPE_INVALID_INPUT: _ClassVar[SampleConvertDoneErrorType]
    SAMPLE_CONVERT_DONE_ERROR_TYPE_INTERNAL: _ClassVar[SampleConvertDoneErrorType]
SAMPLE_CONVERT_DONE_ERROR_TYPE_UNSPECIFIED: SampleConvertDoneErrorType
SAMPLE_CONVERT_DONE_ERROR_TYPE_NONE: SampleConvertDoneErrorType
SAMPLE_CONVERT_DONE_ERROR_TYPE_INVALID_INPUT: SampleConvertDoneErrorType
SAMPLE_CONVERT_DONE_ERROR_TYPE_INTERNAL: SampleConvertDoneErrorType

class SampleEvent(_message.Message):
    __slots__ = ("id", "create_time", "sample_convert_done")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_CONVERT_DONE_FIELD_NUMBER: _ClassVar[int]
    id: str
    create_time: _timestamp_pb2.Timestamp
    sample_convert_done: SampleConvertDone
    def __init__(self, id: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sample_convert_done: _Optional[_Union[SampleConvertDone, _Mapping]] = ...) -> None: ...

class SampleConvertDone(_message.Message):
    __slots__ = ("sample", "error")
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sample: _sample_pb2.Sample
    error: SampleConvertDoneErrorType
    def __init__(self, sample: _Optional[_Union[_sample_pb2.Sample, _Mapping]] = ..., error: _Optional[_Union[SampleConvertDoneErrorType, str]] = ...) -> None: ...

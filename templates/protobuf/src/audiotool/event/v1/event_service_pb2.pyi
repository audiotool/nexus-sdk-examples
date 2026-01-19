from audiotool.event.v1 import event_pb2 as _event_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListenRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListenResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _event_pb2.Event
    def __init__(self, event: _Optional[_Union[_event_pb2.Event, _Mapping]] = ...) -> None: ...

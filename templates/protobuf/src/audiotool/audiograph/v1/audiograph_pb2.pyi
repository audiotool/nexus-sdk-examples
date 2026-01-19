from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Graph(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class Audiograph(_message.Message):
    __slots__ = ("resource_name", "graphs")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    GRAPHS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    graphs: _containers.RepeatedCompositeFieldContainer[Graph]
    def __init__(self, resource_name: _Optional[str] = ..., graphs: _Optional[_Iterable[_Union[Graph, _Mapping]]] = ...) -> None: ...

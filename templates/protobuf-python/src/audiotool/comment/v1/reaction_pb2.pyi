from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Reaction(_message.Message):
    __slots__ = ("reaction_name", "user_names")
    REACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAMES_FIELD_NUMBER: _ClassVar[int]
    reaction_name: str
    user_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, reaction_name: _Optional[str] = ..., user_names: _Optional[_Iterable[str]] = ...) -> None: ...

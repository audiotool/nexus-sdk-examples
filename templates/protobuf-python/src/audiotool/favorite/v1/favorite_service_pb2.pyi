from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFavoriteRequest(_message.Message):
    __slots__ = ("parent", "user_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_name: str
    def __init__(self, parent: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class CreateFavoriteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFavoriteRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteFavoriteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

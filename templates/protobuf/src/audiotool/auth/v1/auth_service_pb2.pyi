from audiotool.auth.v1 import auth_pb2 as _auth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWhoamiRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWhoamiResponse(_message.Message):
    __slots__ = ("whoami",)
    WHOAMI_FIELD_NUMBER: _ClassVar[int]
    whoami: _auth_pb2.Whoami
    def __init__(self, whoami: _Optional[_Union[_auth_pb2.Whoami, _Mapping]] = ...) -> None: ...

class ListPersonalAccessTokensRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPersonalAccessTokensResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[_auth_pb2.PersonalAccessToken]
    def __init__(self, tokens: _Optional[_Iterable[_Union[_auth_pb2.PersonalAccessToken, _Mapping]]] = ...) -> None: ...

class CreatePersonalAccessTokenRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.PersonalAccessToken
    def __init__(self, token: _Optional[_Union[_auth_pb2.PersonalAccessToken, _Mapping]] = ...) -> None: ...

class CreatePersonalAccessTokenResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.PersonalAccessToken
    def __init__(self, token: _Optional[_Union[_auth_pb2.PersonalAccessToken, _Mapping]] = ...) -> None: ...

class DeletePersonalAccessTokenRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeletePersonalAccessTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

from audiotool.user.v1 import settings_pb2 as _settings_pb2
from audiotool.user.v1 import user_pb2 as _user_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUsersRequest(_message.Message):
    __slots__ = ("filter", "page_size", "page_token", "order_by")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    next_page_token: str
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user", "update_mask")
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _settings_pb2.Settings
    def __init__(self, settings: _Optional[_Union[_settings_pb2.Settings, _Mapping]] = ...) -> None: ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ("name", "settings", "update_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    settings: _settings_pb2.Settings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., settings: _Optional[_Union[_settings_pb2.Settings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _settings_pb2.Settings
    def __init__(self, settings: _Optional[_Union[_settings_pb2.Settings, _Mapping]] = ...) -> None: ...

class UploadAvatarRequest(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class UploadAvatarResponse(_message.Message):
    __slots__ = ("avatar_url",)
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    avatar_url: str
    def __init__(self, avatar_url: _Optional[str] = ...) -> None: ...

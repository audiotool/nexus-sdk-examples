from audiotool.project.v1 import project_role_pb2 as _project_role_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProjectRolesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListProjectRolesResponse(_message.Message):
    __slots__ = ("project_roles", "next_page_token")
    PROJECT_ROLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_roles: _containers.RepeatedCompositeFieldContainer[_project_role_pb2.ProjectRole]
    next_page_token: str
    def __init__(self, project_roles: _Optional[_Iterable[_Union[_project_role_pb2.ProjectRole, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateProjectRoleRequest(_message.Message):
    __slots__ = ("parent", "project_role")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    project_role: _project_role_pb2.ProjectRole
    def __init__(self, parent: _Optional[str] = ..., project_role: _Optional[_Union[_project_role_pb2.ProjectRole, _Mapping]] = ...) -> None: ...

class CreateProjectRoleResponse(_message.Message):
    __slots__ = ("project_role",)
    PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    project_role: _project_role_pb2.ProjectRole
    def __init__(self, project_role: _Optional[_Union[_project_role_pb2.ProjectRole, _Mapping]] = ...) -> None: ...

class DeleteProjectRoleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteProjectRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateProjectRoleRequest(_message.Message):
    __slots__ = ("project_role", "update_mask")
    PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project_role: _project_role_pb2.ProjectRole
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, project_role: _Optional[_Union[_project_role_pb2.ProjectRole, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateProjectRoleResponse(_message.Message):
    __slots__ = ("project_role",)
    PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    project_role: _project_role_pb2.ProjectRole
    def __init__(self, project_role: _Optional[_Union[_project_role_pb2.ProjectRole, _Mapping]] = ...) -> None: ...

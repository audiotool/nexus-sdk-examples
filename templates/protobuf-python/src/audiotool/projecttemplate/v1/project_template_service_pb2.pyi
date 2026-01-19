from audiotool.projecttemplate.v1 import project_template_pb2 as _project_template_pb2
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

class ListProjectTemplatesRequest(_message.Message):
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

class ListProjectTemplatesResponse(_message.Message):
    __slots__ = ("project_templates", "next_page_token")
    PROJECT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_templates: _containers.RepeatedCompositeFieldContainer[_project_template_pb2.ProjectTemplate]
    next_page_token: str
    def __init__(self, project_templates: _Optional[_Iterable[_Union[_project_template_pb2.ProjectTemplate, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetProjectTemplateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetProjectTemplateResponse(_message.Message):
    __slots__ = ("project_template",)
    PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    project_template: _project_template_pb2.ProjectTemplate
    def __init__(self, project_template: _Optional[_Union[_project_template_pb2.ProjectTemplate, _Mapping]] = ...) -> None: ...

class CreateProjectTemplateRequest(_message.Message):
    __slots__ = ("project_template", "visual_state")
    PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    VISUAL_STATE_FIELD_NUMBER: _ClassVar[int]
    project_template: _project_template_pb2.ProjectTemplate
    visual_state: _any_pb2.Any
    def __init__(self, project_template: _Optional[_Union[_project_template_pb2.ProjectTemplate, _Mapping]] = ..., visual_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class CreateProjectTemplateResponse(_message.Message):
    __slots__ = ("project_template",)
    PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    project_template: _project_template_pb2.ProjectTemplate
    def __init__(self, project_template: _Optional[_Union[_project_template_pb2.ProjectTemplate, _Mapping]] = ...) -> None: ...

class UpdateProjectTemplateRequest(_message.Message):
    __slots__ = ("project_template", "visual_state", "update_mask")
    PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    VISUAL_STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project_template: _project_template_pb2.ProjectTemplate
    visual_state: _any_pb2.Any
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, project_template: _Optional[_Union[_project_template_pb2.ProjectTemplate, _Mapping]] = ..., visual_state: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateProjectTemplateResponse(_message.Message):
    __slots__ = ("project_template",)
    PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    project_template: _project_template_pb2.ProjectTemplate
    def __init__(self, project_template: _Optional[_Union[_project_template_pb2.ProjectTemplate, _Mapping]] = ...) -> None: ...

class DeleteProjectTemplateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteProjectTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

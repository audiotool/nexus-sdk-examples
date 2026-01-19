from audiotool.application.v1 import application_pb2 as _application_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListApplicationsRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: str
    def __init__(self, filter: _Optional[str] = ...) -> None: ...

class ListApplicationsResponse(_message.Message):
    __slots__ = ("applications",)
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[_application_pb2.Application]
    def __init__(self, applications: _Optional[_Iterable[_Union[_application_pb2.Application, _Mapping]]] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetApplicationResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class CreateApplicationResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ("application", "update_mask")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateApplicationResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteApplicationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadLogoRequest(_message.Message):
    __slots__ = ("name", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: bytes
    def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadLogoResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

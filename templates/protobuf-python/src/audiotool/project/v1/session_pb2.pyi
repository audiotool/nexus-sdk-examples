from audiotool.project.v1 import project_pb2 as _project_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ("project", "document_service_url", "studio_prefix_url", "document_service_prefix_url", "audio_engine_prefix_url")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SERVICE_URL_FIELD_NUMBER: _ClassVar[int]
    STUDIO_PREFIX_URL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SERVICE_PREFIX_URL_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENGINE_PREFIX_URL_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    document_service_url: str
    studio_prefix_url: str
    document_service_prefix_url: str
    audio_engine_prefix_url: str
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ..., document_service_url: _Optional[str] = ..., studio_prefix_url: _Optional[str] = ..., document_service_prefix_url: _Optional[str] = ..., audio_engine_prefix_url: _Optional[str] = ...) -> None: ...

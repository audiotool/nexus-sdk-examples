from audiotool.sample.v1 import sample_pb2 as _sample_pb2
from audiotool.sample.v1 import sample_event_pb2 as _sample_event_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListSamplesRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter", "order_by", "text_search")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    TEXT_SEARCH_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    order_by: str
    text_search: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., text_search: _Optional[str] = ...) -> None: ...

class ListSamplesResponse(_message.Message):
    __slots__ = ("samples", "next_page_token")
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    samples: _containers.RepeatedCompositeFieldContainer[_sample_pb2.Sample]
    next_page_token: str
    def __init__(self, samples: _Optional[_Iterable[_Union[_sample_pb2.Sample, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateSampleRequest(_message.Message):
    __slots__ = ("sample",)
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    sample: _sample_pb2.Sample
    def __init__(self, sample: _Optional[_Union[_sample_pb2.Sample, _Mapping]] = ...) -> None: ...

class SampleUploadEndpoint(_message.Message):
    __slots__ = ("upload_url", "headers")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    headers: _containers.ScalarMap[str, str]
    def __init__(self, upload_url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateSampleResponse(_message.Message):
    __slots__ = ("sample", "upload_endpoint")
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    sample: _sample_pb2.Sample
    upload_endpoint: SampleUploadEndpoint
    def __init__(self, sample: _Optional[_Union[_sample_pb2.Sample, _Mapping]] = ..., upload_endpoint: _Optional[_Union[SampleUploadEndpoint, _Mapping]] = ...) -> None: ...

class UploadSampleFinishedRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UploadSampleFinishedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSampleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSampleResponse(_message.Message):
    __slots__ = ("sample",)
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    sample: _sample_pb2.Sample
    def __init__(self, sample: _Optional[_Union[_sample_pb2.Sample, _Mapping]] = ...) -> None: ...

class UpdateSampleRequest(_message.Message):
    __slots__ = ("sample", "update_mask")
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sample: _sample_pb2.Sample
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, sample: _Optional[_Union[_sample_pb2.Sample, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSampleResponse(_message.Message):
    __slots__ = ("sample",)
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    sample: _sample_pb2.Sample
    def __init__(self, sample: _Optional[_Union[_sample_pb2.Sample, _Mapping]] = ...) -> None: ...

class DeleteSampleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSampleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListenRequest(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class ListenResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _sample_event_pb2.SampleEvent
    def __init__(self, event: _Optional[_Union[_sample_event_pb2.SampleEvent, _Mapping]] = ...) -> None: ...

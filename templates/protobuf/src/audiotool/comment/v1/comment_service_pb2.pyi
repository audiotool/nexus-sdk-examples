from audiotool.comment.v1 import comment_pb2 as _comment_pb2
from audiotool.comment.v1 import possible_reaction_pb2 as _possible_reaction_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCommentsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "hide_children")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    HIDE_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    hide_children: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., hide_children: _Optional[bool] = ...) -> None: ...

class ListCommentsResponse(_message.Message):
    __slots__ = ("comments", "next_page_token")
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_comment_pb2.Comment]
    next_page_token: str
    def __init__(self, comments: _Optional[_Iterable[_Union[_comment_pb2.Comment, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ("parent", "comment")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    comment: _comment_pb2.Comment
    def __init__(self, parent: _Optional[str] = ..., comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class CreateCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class GetCommentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class UpdateCommentRequest(_message.Message):
    __slots__ = ("comment", "update_mask")
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class DeleteCommentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteCommentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPossibleReactionsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter", "order_by")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListPossibleReactionsResponse(_message.Message):
    __slots__ = ("possible_reactions", "url_prefix")
    POSSIBLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    URL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    possible_reactions: _containers.RepeatedCompositeFieldContainer[_possible_reaction_pb2.PossibleReaction]
    url_prefix: str
    def __init__(self, possible_reactions: _Optional[_Iterable[_Union[_possible_reaction_pb2.PossibleReaction, _Mapping]]] = ..., url_prefix: _Optional[str] = ...) -> None: ...

class AddReactionRequest(_message.Message):
    __slots__ = ("reaction_name", "comment_name")
    REACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    reaction_name: str
    comment_name: str
    def __init__(self, reaction_name: _Optional[str] = ..., comment_name: _Optional[str] = ...) -> None: ...

class AddReactionResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class RemoveReactionRequest(_message.Message):
    __slots__ = ("reaction_name", "comment_name")
    REACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    reaction_name: str
    comment_name: str
    def __init__(self, reaction_name: _Optional[str] = ..., comment_name: _Optional[str] = ...) -> None: ...

class RemoveReactionResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMENT_MODE_UNSPECIFIED: _ClassVar[CommentMode]
    COMMENT_MODE_PUBLIC: _ClassVar[CommentMode]
    COMMENT_MODE_USERS_FOLLOWING: _ClassVar[CommentMode]
    COMMENT_MODE_DISABLED: _ClassVar[CommentMode]
COMMENT_MODE_UNSPECIFIED: CommentMode
COMMENT_MODE_PUBLIC: CommentMode
COMMENT_MODE_USERS_FOLLOWING: CommentMode
COMMENT_MODE_DISABLED: CommentMode

class Settings(_message.Message):
    __slots__ = ("user_page_comment_mode", "default_track_comment_mode", "default_playlist_comment_mode", "show_online_status", "show_as_listener", "newsletter_subscriber", "allow_links_on_user_page_comments", "allow_links_on_track_comments", "allow_links_on_playlist_comments")
    USER_PAGE_COMMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TRACK_COMMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PLAYLIST_COMMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    SHOW_ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SHOW_AS_LISTENER_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_SUBSCRIBER_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LINKS_ON_USER_PAGE_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LINKS_ON_TRACK_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LINKS_ON_PLAYLIST_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    user_page_comment_mode: CommentMode
    default_track_comment_mode: CommentMode
    default_playlist_comment_mode: CommentMode
    show_online_status: bool
    show_as_listener: bool
    newsletter_subscriber: bool
    allow_links_on_user_page_comments: bool
    allow_links_on_track_comments: bool
    allow_links_on_playlist_comments: bool
    def __init__(self, user_page_comment_mode: _Optional[_Union[CommentMode, str]] = ..., default_track_comment_mode: _Optional[_Union[CommentMode, str]] = ..., default_playlist_comment_mode: _Optional[_Union[CommentMode, str]] = ..., show_online_status: _Optional[bool] = ..., show_as_listener: _Optional[bool] = ..., newsletter_subscriber: _Optional[bool] = ..., allow_links_on_user_page_comments: _Optional[bool] = ..., allow_links_on_track_comments: _Optional[bool] = ..., allow_links_on_playlist_comments: _Optional[bool] = ...) -> None: ...

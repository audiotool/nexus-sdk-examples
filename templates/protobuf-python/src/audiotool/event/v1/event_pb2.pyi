import datetime

from audiotool.comment.v1 import comment_pb2 as _comment_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleConvertDoneErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLE_CONVERT_DONE_ERROR_TYPE_UNSPECIFIED: _ClassVar[SampleConvertDoneErrorType]
    SAMPLE_CONVERT_DONE_ERROR_TYPE_NONE: _ClassVar[SampleConvertDoneErrorType]
    SAMPLE_CONVERT_DONE_ERROR_TYPE_INVALID_INPUT: _ClassVar[SampleConvertDoneErrorType]
    SAMPLE_CONVERT_DONE_ERROR_TYPE_INTERNAL: _ClassVar[SampleConvertDoneErrorType]
SAMPLE_CONVERT_DONE_ERROR_TYPE_UNSPECIFIED: SampleConvertDoneErrorType
SAMPLE_CONVERT_DONE_ERROR_TYPE_NONE: SampleConvertDoneErrorType
SAMPLE_CONVERT_DONE_ERROR_TYPE_INVALID_INPUT: SampleConvertDoneErrorType
SAMPLE_CONVERT_DONE_ERROR_TYPE_INTERNAL: SampleConvertDoneErrorType

class Event(_message.Message):
    __slots__ = ("id", "create_time", "project_access_granted", "user_joined_session", "user_left_session", "sample_convert_done", "synced_track", "track_favorited", "sample_favorited", "preset_favorited", "playlist_favorited", "user_following", "operation", "user_commented", "user_updated_comment", "deleted_comment")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ACCESS_GRANTED_FIELD_NUMBER: _ClassVar[int]
    USER_JOINED_SESSION_FIELD_NUMBER: _ClassVar[int]
    USER_LEFT_SESSION_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_CONVERT_DONE_FIELD_NUMBER: _ClassVar[int]
    SYNCED_TRACK_FIELD_NUMBER: _ClassVar[int]
    TRACK_FAVORITED_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FAVORITED_FIELD_NUMBER: _ClassVar[int]
    PRESET_FAVORITED_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_FAVORITED_FIELD_NUMBER: _ClassVar[int]
    USER_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    USER_COMMENTED_FIELD_NUMBER: _ClassVar[int]
    USER_UPDATED_COMMENT_FIELD_NUMBER: _ClassVar[int]
    DELETED_COMMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    create_time: _timestamp_pb2.Timestamp
    project_access_granted: ProjectAccessGranted
    user_joined_session: UserJoinedSession
    user_left_session: UserLeftSession
    sample_convert_done: SampleConvertDone
    synced_track: SyncedTrack
    track_favorited: TrackFavorited
    sample_favorited: SampleFavorited
    preset_favorited: PresetFavorited
    playlist_favorited: PlaylistFavorited
    user_following: UserFollowing
    operation: _operations_pb2.Operation
    user_commented: UserCommented
    user_updated_comment: UserUpdatedComment
    deleted_comment: DeletedComment
    def __init__(self, id: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., project_access_granted: _Optional[_Union[ProjectAccessGranted, _Mapping]] = ..., user_joined_session: _Optional[_Union[UserJoinedSession, _Mapping]] = ..., user_left_session: _Optional[_Union[UserLeftSession, _Mapping]] = ..., sample_convert_done: _Optional[_Union[SampleConvertDone, _Mapping]] = ..., synced_track: _Optional[_Union[SyncedTrack, _Mapping]] = ..., track_favorited: _Optional[_Union[TrackFavorited, _Mapping]] = ..., sample_favorited: _Optional[_Union[SampleFavorited, _Mapping]] = ..., preset_favorited: _Optional[_Union[PresetFavorited, _Mapping]] = ..., playlist_favorited: _Optional[_Union[PlaylistFavorited, _Mapping]] = ..., user_following: _Optional[_Union[UserFollowing, _Mapping]] = ..., operation: _Optional[_Union[_operations_pb2.Operation, _Mapping]] = ..., user_commented: _Optional[_Union[UserCommented, _Mapping]] = ..., user_updated_comment: _Optional[_Union[UserUpdatedComment, _Mapping]] = ..., deleted_comment: _Optional[_Union[DeletedComment, _Mapping]] = ...) -> None: ...

class ProjectAccessGranted(_message.Message):
    __slots__ = ("project_role", "project")
    PROJECT_ROLE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project_role: _any_pb2.Any
    project: _any_pb2.Any
    def __init__(self, project_role: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., project: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class SyncedTrack(_message.Message):
    __slots__ = ("project_name", "track")
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    project_name: str
    track: _any_pb2.Any
    def __init__(self, project_name: _Optional[str] = ..., track: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class SampleConvertDone(_message.Message):
    __slots__ = ("sample_name", "error")
    SAMPLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sample_name: str
    error: SampleConvertDoneErrorType
    def __init__(self, sample_name: _Optional[str] = ..., error: _Optional[_Union[SampleConvertDoneErrorType, str]] = ...) -> None: ...

class UserJoinedSession(_message.Message):
    __slots__ = ("user_name", "project_name", "project")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    project_name: str
    project: _any_pb2.Any
    def __init__(self, user_name: _Optional[str] = ..., project_name: _Optional[str] = ..., project: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class UserLeftSession(_message.Message):
    __slots__ = ("user_name", "project_name", "project")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    project_name: str
    project: _any_pb2.Any
    def __init__(self, user_name: _Optional[str] = ..., project_name: _Optional[str] = ..., project: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class TrackFavorited(_message.Message):
    __slots__ = ("name", "user_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_name: str
    def __init__(self, name: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class SampleFavorited(_message.Message):
    __slots__ = ("name", "user_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_name: str
    def __init__(self, name: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class PresetFavorited(_message.Message):
    __slots__ = ("name", "user_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_name: str
    def __init__(self, name: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class PlaylistFavorited(_message.Message):
    __slots__ = ("name", "user_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_name: str
    def __init__(self, name: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class UserFollowing(_message.Message):
    __slots__ = ("user_name",)
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    def __init__(self, user_name: _Optional[str] = ...) -> None: ...

class UserCommented(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class UserUpdatedComment(_message.Message):
    __slots__ = ("before", "now")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    NOW_FIELD_NUMBER: _ClassVar[int]
    before: _comment_pb2.Comment
    now: _comment_pb2.Comment
    def __init__(self, before: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ..., now: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

class DeletedComment(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]] = ...) -> None: ...

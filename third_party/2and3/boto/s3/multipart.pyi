from typing import Any, Optional

class CompleteMultiPartUpload:
    bucket = ...  # type: Any
    location = ...  # type: Any
    bucket_name = ...  # type: Any
    key_name = ...  # type: Any
    etag = ...  # type: Any
    version_id = ...  # type: Any
    encrypted = ...  # type: Any
    def __init__(self, bucket: Optional[Any] = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...

class Part:
    bucket = ...  # type: Any
    part_number = ...  # type: Any
    last_modified = ...  # type: Any
    etag = ...  # type: Any
    size = ...  # type: Any
    def __init__(self, bucket: Optional[Any] = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...

def part_lister(mpupload, part_number_marker: Optional[Any] = ...): ...

class MultiPartUpload:
    bucket = ...  # type: Any
    bucket_name = ...  # type: Any
    key_name = ...  # type: Any
    id = ...  # type: Any
    initiator = ...  # type: Any
    owner = ...  # type: Any
    storage_class = ...  # type: Any
    initiated = ...  # type: Any
    part_number_marker = ...  # type: Any
    next_part_number_marker = ...  # type: Any
    max_parts = ...  # type: Any
    is_truncated = ...  # type: bool
    def __init__(self, bucket: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def to_xml(self): ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...
    def get_all_parts(self, max_parts: Optional[Any] = ..., part_number_marker: Optional[Any] = ..., encoding_type: Optional[Any] = ...): ...
    def upload_part_from_file(self, fp, part_num, headers: Optional[Any] = ..., replace: bool = ..., cb: Optional[Any] = ..., num_cb: int = ..., md5: Optional[Any] = ..., size: Optional[Any] = ...): ...
    def copy_part_from_key(self, src_bucket_name, src_key_name, part_num, start: Optional[Any] = ..., end: Optional[Any] = ..., src_version_id: Optional[Any] = ..., headers: Optional[Any] = ...): ...
    def complete_upload(self): ...
    def cancel_upload(self): ...

import typing
import zipfile
from _typeshed import Incomplete

class LinuxZipFileWithPermissions(zipfile.ZipFile):
    def extract(self, member, path: Incomplete | None = ..., pwd: Incomplete | None = ...): ...

class Archive:
    file_path: Incomplete
    os_type: Incomplete
    def __init__(self, path: str, os_type: typing.Optional[str] = ...) -> None: ...
    def unpack(self, directory): ...

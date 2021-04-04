import typing as t

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class GetBookOptions:
    id: t.Union[int, str]


@dataclass_json
@dataclass(frozen=True)
class CreateBookOptions:
    title: t.Text
    author: t.Text
    pages_num: int


@dataclass_json
@dataclass(frozen=True)
class UpdateBookOptions:
    id: int
    title: t.Text
    author: t.Text
    pages_num: int


@dataclass_json
@dataclass(frozen=True)
class DeleteBookOptions:
    id: int

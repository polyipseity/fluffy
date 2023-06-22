# -*- coding: UTF-8 -*-
from typing import Annotated as _Annotated, TypeVar as _TVar

_T = _TVar("_T")
UTF8 = _Annotated[_T, "UTF-8"]
UniversalNewlines = _Annotated[_T, "universal newlines"]


def unsound(self: _T) -> _T:
    return self

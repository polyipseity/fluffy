# -*- coding: UTF-8 -*-
from types import SimpleNamespace as _NS
from typing import (
    Awaitable as _Awaitable,
    Callable as _Call,
    ClassVar as _ClsVar,
    Generic as _Gene,
    Protocol as _Proto,
    TypeVar as _TVar,
    cast as _cast,
)

_S = _TVar("_S")
_V = _TVar("_V")
_SV = _TVar("_SV")


class Lens(_Gene[_S, _V], _Proto):
    __slots__: _ClsVar = ()

    async def get(self, source: _S) -> _V:
        ...

    async def put(self, source: _S, view: _V) -> _S:
        ...


def lens(get: _Call[[_S], _Awaitable[_V]], put: _Call[[_S, _V], _Awaitable[_S]]):
    return _cast(Lens[_S, _V], _NS(get=get, put=put))


def compose(left: Lens[_S, _SV], right: Lens[_SV, _V]) -> Lens[_S, _V]:
    async def get(source: _S):
        return await right.get(await left.get(source))

    async def put(source: _S, view: _V):
        return await left.put(source, await right.put(await left.get(source), view))

    return lens(get, put)

# -*- coding: UTF-8 -*-
from ..semantics import UTF8 as _U8, UniversalNewlines as _UNL, unsound as _unsound
from .lens import Lens as _Lens
from anyio import Path as _Path
from pathlib import PurePath as _PPath
from tokenize import generate_tokens as _gen_tokens, untokenize as _untoken
from typing import ClassVar as _ClsVar, Sequence as _Seq, final as _fin

IOReadLens = _Lens[_Path, _UNL[_U8[str]]]
IOPathLens = _Lens[_Path, _PPath]
LexLens = _Lens[_UNL[_U8[str]], _Seq[tuple[int, str]]]


@_unsound
@_fin
class PyIOReadLens(IOReadLens):
    __slots__: _ClsVar = ()

    async def get(self, source: _Path):
        return await source.read_text("UTF-8", "strict")

    async def put(self, source: _Path, view: _UNL[_U8[str]]):
        await source.write_text(view, "UTF-8", "strict")
        return source


@_fin
class PyIOPathLens(IOPathLens):
    __slots__: _ClsVar = ()

    async def get(self, source: _Path):
        return _PPath(source)

    async def put(self, source: _Path, view: _PPath):
        return _Path(view)


@_fin
class PyLexLens(LexLens):
    __slots__: _ClsVar = ()

    async def get(self, source: _UNL[_U8[str]]):
        return tuple(
            token[:2] for token in _gen_tokens(iter(source.splitlines()).__next__)
        )

    async def put(self, source: str, view: _Seq[tuple[int, str]]):
        return _untoken(view)

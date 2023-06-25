# -*- coding: UTF-8 -*-
from .lens import Lens as _Lens
from dataclasses import dataclass as _dc
from infinitesimals import (  # pyright: ignore[reportMissingTypeStubs]
    HyperReal as _Hreal,
    omega as _omega,
)
from typing import (
    Literal as _Lit,
    NewType as _NewT,
    Self as _Self,
    Sequence as _Seq,
    TypedDict as _TDict,
    final as _fin,
)


@_fin
class _DataclassArguments(_TDict):
    init: _Lit[True]
    repr: _Lit[True]
    eq: _Lit[True]
    order: _Lit[False]
    unsafe_hash: _Lit[False]
    frozen: _Lit[True]
    match_args: _Lit[True]
    kw_only: _Lit[True]
    slots: _Lit[True]
    weakref_slot: _Lit[True]


_dc_args: _DataclassArguments = {
    "init": True,
    "repr": True,
    "eq": True,
    "order": False,
    "unsafe_hash": False,
    "frozen": True,
    "match_args": True,
    "kw_only": True,
    "slots": True,
    "weakref_slot": True,
}
Universe = _NewT("Universe", _Hreal)
ValueUniverse = Universe(_Hreal(0))
TypeUniverse = Universe(ValueUniverse + 1)
KindUniverse = Universe(TypeUniverse + 1)
MacroUniverse = Universe(ValueUniverse + _omega)


@_dc(**_dc_args)
@_fin
class AST:
    semantics: str
    children: _Seq[_Self] = []
    name: str | None = None

    def __post_init__(self):
        object.__setattr__(self, "children", tuple(self.children))


ASTLens = _Lens[AST, _Seq[tuple[int, str]]]

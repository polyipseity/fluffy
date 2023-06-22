# -*- coding: UTF-8 -*-
from .lens import Lens as _Lens
from dataclasses import dataclass as _dc
from infinitesimals import (  # pyright: ignore[reportMissingTypeStubs]
    HyperReal as _Hreal,
    omega as _omega,
)
from types import MappingProxyType as _MapPxy
from typing import (
    Literal as _Lit,
    Mapping as _Map,
    NewType as _NewT,
    Sequence as _Seq,
    TypedDict as _TDict,
    TypeVar as _TVar,
    cast as _cast,
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
class ASTModule:
    pass


_ExtendsASTModule = _TVar("_ExtendsASTModule", bound=ASTModule)


@_dc(**_dc_args)
@_fin
class AST:
    modules: _Map[type[ASTModule], ASTModule] = {}

    def __post_init__(self):
        object.__setattr__(self, "modules", _MapPxy(dict(self.modules)))

    def module(self, type: type[_ExtendsASTModule]) -> _ExtendsASTModule | None:
        return _cast(_ExtendsASTModule | None, self.modules.get(type, None))


@_fin
@_dc(**_dc_args)
class Named(ASTModule):
    name: str


@_fin
@_dc(**_dc_args)
class Scope(ASTModule):
    children: _Seq[AST]

    def __post_init__(self):
        object.__setattr__(self, "children", tuple(self.children))


@_fin
@_dc(**_dc_args)
class Parameterized(ASTModule):
    parameters: _Seq[AST]

    def __post_init__(self):
        object.__setattr__(self, "parameters", tuple(self.parameters))


ASTLens = _Lens[AST, _Seq[tuple[int, str]]]

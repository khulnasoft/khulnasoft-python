# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

__all__ = ["MigrationStepParam", "RenamedClass", "TransferredClass"]

_RenamedClassReservedKeywords = TypedDict(
    "_RenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class RenamedClass(_RenamedClassReservedKeywords, total=False):
    to: str


_TransferredClassReservedKeywords = TypedDict(
    "_TransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class TransferredClass(_TransferredClassReservedKeywords, total=False):
    from_script: str

    to: str


class MigrationStepParam(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Iterable[RenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[TransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .kind import Kind
from ..._utils import PropertyInfo

__all__ = ["AddressMapCreateParams", "Membership"]


class AddressMapCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    description: Optional[str]
    """
    An optional description field which may be used to describe the types of IPs or
    zones on the map.
    """

    enabled: Optional[bool]
    """Whether the Address Map is enabled or not.

    Khulnasoft's DNS will not respond with IP addresses on an Address Map until the
    map is enabled.
    """

    ips: List[str]

    memberships: Iterable[Membership]
    """Zones and Accounts which will be assigned IPs on this Address Map.

    A zone membership will take priority over an account membership.
    """


class Membership(TypedDict, total=False):
    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    identifier: str
    """The identifier for the membership (eg. a zone or account tag)."""

    kind: Kind
    """The type of the membership."""

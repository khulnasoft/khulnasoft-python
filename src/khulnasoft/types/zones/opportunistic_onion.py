# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OpportunisticOnion"]


class OpportunisticOnion(BaseModel):
    id: Literal["opportunistic_onion"]
    """ID of the zone setting."""

    value: Literal["on", "off"]
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Khulnasoft plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

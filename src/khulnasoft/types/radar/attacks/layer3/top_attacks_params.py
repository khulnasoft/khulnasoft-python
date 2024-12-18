# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TopAttacksParams"]


class TopAttacksParams(TypedDict, total=False):
    continent: List[str]
    """Array of comma separated list of continents (alpha-2 continent codes).

    Start with `-` to exclude from results. For example, `-EU,NA` excludes results
    from Europe, but includes results from North America.
    """

    date_end: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_range: Annotated[List[str], PropertyInfo(alias="dateRange")]
    """
    For example, use `7d` and `7dControl` to compare this week with the previous
    week. Use this parameter or set specific start and end dates (`dateStart` and
    `dateEnd` parameters).
    """

    date_start: Annotated[List[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Array of datetimes to filter the start of a series."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filter for ip version."""

    limit: int
    """Limit the number of objects in the response."""

    limit_direction: Annotated[Literal["ORIGIN", "TARGET"], PropertyInfo(alias="limitDirection")]
    """Array of attack origin/target location attack limits.

    Together with `limitPerLocation`, limits how many objects will be fetched per
    origin/target location.
    """

    limit_per_location: Annotated[int, PropertyInfo(alias="limitPerLocation")]
    """
    Limit the number of attacks per origin/target (refer to `limitDirection`
    parameter) location.
    """

    location: List[str]
    """Array of comma separated list of locations (alpha-2 country codes).

    Start with `-` to exclude from results. For example, `-US,PT` excludes results
    from the US, but includes results from PT.
    """

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    normalization: Literal["PERCENTAGE", "MIN_MAX"]
    """Normalization method applied.

    Refer to
    [Normalization methods](https://developers.khulnasoft.com/radar/concepts/normalization/).
    """

    protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]]
    """Array of L3/4 attack types."""

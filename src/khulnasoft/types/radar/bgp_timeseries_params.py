# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BGPTimeseriesParams", "Prefix"]


class BGPTimeseriesParams(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """
    Aggregation interval results should be returned in (for example, in 15 minutes
    or 1 hour intervals). Refer to
    [Aggregation intervals](https://developers.khulnasoft.com/radar/concepts/aggregation-intervals/).
    """

    asn: List[str]
    """Array of comma separated list of ASNs, start with `-` to exclude from results.

    For example, `-174, 3356` excludes results from AS174, but includes results from
    AS3356.
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

    name: List[str]
    """Array of names that will be used to name the series in responses."""

    prefix: Iterable[Prefix]
    """Array of BGP network prefixes."""

    update_type: Annotated[List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]], PropertyInfo(alias="updateType")]
    """Array of BGP update types."""


_PrefixReservedKeywords = TypedDict(
    "_PrefixReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class Prefix(_PrefixReservedKeywords, total=False):
    name: Required[str]

    test: Required[float]

    type: str
    """Network prefix, IPv4 or IPv6."""

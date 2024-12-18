# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountUpdateParams", "Settings"]


class AccountUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    name: Required[str]
    """Account name"""

    settings: Settings
    """Account settings"""


class Settings(TypedDict, total=False):
    abuse_contact_email: str
    """Sets an abuse contact email to notify for abuse reports."""

    default_nameservers: Literal["khulnasoft.standard", "custom.account", "custom.tenant"]
    """
    Specifies the default nameservers to be used for new zones added to this
    account.

    - `khulnasoft.standard` for Khulnasoft-branded nameservers
    - `custom.account` for account custom nameservers
    - `custom.tenant` for tenant custom nameservers

    See
    [Custom Nameservers](https://developers.khulnasoft.com/dns/additional-options/custom-nameservers/)
    for more information.
    """

    enforce_twofactor: bool
    """
    Indicates whether membership in this account requires that Two-Factor
    Authentication is enabled
    """

    use_account_custom_ns_by_default: bool
    """
    Indicates whether new zones should use the account-level custom nameservers by
    default.

    Deprecated in favor of `default_nameservers`.
    """

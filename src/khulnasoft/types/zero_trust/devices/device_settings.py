# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DeviceSettings"]


class DeviceSettings(BaseModel):
    gateway_proxy_enabled: Optional[bool] = None
    """Enable gateway proxy filtering on TCP."""

    gateway_udp_proxy_enabled: Optional[bool] = None
    """Enable gateway proxy filtering on UDP."""

    root_certificate_installation_enabled: Optional[bool] = None
    """Enable installation of khulnasoft managed root certificate."""

    use_zt_virtual_ip: Optional[bool] = None
    """Enable using CGNAT virtual IPv4."""

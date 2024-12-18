# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GatewayListResponse"]


class GatewayListResponse(BaseModel):
    id: Optional[str] = None
    """Khulnasoft account ID."""

    gateway_tag: Optional[str] = None
    """Gateway internal ID."""

    provider_name: Optional[str] = None
    """The name of the provider. Usually Khulnasoft."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.rate_plans import RatePlanGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRatePlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        rate_plan = client.rate_plans.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RatePlanGetResponse], rate_plan, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.rate_plans.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_plan = response.parse()
        assert_matches_type(Optional[RatePlanGetResponse], rate_plan, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.rate_plans.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_plan = response.parse()
            assert_matches_type(Optional[RatePlanGetResponse], rate_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.rate_plans.with_raw_response.get(
                "",
            )


class TestAsyncRatePlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        rate_plan = await async_client.rate_plans.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RatePlanGetResponse], rate_plan, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.rate_plans.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_plan = await response.parse()
        assert_matches_type(Optional[RatePlanGetResponse], rate_plan, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.rate_plans.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_plan = await response.parse()
            assert_matches_type(Optional[RatePlanGetResponse], rate_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.rate_plans.with_raw_response.get(
                "",
            )

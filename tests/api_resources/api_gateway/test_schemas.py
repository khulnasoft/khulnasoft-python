# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.api_gateway import SchemaListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        schema = client.api_gateway.schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        schema = client.api_gateway.schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
            host=["www.example.com"],
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.api_gateway.schemas.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.api_gateway.schemas.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.schemas.with_raw_response.list(
                zone_id="",
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        schema = await async_client.api_gateway.schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        schema = await async_client.api_gateway.schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
            host=["www.example.com"],
        )
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.api_gateway.schemas.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaListResponse, schema, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.api_gateway.schemas.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaListResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.schemas.with_raw_response.list(
                zone_id="",
            )

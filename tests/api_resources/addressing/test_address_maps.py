# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft._utils import parse_datetime
from khulnasoft.pagination import SyncSinglePage, AsyncSinglePage
from khulnasoft.types.addressing import (
    AddressMap,
    AddressMapGetResponse,
    AddressMapCreateResponse,
    AddressMapDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddressMaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="My Ecommerce zones",
            enabled=True,
            ips=["192.0.2.1", "192.0.2.1", "192.0.2.1"],
            memberships=[
                {
                    "created_at": parse_datetime("2014-01-01T05:20:00.12345Z"),
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                },
                {
                    "created_at": parse_datetime("2014-01-01T05:20:00.12345Z"),
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                },
                {
                    "created_at": parse_datetime("2014-01-01T05:20:00.12345Z"),
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                },
            ],
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.addressing.address_maps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.addressing.address_maps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.addressing.address_maps.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(SyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.addressing.address_maps.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(SyncSinglePage[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.delete(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.addressing.address_maps.with_raw_response.delete(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.addressing.address_maps.with_streaming_response.delete(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.delete(
                address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.with_raw_response.delete(
                address_map_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_sni="*.example.com",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Khulnasoft) -> None:
        response = client.addressing.address_maps.with_raw_response.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Khulnasoft) -> None:
        with client.addressing.address_maps.with_streaming_response.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.edit(
                address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.with_raw_response.edit(
                address_map_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        address_map = client.addressing.address_maps.get(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.addressing.address_maps.with_raw_response.get(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.addressing.address_maps.with_streaming_response.get(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.with_raw_response.get(
                address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.with_raw_response.get(
                address_map_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAddressMaps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="My Ecommerce zones",
            enabled=True,
            ips=["192.0.2.1", "192.0.2.1", "192.0.2.1"],
            memberships=[
                {
                    "created_at": parse_datetime("2014-01-01T05:20:00.12345Z"),
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                },
                {
                    "created_at": parse_datetime("2014-01-01T05:20:00.12345Z"),
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                },
                {
                    "created_at": parse_datetime("2014-01-01T05:20:00.12345Z"),
                    "identifier": "023e105f4ecef8ad9ca31a8372d0c353",
                    "kind": "zone",
                },
            ],
        )
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapCreateResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(AsyncSinglePage[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(AsyncSinglePage[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.delete(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.delete(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.delete(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.delete(
                address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.delete(
                address_map_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_sni="*.example.com",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMap], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.edit(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMap], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.edit(
                address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.edit(
                address_map_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        address_map = await async_client.addressing.address_maps.get(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.address_maps.with_raw_response.get(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.address_maps.with_streaming_response.get(
            address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapGetResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.get(
                address_map_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.with_raw_response.get(
                address_map_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncSinglePage, AsyncSinglePage
from khulnasoft.types.addressing.prefixes.bgp import ServiceBinding, BindingDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        binding = client.addressing.prefixes.bgp.bindings.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        binding = client.addressing.prefixes.bgp.bindings.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            service_id="2db684ee7ca04e159946fd05b99e1bcd",
        )
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.addressing.prefixes.bgp.bindings.with_raw_response.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.addressing.prefixes.bgp.bindings.with_streaming_response.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.create(
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.create(
                prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        binding = client.addressing.prefixes.bgp.bindings.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.addressing.prefixes.bgp.bindings.with_raw_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(SyncSinglePage[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.addressing.prefixes.bgp.bindings.with_streaming_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(SyncSinglePage[ServiceBinding], binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.list(
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.list(
                prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        binding = client.addressing.prefixes.bgp.bindings.delete(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.addressing.prefixes.bgp.bindings.with_streaming_response.delete(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(BindingDeleteResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        binding = client.addressing.prefixes.bgp.bindings.get(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.addressing.prefixes.bgp.bindings.with_raw_response.get(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.addressing.prefixes.bgp.bindings.with_streaming_response.get(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.get(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.get(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.addressing.prefixes.bgp.bindings.with_raw_response.get(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBindings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        binding = await async_client.addressing.prefixes.bgp.bindings.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        binding = await async_client.addressing.prefixes.bgp.bindings.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            service_id="2db684ee7ca04e159946fd05b99e1bcd",
        )
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.prefixes.bgp.bindings.with_raw_response.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.prefixes.bgp.bindings.with_streaming_response.create(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.create(
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.create(
                prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        binding = await async_client.addressing.prefixes.bgp.bindings.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.prefixes.bgp.bindings.with_raw_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(AsyncSinglePage[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.prefixes.bgp.bindings.with_streaming_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(AsyncSinglePage[ServiceBinding], binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.list(
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.list(
                prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        binding = await async_client.addressing.prefixes.bgp.bindings.delete(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.prefixes.bgp.bindings.with_streaming_response.delete(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(BindingDeleteResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.delete(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        binding = await async_client.addressing.prefixes.bgp.bindings.get(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.prefixes.bgp.bindings.with_raw_response.get(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.prefixes.bgp.bindings.with_streaming_response.get(
            binding_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(Optional[ServiceBinding], binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.get(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.get(
                binding_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.addressing.prefixes.bgp.bindings.with_raw_response.get(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

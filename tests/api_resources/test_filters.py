# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from khulnasoft.types.filters import (
    FirewallFilter,
    FilterCreateResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(Optional[FilterCreateResponse], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterCreateResponse], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(Optional[FilterCreateResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.filters.with_raw_response.create(
                    zone_identifier="",
                    body={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.update(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.filters.with_raw_response.update(
                    id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_identifier="",
                    body={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.filters.with_raw_response.update(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                    body={},
                )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b61",
                description="browsers",
                expression="php",
                page=1,
                paused=False,
                per_page=5,
                ref="FIL-100",
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(SyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.filters.with_raw_response.list(
                    zone_identifier="",
                )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.delete(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.filters.with_raw_response.delete(
                    id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.filters.with_raw_response.delete(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = client.filters.get(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.filters.with_raw_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with client.filters.with_streaming_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.filters.with_raw_response.get(
                    id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.filters.with_raw_response.get(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )


class TestAsyncFilters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(Optional[FilterCreateResponse], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterCreateResponse], filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(Optional[FilterCreateResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.filters.with_raw_response.create(
                    zone_identifier="",
                    body={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.update(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.filters.with_raw_response.update(
                    id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_identifier="",
                    body={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.filters.with_raw_response.update(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                    body={},
                )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b61",
                description="browsers",
                expression="php",
                page=1,
                paused=False,
                per_page=5,
                ref="FIL-100",
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(AsyncV4PagePaginationArray[FirewallFilter], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.filters.with_raw_response.list(
                    zone_identifier="",
                )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.delete(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.filters.with_raw_response.delete(
                    id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.filters.with_raw_response.delete(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            filter = await async_client.filters.get(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.filters.with_raw_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FirewallFilter, filter, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.filters.with_streaming_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b61",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                filter = await response.parse()
                assert_matches_type(FirewallFilter, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.filters.with_raw_response.get(
                    id="372e67954025e0ba6aaa6d586b9e0b61",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.filters.with_raw_response.get(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )

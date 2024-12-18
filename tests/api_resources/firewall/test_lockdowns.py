# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft._utils import parse_datetime
from khulnasoft.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from khulnasoft.types.firewall import (
    Lockdown,
    LockdownDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockdowns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        lockdown = client.firewall.lockdowns.create(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.firewall.lockdowns.with_raw_response.create(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.firewall.lockdowns.with_streaming_response.create(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.lockdowns.with_raw_response.create(
                zone_identifier="",
                body={},
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        lockdown = client.firewall.lockdowns.update(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.firewall.lockdowns.with_raw_response.update(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.firewall.lockdowns.with_streaming_response.update(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.lockdowns.with_raw_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewall.lockdowns.with_raw_response.update(
                id="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        lockdown = client.firewall.lockdowns.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        lockdown = client.firewall.lockdowns.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            created_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            description="endpoints",
            description_search="endpoints",
            ip="1.2.3.4",
            ip_range_search="1.2.3.0/16",
            ip_search="1.2.3.4",
            modified_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            page=1,
            per_page=1,
            priority=5,
            uri_search="/some/path",
        )
        assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.firewall.lockdowns.with_raw_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.firewall.lockdowns.with_streaming_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.lockdowns.with_raw_response.list(
                zone_identifier="",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        lockdown = client.firewall.lockdowns.delete(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.firewall.lockdowns.with_raw_response.delete(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.firewall.lockdowns.with_streaming_response.delete(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.lockdowns.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewall.lockdowns.with_raw_response.delete(
                id="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        lockdown = client.firewall.lockdowns.get(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.firewall.lockdowns.with_raw_response.get(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.firewall.lockdowns.with_streaming_response.get(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.lockdowns.with_raw_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewall.lockdowns.with_raw_response.get(
                id="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLockdowns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        lockdown = await async_client.firewall.lockdowns.create(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.create(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.create(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.create(
                zone_identifier="",
                body={},
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        lockdown = await async_client.firewall.lockdowns.update(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.update(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.update(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.update(
                id="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        lockdown = await async_client.firewall.lockdowns.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        lockdown = await async_client.firewall.lockdowns.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            created_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            description="endpoints",
            description_search="endpoints",
            ip="1.2.3.4",
            ip_range_search="1.2.3.0/16",
            ip_search="1.2.3.4",
            modified_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            page=1,
            per_page=1,
            priority=5,
            uri_search="/some/path",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.list(
                zone_identifier="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        lockdown = await async_client.firewall.lockdowns.delete(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.delete(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.delete(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.delete(
                id="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        lockdown = await async_client.firewall.lockdowns.get(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.get(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.get(
            id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.get(
                id="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

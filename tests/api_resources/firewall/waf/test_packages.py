# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from khulnasoft.types.firewall.waf import PackageGetResponse, PackageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPackages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        package = client.firewall.waf.packages.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        package = client.firewall.waf.packages.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            match="any",
            name="USER",
            order="name",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.firewall.waf.packages.with_raw_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.firewall.waf.packages.with_streaming_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.waf.packages.with_raw_response.list(
                zone_identifier="",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        package = client.firewall.waf.packages.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PackageGetResponse, package, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.firewall.waf.packages.with_raw_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(PackageGetResponse, package, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.firewall.waf.packages.with_streaming_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(PackageGetResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewall.waf.packages.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.firewall.waf.packages.with_raw_response.get(
                identifier="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPackages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        package = await async_client.firewall.waf.packages.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        package = await async_client.firewall.waf.packages.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            match="any",
            name="USER",
            order="name",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.waf.packages.with_raw_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.waf.packages.with_streaming_response.list(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[PackageListResponse], package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.waf.packages.with_raw_response.list(
                zone_identifier="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        package = await async_client.firewall.waf.packages.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PackageGetResponse, package, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.waf.packages.with_raw_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(PackageGetResponse, package, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.waf.packages.with_streaming_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(PackageGetResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewall.waf.packages.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.firewall.waf.packages.with_raw_response.get(
                identifier="",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncV4PagePagination, AsyncV4PagePagination
from khulnasoft.types.zero_trust.dex import TestListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        test = client.zero_trust.dex.tests.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(SyncV4PagePagination[TestListResponse], test, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        test = client.zero_trust.dex.tests.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            colo="colo",
            device_id=["string", "string", "string"],
            page=1,
            per_page=1,
            test_name="testName",
        )
        assert_matches_type(SyncV4PagePagination[TestListResponse], test, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.zero_trust.dex.tests.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SyncV4PagePagination[TestListResponse], test, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.zero_trust.dex.tests.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SyncV4PagePagination[TestListResponse], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.tests.with_raw_response.list(
                account_id="",
            )


class TestAsyncTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        test = await async_client.zero_trust.dex.tests.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(AsyncV4PagePagination[TestListResponse], test, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        test = await async_client.zero_trust.dex.tests.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            colo="colo",
            device_id=["string", "string", "string"],
            page=1,
            per_page=1,
            test_name="testName",
        )
        assert_matches_type(AsyncV4PagePagination[TestListResponse], test, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.zero_trust.dex.tests.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(AsyncV4PagePagination[TestListResponse], test, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.zero_trust.dex.tests.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(AsyncV4PagePagination[TestListResponse], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.tests.with_raw_response.list(
                account_id="",
            )

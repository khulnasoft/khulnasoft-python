# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncSinglePage, AsyncSinglePage
from khulnasoft.types.calls import (
    CallsApp,
    CallListResponse,
    CallsAppWithSecret,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        call = client.calls.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        call = client.calls.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.calls.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.calls.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        call = client.calls.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Khulnasoft) -> None:
        call = client.calls.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.calls.with_raw_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.calls.with_streaming_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(Optional[CallsApp], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.with_raw_response.update(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.calls.with_raw_response.update(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        call = client.calls.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[CallListResponse], call, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.calls.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(SyncSinglePage[CallListResponse], call, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.calls.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(SyncSinglePage[CallListResponse], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        call = client.calls.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.calls.with_raw_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.calls.with_streaming_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(Optional[CallsApp], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.with_raw_response.delete(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.calls.with_raw_response.delete(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        call = client.calls.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.calls.with_raw_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.calls.with_streaming_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(Optional[CallsApp], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.calls.with_raw_response.get(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.calls.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.calls.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.calls.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(Optional[CallsAppWithSecret], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="production-realtime-app",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.calls.with_raw_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.calls.with_streaming_response.update(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(Optional[CallsApp], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.with_raw_response.update(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.calls.with_raw_response.update(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[CallListResponse], call, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.calls.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(AsyncSinglePage[CallListResponse], call, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.calls.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(AsyncSinglePage[CallListResponse], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.calls.with_raw_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.calls.with_streaming_response.delete(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(Optional[CallsApp], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.with_raw_response.delete(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.calls.with_raw_response.delete(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        call = await async_client.calls.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.calls.with_raw_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(Optional[CallsApp], call, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.calls.with_streaming_response.get(
            app_id="2a95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(Optional[CallsApp], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.calls.with_raw_response.get(
                app_id="2a95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.calls.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

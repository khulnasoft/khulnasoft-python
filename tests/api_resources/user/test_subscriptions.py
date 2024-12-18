# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.user import (
    SubscriptionGetResponse,
    SubscriptionEditResponse,
    SubscriptionDeleteResponse,
    SubscriptionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        subscription = client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Khulnasoft) -> None:
        subscription = client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "install_id"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.user.subscriptions.with_raw_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.user.subscriptions.with_streaming_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.user.subscriptions.with_raw_response.update(
                identifier="",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        subscription = client.user.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.user.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.user.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.user.subscriptions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_edit(self, client: Khulnasoft) -> None:
        subscription = client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Khulnasoft) -> None:
        subscription = client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "install_id"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Khulnasoft) -> None:
        response = client.user.subscriptions.with_raw_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Khulnasoft) -> None:
        with client.user.subscriptions.with_streaming_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.user.subscriptions.with_raw_response.edit(
                identifier="",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        subscription = client.user.subscriptions.get()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.user.subscriptions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.user.subscriptions.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        subscription = await async_client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        subscription = await async_client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "install_id"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.user.subscriptions.with_raw_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.user.subscriptions.with_streaming_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.user.subscriptions.with_raw_response.update(
                identifier="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        subscription = await async_client.user.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.user.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.user.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.user.subscriptions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncKhulnasoft) -> None:
        subscription = await async_client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        subscription = await async_client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "install_id"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.user.subscriptions.with_raw_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.user.subscriptions.with_streaming_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionEditResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.user.subscriptions.with_raw_response.edit(
                identifier="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        subscription = await async_client.user.subscriptions.get()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.user.subscriptions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.user.subscriptions.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

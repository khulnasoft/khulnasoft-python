# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from khulnasoft.types.firewall import (
    AccessRuleGetResponse,
    AccessRuleEditResponse,
    AccessRuleCreateResponse,
    AccessRuleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.create(
            configuration={},
            mode="challenge",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="challenge",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="challenge",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="challenge",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="challenge",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.list(
            account_id="account_id",
            direction="desc",
            egs_pagination={
                "json": {
                    "page": 1,
                    "per_page": 1,
                }
            },
            filters={
                "configuration_target": "ip",
                "configuration_value": "198.51.100.4",
                "match": "any",
                "mode": "challenge",
                "notes": "my note",
            },
            order="mode",
            page=1,
            per_page=20,
        )
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.firewall.access_rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.firewall.access_rules.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.delete(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.delete(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.firewall.access_rules.with_raw_response.delete(
            identifier={},
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.firewall.access_rules.with_streaming_response.delete(
            identifier={},
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.delete(
                identifier={},
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.delete(
                identifier={},
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.edit(
            identifier={},
            configuration={},
            mode="challenge",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.edit(
            identifier={},
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Khulnasoft) -> None:
        response = client.firewall.access_rules.with_raw_response.edit(
            identifier={},
            configuration={},
            mode="challenge",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Khulnasoft) -> None:
        with client.firewall.access_rules.with_streaming_response.edit(
            identifier={},
            configuration={},
            mode="challenge",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.edit(
                identifier={},
                configuration={},
                mode="challenge",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.edit(
                identifier={},
                configuration={},
                mode="challenge",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.get(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Khulnasoft) -> None:
        access_rule = client.firewall.access_rules.get(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.firewall.access_rules.with_raw_response.get(
            identifier={},
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.firewall.access_rules.with_streaming_response.get(
            identifier={},
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.firewall.access_rules.with_raw_response.get(
                identifier={},
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.access_rules.with_raw_response.get(
                identifier={},
                account_id="account_id",
            )


class TestAsyncAccessRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.create(
            configuration={},
            mode="challenge",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="challenge",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="challenge",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AccessRuleCreateResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="challenge",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.create(
                configuration={},
                mode="challenge",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.list(
            account_id="account_id",
            direction="desc",
            egs_pagination={
                "json": {
                    "page": 1,
                    "per_page": 1,
                }
            },
            filters={
                "configuration_target": "ip",
                "configuration_value": "198.51.100.4",
                "match": "any",
                "mode": "challenge",
                "notes": "my note",
            },
            order="mode",
            page=1,
            per_page=20,
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.delete(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.delete(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.delete(
            identifier={},
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.delete(
            identifier={},
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.delete(
                identifier={},
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.delete(
                identifier={},
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.edit(
            identifier={},
            configuration={},
            mode="challenge",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.edit(
            identifier={},
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.edit(
            identifier={},
            configuration={},
            mode="challenge",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.edit(
            identifier={},
            configuration={},
            mode="challenge",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AccessRuleEditResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.edit(
                identifier={},
                configuration={},
                mode="challenge",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.edit(
                identifier={},
                configuration={},
                mode="challenge",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.get(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        access_rule = await async_client.firewall.access_rules.get(
            identifier={},
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.firewall.access_rules.with_raw_response.get(
            identifier={},
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.get(
            identifier={},
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(AccessRuleGetResponse, access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.get(
                identifier={},
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.access_rules.with_raw_response.get(
                identifier={},
                account_id="account_id",
            )

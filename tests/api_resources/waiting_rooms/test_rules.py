# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncSinglePage, AsyncSinglePage
from khulnasoft.types.waiting_rooms import (
    WaitingRoomRule,
    RuleEditResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.waiting_rooms.rules.with_raw_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.waiting_rooms.rules.with_streaming_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.create(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.create(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.waiting_rooms.rules.with_raw_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.waiting_rooms.rules.with_streaming_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.update(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                body=[
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.update(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                ],
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[WaitingRoomRule], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.waiting_rooms.rules.with_raw_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[WaitingRoomRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.waiting_rooms.rules.with_streaming_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncSinglePage[WaitingRoomRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.list(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.list(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.delete(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.waiting_rooms.rules.with_raw_response.delete(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.waiting_rooms.rules.with_streaming_response.delete(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Khulnasoft) -> None:
        rule = client.waiting_rooms.rules.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
            position={"index": 0},
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Khulnasoft) -> None:
        response = client.waiting_rooms.rules.with_raw_response.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Khulnasoft) -> None:
        with client.waiting_rooms.rules.with_streaming_response.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.edit(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.edit(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.edit(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.create(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.create(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.update(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.update(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                body=[
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.update(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[WaitingRoomRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[WaitingRoomRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncSinglePage[WaitingRoomRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.list(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.list(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.delete(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.delete(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.delete(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        rule = await async_client.waiting_rooms.rules.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
            position={"index": 0},
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.edit(
            rule_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.edit(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.edit(
                rule_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.edit(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

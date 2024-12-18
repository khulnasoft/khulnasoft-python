# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.rulesets import PhaseGetResponse, PhaseUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        phase = client.rulesets.phases.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="account_id",
        )
        assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Khulnasoft) -> None:
        phase = client.rulesets.phases.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
            ],
            account_id="account_id",
            description="My ruleset to execute managed rulesets",
            name="My ruleset",
        )
        assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.rulesets.phases.with_raw_response.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phase = response.parse()
        assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.rulesets.phases.with_streaming_response.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phase = response.parse()
            assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.phases.with_raw_response.update(
                ruleset_phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.phases.with_raw_response.update(
                ruleset_phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        phase = client.rulesets.phases.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        )
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Khulnasoft) -> None:
        phase = client.rulesets.phases.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        )
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.rulesets.phases.with_raw_response.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phase = response.parse()
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.rulesets.phases.with_streaming_response.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phase = response.parse()
            assert_matches_type(PhaseGetResponse, phase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.phases.with_raw_response.get(
                ruleset_phase="http_request_firewall_custom",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.phases.with_raw_response.get(
                ruleset_phase="http_request_firewall_custom",
                account_id="account_id",
            )


class TestAsyncPhases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        phase = await async_client.rulesets.phases.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="account_id",
        )
        assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        phase = await async_client.rulesets.phases.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
            ],
            account_id="account_id",
            description="My ruleset to execute managed rulesets",
            name="My ruleset",
        )
        assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.rulesets.phases.with_raw_response.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phase = await response.parse()
        assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.rulesets.phases.with_streaming_response.update(
            ruleset_phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phase = await response.parse()
            assert_matches_type(PhaseUpdateResponse, phase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.phases.with_raw_response.update(
                ruleset_phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.phases.with_raw_response.update(
                ruleset_phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        phase = await async_client.rulesets.phases.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        )
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        phase = await async_client.rulesets.phases.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        )
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.rulesets.phases.with_raw_response.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phase = await response.parse()
        assert_matches_type(PhaseGetResponse, phase, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.rulesets.phases.with_streaming_response.get(
            ruleset_phase="http_request_firewall_custom",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phase = await response.parse()
            assert_matches_type(PhaseGetResponse, phase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.phases.with_raw_response.get(
                ruleset_phase="http_request_firewall_custom",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.phases.with_raw_response.get(
                ruleset_phase="http_request_firewall_custom",
                account_id="account_id",
            )

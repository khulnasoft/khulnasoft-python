# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.email_routing.rules import CatchAllGetResponse, CatchAllUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatchAlls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        catch_all = client.email_routing.rules.catch_alls.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Khulnasoft) -> None:
        catch_all = client.email_routing.rules.catch_alls.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            enabled=True,
            name="Send to user@example.net rule.",
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.email_routing.rules.catch_alls.with_raw_response.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = response.parse()
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.email_routing.rules.catch_alls.with_streaming_response.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = response.parse()
            assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.email_routing.rules.catch_alls.with_raw_response.update(
                zone_identifier="",
                actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        catch_all = client.email_routing.rules.catch_alls.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.email_routing.rules.catch_alls.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = response.parse()
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.email_routing.rules.catch_alls.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = response.parse()
            assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.email_routing.rules.catch_alls.with_raw_response.get(
                "",
            )


class TestAsyncCatchAlls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        catch_all = await async_client.email_routing.rules.catch_alls.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        catch_all = await async_client.email_routing.rules.catch_alls.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            enabled=True,
            name="Send to user@example.net rule.",
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.email_routing.rules.catch_alls.with_raw_response.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = await response.parse()
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.email_routing.rules.catch_alls.with_streaming_response.update(
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = await response.parse()
            assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.email_routing.rules.catch_alls.with_raw_response.update(
                zone_identifier="",
                actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        catch_all = await async_client.email_routing.rules.catch_alls.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.email_routing.rules.catch_alls.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = await response.parse()
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.email_routing.rules.catch_alls.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = await response.parse()
            assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.email_routing.rules.catch_alls.with_raw_response.get(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.zero_trust import RiskScoringGetResponse, RiskScoringResetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRiskScoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        risk_scoring = client.zero_trust.risk_scoring.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Khulnasoft) -> None:
        risk_scoring = client.zero_trust.risk_scoring.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            order_by="timestamp",
            page=0,
            per_page=0,
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.zero_trust.risk_scoring.with_raw_response.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = response.parse()
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.zero_trust.risk_scoring.with_streaming_response.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = response.parse()
            assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_reset(self, client: Khulnasoft) -> None:
        risk_scoring = client.zero_trust.risk_scoring.reset(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: Khulnasoft) -> None:
        response = client.zero_trust.risk_scoring.with_raw_response.reset(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = response.parse()
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: Khulnasoft) -> None:
        with client.zero_trust.risk_scoring.with_streaming_response.reset(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = response.parse()
            assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRiskScoring:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            order_by="timestamp",
            page=0,
            per_page=0,
        )
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.zero_trust.risk_scoring.with_raw_response.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = await response.parse()
        assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.zero_trust.risk_scoring.with_streaming_response.get(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = await response.parse()
            assert_matches_type(RiskScoringGetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.get(
                user_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncKhulnasoft) -> None:
        risk_scoring = await async_client.zero_trust.risk_scoring.reset(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.zero_trust.risk_scoring.with_raw_response.reset(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        risk_scoring = await response.parse()
        assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.zero_trust.risk_scoring.with_streaming_response.reset(
            user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            risk_scoring = await response.parse()
            assert_matches_type(RiskScoringResetResponse, risk_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="f2108713-1206-4e84-8b80-0e71a6a1c67b",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.risk_scoring.with_raw_response.reset(
                user_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

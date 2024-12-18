# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.zero_trust.dlp import PayloadLogGetResponse, PayloadLogUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayloadLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Khulnasoft) -> None:
        payload_log = client.zero_trust.dlp.payload_logs.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )
        assert_matches_type(PayloadLogUpdateResponse, payload_log, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Khulnasoft) -> None:
        response = client.zero_trust.dlp.payload_logs.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = response.parse()
        assert_matches_type(PayloadLogUpdateResponse, payload_log, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Khulnasoft) -> None:
        with client.zero_trust.dlp.payload_logs.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = response.parse()
            assert_matches_type(PayloadLogUpdateResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.payload_logs.with_raw_response.update(
                account_id="",
                public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        payload_log = client.zero_trust.dlp.payload_logs.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PayloadLogGetResponse, payload_log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.zero_trust.dlp.payload_logs.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = response.parse()
        assert_matches_type(PayloadLogGetResponse, payload_log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.zero_trust.dlp.payload_logs.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = response.parse()
            assert_matches_type(PayloadLogGetResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.payload_logs.with_raw_response.get(
                account_id="",
            )


class TestAsyncPayloadLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncKhulnasoft) -> None:
        payload_log = await async_client.zero_trust.dlp.payload_logs.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )
        assert_matches_type(PayloadLogUpdateResponse, payload_log, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.zero_trust.dlp.payload_logs.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = await response.parse()
        assert_matches_type(PayloadLogUpdateResponse, payload_log, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.zero_trust.dlp.payload_logs.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = await response.parse()
            assert_matches_type(PayloadLogUpdateResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.payload_logs.with_raw_response.update(
                account_id="",
                public_key="EmpOvSXw8BfbrGCi0fhGiD/3yXk2SiV1Nzg2lru3oj0=",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        payload_log = await async_client.zero_trust.dlp.payload_logs.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PayloadLogGetResponse, payload_log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.zero_trust.dlp.payload_logs.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload_log = await response.parse()
        assert_matches_type(PayloadLogGetResponse, payload_log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.zero_trust.dlp.payload_logs.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload_log = await response.parse()
            assert_matches_type(PayloadLogGetResponse, payload_log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.payload_logs.with_raw_response.get(
                account_id="",
            )

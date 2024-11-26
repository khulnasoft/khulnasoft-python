# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.logpush import (
    ValidateOriginResponse,
    ValidateDestinationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_destination(self, client: Khulnasoft) -> None:
        validate = client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_destination_with_all_params(self, client: Khulnasoft) -> None:
        validate = client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_destination(self, client: Khulnasoft) -> None:
        response = client.logpush.validate.with_raw_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_destination(self, client: Khulnasoft) -> None:
        with client.logpush.validate.with_streaming_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_destination(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_origin(self, client: Khulnasoft) -> None:
        validate = client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_origin_with_all_params(self, client: Khulnasoft) -> None:
        validate = client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_origin(self, client: Khulnasoft) -> None:
        response = client.logpush.validate.with_raw_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_origin(self, client: Khulnasoft) -> None:
        with client.logpush.validate.with_streaming_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_origin(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="account_id",
            )


class TestAsyncValidate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_destination(self, async_client: AsyncKhulnasoft) -> None:
        validate = await async_client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_destination_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        validate = await async_client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_destination(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.logpush.validate.with_raw_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_destination(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.logpush.validate.with_streaming_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_destination(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_origin(self, async_client: AsyncKhulnasoft) -> None:
        validate = await async_client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_origin_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        validate = await async_client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_origin(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.logpush.validate.with_raw_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_origin(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.logpush.validate.with_streaming_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_origin(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="account_id",
            )

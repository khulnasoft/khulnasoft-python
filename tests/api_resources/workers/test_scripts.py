# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import httpx
import pytest
from respx import MockRouter

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from khulnasoft.pagination import SyncSinglePage, AsyncSinglePage
from khulnasoft.types.workers import Script

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScripts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_1(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            rollback_to="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "text": "my_data",
                        "type": "plain_text",
                    }
                ],
                "body_part": "worker.js",
                "compatibility_date": "2023-07-25",
                "compatibility_flags": ["string", "string", "string"],
                "keep_bindings": ["string", "string", "string"],
                "logpush": False,
                "main_module": "worker.js",
                "migrations": {
                    "new_tag": "v2",
                    "old_tag": "v1",
                    "deleted_classes": ["string", "string", "string"],
                    "new_classes": ["string", "string", "string"],
                    "renamed_classes": [
                        {
                            "from": "from",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "to": "to",
                        },
                    ],
                    "transferred_classes": [
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        },
                    ],
                },
                "placement": {"mode": "smart"},
                "tags": ["string", "string", "string"],
                "tail_consumers": [
                    {
                        "environment": "production",
                        "namespace": "my-namespace",
                        "service": "my-log-consumer",
                    },
                    {
                        "environment": "production",
                        "namespace": "my-namespace",
                        "service": "my-log-consumer",
                    },
                    {
                        "environment": "production",
                        "namespace": "my-namespace",
                        "service": "my-log-consumer",
                    },
                ],
                "usage_model": "bundled",
                "version_tags": {},
            },
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Khulnasoft) -> None:
        response = client.workers.scripts.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Khulnasoft) -> None:
        with client.workers.scripts.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(Optional[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_1(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.with_raw_response.update(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_2(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            rollback_to="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            message="message",
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Khulnasoft) -> None:
        response = client.workers.scripts.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Khulnasoft) -> None:
        with client.workers.scripts.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(Optional[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_2(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.with_raw_response.update(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Script], script, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.workers.scripts.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(SyncSinglePage[Script], script, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.workers.scripts.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(SyncSinglePage[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert script is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Khulnasoft) -> None:
        script = client.workers.scripts.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            force=True,
        )
        assert script is None

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.workers.scripts.with_raw_response.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert script is None

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.workers.scripts.with_streaming_response.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert script is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.with_raw_response.delete(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.with_raw_response.delete(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        script = client.workers.scripts.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert script.is_closed
        assert script.json() == {"foo": "bar"}
        assert cast(Any, script.is_closed) is True
        assert isinstance(script, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        script = client.workers.scripts.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert script.is_closed is True
        assert script.http_request.headers.get("X-Stainless-Lang") == "python"
        assert script.json() == {"foo": "bar"}
        assert isinstance(script, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.workers.scripts.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as script:
            assert not script.is_closed
            assert script.http_request.headers.get("X-Stainless-Lang") == "python"

            assert script.json() == {"foo": "bar"}
            assert cast(Any, script.is_closed) is True
            assert isinstance(script, StreamedBinaryAPIResponse)

        assert cast(Any, script.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncScripts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            rollback_to="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "text": "my_data",
                        "type": "plain_text",
                    }
                ],
                "body_part": "worker.js",
                "compatibility_date": "2023-07-25",
                "compatibility_flags": ["string", "string", "string"],
                "keep_bindings": ["string", "string", "string"],
                "logpush": False,
                "main_module": "worker.js",
                "migrations": {
                    "new_tag": "v2",
                    "old_tag": "v1",
                    "deleted_classes": ["string", "string", "string"],
                    "new_classes": ["string", "string", "string"],
                    "renamed_classes": [
                        {
                            "from": "from",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "to": "to",
                        },
                    ],
                    "transferred_classes": [
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        },
                        {
                            "from": "from",
                            "from_script": "from_script",
                            "to": "to",
                        },
                    ],
                },
                "placement": {"mode": "smart"},
                "tags": ["string", "string", "string"],
                "tail_consumers": [
                    {
                        "environment": "production",
                        "namespace": "my-namespace",
                        "service": "my-log-consumer",
                    },
                    {
                        "environment": "production",
                        "namespace": "my-namespace",
                        "service": "my-log-consumer",
                    },
                    {
                        "environment": "production",
                        "namespace": "my-namespace",
                        "service": "my-log-consumer",
                    },
                ],
                "usage_model": "bundled",
                "version_tags": {},
            },
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.workers.scripts.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.workers.scripts.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(Optional[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.with_raw_response.update(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            rollback_to="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            message="message",
        )
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.workers.scripts.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(Optional[Script], script, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.workers.scripts.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(Optional[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.with_raw_response.update(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.workers.scripts.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.workers.scripts.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert script is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        script = await async_client.workers.scripts.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            force=True,
        )
        assert script is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.workers.scripts.with_raw_response.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert script is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.workers.scripts.with_streaming_response.delete(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert script is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.with_raw_response.delete(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.with_raw_response.delete(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncKhulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        script = await async_client.workers.scripts.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert script.is_closed
        assert await script.json() == {"foo": "bar"}
        assert cast(Any, script.is_closed) is True
        assert isinstance(script, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        script = await async_client.workers.scripts.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert script.is_closed is True
        assert script.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await script.json() == {"foo": "bar"}
        assert isinstance(script, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.workers.scripts.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as script:
            assert not script.is_closed
            assert script.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await script.json() == {"foo": "bar"}
            assert cast(Any, script.is_closed) is True
            assert isinstance(script, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, script.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

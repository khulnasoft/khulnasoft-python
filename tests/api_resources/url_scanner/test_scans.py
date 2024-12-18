# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

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
from khulnasoft.types.url_scanner import (
    ScanGetResponse,
    ScanHarResponse,
    ScanCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        scan = client.url_scanner.scans.create(
            account_id="accountId",
            url="https://www.example.com",
        )
        assert_matches_type(ScanCreateResponse, scan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        scan = client.url_scanner.scans.create(
            account_id="accountId",
            url="https://www.example.com",
            custom_headers={"foo": "string"},
            screenshots_resolutions=["desktop", "mobile", "tablet"],
            visibility="Public",
        )
        assert_matches_type(ScanCreateResponse, scan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.url_scanner.scans.with_raw_response.create(
            account_id="accountId",
            url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanCreateResponse, scan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.url_scanner.scans.with_streaming_response.create(
            account_id="accountId",
            url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanCreateResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.create(
                account_id="",
                url="https://www.example.com",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        scan = client.url_scanner.scans.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Khulnasoft) -> None:
        scan = client.url_scanner.scans.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
            full=True,
        )
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.url_scanner.scans.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.url_scanner.scans.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanGetResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.get(
                scan_id="",
                account_id="accountId",
            )

    @parametrize
    def test_method_har(self, client: Khulnasoft) -> None:
        scan = client.url_scanner.scans.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert_matches_type(ScanHarResponse, scan, path=["response"])

    @parametrize
    def test_raw_response_har(self, client: Khulnasoft) -> None:
        response = client.url_scanner.scans.with_raw_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanHarResponse, scan, path=["response"])

    @parametrize
    def test_streaming_response_har(self, client: Khulnasoft) -> None:
        with client.url_scanner.scans.with_streaming_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanHarResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_har(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.har(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.har(
                scan_id="",
                account_id="accountId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert scan.is_closed
        assert scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot_with_all_params(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
            resolution="desktop",
        )
        assert scan.is_closed
        assert scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_screenshot(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scan = client.url_scanner.scans.with_raw_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert scan.is_closed is True
        assert scan.http_request.headers.get("X-Stainless-Lang") == "python"
        assert scan.json() == {"foo": "bar"}
        assert isinstance(scan, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_screenshot(self, client: Khulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.url_scanner.scans.with_streaming_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as scan:
            assert not scan.is_closed
            assert scan.http_request.headers.get("X-Stainless-Lang") == "python"

            assert scan.json() == {"foo": "bar"}
            assert cast(Any, scan.is_closed) is True
            assert isinstance(scan, StreamedBinaryAPIResponse)

        assert cast(Any, scan.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_screenshot(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="",
                account_id="accountId",
            )


class TestAsyncScans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        scan = await async_client.url_scanner.scans.create(
            account_id="accountId",
            url="https://www.example.com",
        )
        assert_matches_type(ScanCreateResponse, scan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        scan = await async_client.url_scanner.scans.create(
            account_id="accountId",
            url="https://www.example.com",
            custom_headers={"foo": "string"},
            screenshots_resolutions=["desktop", "mobile", "tablet"],
            visibility="Public",
        )
        assert_matches_type(ScanCreateResponse, scan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.create(
            account_id="accountId",
            url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanCreateResponse, scan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.create(
            account_id="accountId",
            url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanCreateResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.create(
                account_id="",
                url="https://www.example.com",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        scan = await async_client.url_scanner.scans.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        scan = await async_client.url_scanner.scans.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
            full=True,
        )
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanGetResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.get(
                scan_id="",
                account_id="accountId",
            )

    @parametrize
    async def test_method_har(self, async_client: AsyncKhulnasoft) -> None:
        scan = await async_client.url_scanner.scans.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert_matches_type(ScanHarResponse, scan, path=["response"])

    @parametrize
    async def test_raw_response_har(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanHarResponse, scan, path=["response"])

    @parametrize
    async def test_streaming_response_har(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanHarResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_har(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.har(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.har(
                scan_id="",
                account_id="accountId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot(self, async_client: AsyncKhulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = await async_client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert scan.is_closed
        assert await scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot_with_all_params(
        self, async_client: AsyncKhulnasoft, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = await async_client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
            resolution="desktop",
        )
        assert scan.is_closed
        assert await scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_screenshot(self, async_client: AsyncKhulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scan = await async_client.url_scanner.scans.with_raw_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert scan.is_closed is True
        assert scan.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await scan.json() == {"foo": "bar"}
        assert isinstance(scan, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_screenshot(self, async_client: AsyncKhulnasoft, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/scan/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/screenshot").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.url_scanner.scans.with_streaming_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as scan:
            assert not scan.is_closed
            assert scan.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await scan.json() == {"foo": "bar"}
            assert cast(Any, scan.is_closed) is True
            assert isinstance(scan, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, scan.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_screenshot(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="",
                account_id="accountId",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.addressing import LOADocumentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLOADocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        loa_document = client.addressing.loa_documents.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )
        assert_matches_type(Optional[LOADocumentCreateResponse], loa_document, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.addressing.loa_documents.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_document = response.parse()
        assert_matches_type(Optional[LOADocumentCreateResponse], loa_document, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.addressing.loa_documents.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_document = response.parse()
            assert_matches_type(Optional[LOADocumentCreateResponse], loa_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.loa_documents.with_raw_response.create(
                account_id="",
                loa_document="@document.pdf",
            )


class TestAsyncLOADocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        loa_document = await async_client.addressing.loa_documents.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )
        assert_matches_type(Optional[LOADocumentCreateResponse], loa_document, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.addressing.loa_documents.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_document = await response.parse()
        assert_matches_type(Optional[LOADocumentCreateResponse], loa_document, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.addressing.loa_documents.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_document = await response.parse()
            assert_matches_type(Optional[LOADocumentCreateResponse], loa_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.loa_documents.with_raw_response.create(
                account_id="",
                loa_document="@document.pdf",
            )

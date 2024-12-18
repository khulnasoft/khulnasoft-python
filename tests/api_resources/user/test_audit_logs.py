# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft._utils import parse_datetime
from khulnasoft.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from khulnasoft.types.shared import AuditLog

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        audit_log = client.user.audit_logs.list()
        assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        audit_log = client.user.audit_logs.list(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            action={"type": "add"},
            actor={
                "ip": "17.168.228.63",
                "email": "alice@example.com",
            },
            before=parse_datetime("2019-04-30T01:12:20Z"),
            direction="desc",
            export=True,
            hide_user_logs=True,
            page=50,
            per_page=25,
            since=parse_datetime("2019-04-30T01:12:20Z"),
            zone={"name": "example.com"},
        )
        assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.user.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.user.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        audit_log = await async_client.user.audit_logs.list()
        assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        audit_log = await async_client.user.audit_logs.list(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            action={"type": "add"},
            actor={
                "ip": "17.168.228.63",
                "email": "alice@example.com",
            },
            before=parse_datetime("2019-04-30T01:12:20Z"),
            direction="desc",
            export=True,
            hide_user_logs=True,
            page=50,
            per_page=25,
            since=parse_datetime("2019-04-30T01:12:20Z"),
            zone={"name": "example.com"},
        )
        assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.user.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.user.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[AuditLog], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True

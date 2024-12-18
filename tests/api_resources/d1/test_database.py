# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.d1 import (
    D1,
    DatabaseRawResponse,
    DatabaseListResponse,
    DatabaseQueryResponse,
    DatabaseCreateResponse,
    DatabaseDeleteResponse,
)
from khulnasoft.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        database = client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )
        assert_matches_type(DatabaseCreateResponse, database, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Khulnasoft) -> None:
        database = client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
            primary_location_hint="wnam",
        )
        assert_matches_type(DatabaseCreateResponse, database, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.d1.database.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseCreateResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.d1.database.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseCreateResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.create(
                account_id="",
                name="my-database",
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        database = client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Khulnasoft) -> None:
        database = client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            page=1,
            per_page=10,
        )
        assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.d1.database.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.d1.database.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        database = client.d1.database.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DatabaseDeleteResponse, database, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.d1.database.with_raw_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseDeleteResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.d1.database.with_streaming_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseDeleteResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.delete(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.delete(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        database = client.d1.database.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.d1.database.with_raw_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.d1.database.with_streaming_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(D1, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.get(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.get(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_query(self, client: Khulnasoft) -> None:
        database = client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Khulnasoft) -> None:
        database = client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Khulnasoft) -> None:
        response = client.d1.database.with_raw_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Khulnasoft) -> None:
        with client.d1.database.with_streaming_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseQueryResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.query(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.query(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

    @parametrize
    def test_method_raw(self, client: Khulnasoft) -> None:
        database = client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(DatabaseRawResponse, database, path=["response"])

    @parametrize
    def test_method_raw_with_all_params(self, client: Khulnasoft) -> None:
        database = client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(DatabaseRawResponse, database, path=["response"])

    @parametrize
    def test_raw_response_raw(self, client: Khulnasoft) -> None:
        response = client.d1.database.with_raw_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(DatabaseRawResponse, database, path=["response"])

    @parametrize
    def test_streaming_response_raw(self, client: Khulnasoft) -> None:
        with client.d1.database.with_streaming_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(DatabaseRawResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_raw(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.d1.database.with_raw_response.raw(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            client.d1.database.with_raw_response.raw(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )


class TestAsyncDatabase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )
        assert_matches_type(DatabaseCreateResponse, database, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
            primary_location_hint="wnam",
        )
        assert_matches_type(DatabaseCreateResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.d1.database.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseCreateResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.d1.database.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="my-database",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseCreateResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.create(
                account_id="",
                name="my-database",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            page=1,
            per_page=10,
        )
        assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.d1.database.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.d1.database.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DatabaseListResponse], database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DatabaseDeleteResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.d1.database.with_raw_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseDeleteResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.d1.database.with_streaming_response.delete(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseDeleteResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.delete(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.delete(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.d1.database.with_raw_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(D1, database, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.d1.database.with_streaming_response.get(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(D1, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.get(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.get(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.d1.database.with_raw_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseQueryResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.d1.database.with_streaming_response.query(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseQueryResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.query(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.query(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

    @parametrize
    async def test_method_raw(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )
        assert_matches_type(DatabaseRawResponse, database, path=["response"])

    @parametrize
    async def test_method_raw_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        database = await async_client.d1.database.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            params=["firstParam", "secondParam"],
        )
        assert_matches_type(DatabaseRawResponse, database, path=["response"])

    @parametrize
    async def test_raw_response_raw(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.d1.database.with_raw_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(DatabaseRawResponse, database, path=["response"])

    @parametrize
    async def test_streaming_response_raw(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.d1.database.with_streaming_response.raw(
            database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(DatabaseRawResponse, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_raw(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.d1.database.with_raw_response.raw(
                database_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                account_id="",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `database_id` but received ''"):
            await async_client.d1.database.with_raw_response.raw(
                database_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sql="SELECT * FROM myTable WHERE field = ? OR field = ?;",
            )

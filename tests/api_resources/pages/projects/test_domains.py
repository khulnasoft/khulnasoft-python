# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.pagination import SyncSinglePage, AsyncSinglePage
from khulnasoft.types.pages.projects import (
    DomainGetResponse,
    DomainEditResponse,
    DomainCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Khulnasoft) -> None:
        domain = client.pages.projects.domains.create(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )
        assert_matches_type(Optional[DomainCreateResponse], domain, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Khulnasoft) -> None:
        response = client.pages.projects.domains.with_raw_response.create(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Optional[DomainCreateResponse], domain, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Khulnasoft) -> None:
        with client.pages.projects.domains.with_streaming_response.create(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Optional[DomainCreateResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.create(
                project_name="this-is-my-project-01",
                account_id="",
                body={"name": "example.com"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.create(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={"name": "example.com"},
            )

    @parametrize
    def test_method_list(self, client: Khulnasoft) -> None:
        domain = client.pages.projects.domains.list(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[object], domain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Khulnasoft) -> None:
        response = client.pages.projects.domains.with_raw_response.list(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(SyncSinglePage[object], domain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Khulnasoft) -> None:
        with client.pages.projects.domains.with_streaming_response.list(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(SyncSinglePage[object], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.list(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.list(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Khulnasoft) -> None:
        domain = client.pages.projects.domains.delete(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Khulnasoft) -> None:
        response = client.pages.projects.domains.with_raw_response.delete(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Khulnasoft) -> None:
        with client.pages.projects.domains.with_streaming_response.delete(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(object, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.delete(
                domain_name="this-is-my-domain-01.com",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.delete(
                domain_name="this-is-my-domain-01.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.pages.projects.domains.with_raw_response.delete(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @parametrize
    def test_method_edit(self, client: Khulnasoft) -> None:
        domain = client.pages.projects.domains.edit(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            body={},
        )
        assert_matches_type(Optional[DomainEditResponse], domain, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Khulnasoft) -> None:
        response = client.pages.projects.domains.with_raw_response.edit(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Optional[DomainEditResponse], domain, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Khulnasoft) -> None:
        with client.pages.projects.domains.with_streaming_response.edit(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Optional[DomainEditResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.edit(
                domain_name="this-is-my-domain-01.com",
                account_id="",
                project_name="this-is-my-project-01",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.edit(
                domain_name="this-is-my-domain-01.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.pages.projects.domains.with_raw_response.edit(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Khulnasoft) -> None:
        domain = client.pages.projects.domains.get(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Khulnasoft) -> None:
        response = client.pages.projects.domains.with_raw_response.get(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Khulnasoft) -> None:
        with client.pages.projects.domains.with_streaming_response.get(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.get(
                domain_name="this-is-my-domain-01.com",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.get(
                domain_name="this-is-my-domain-01.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.pages.projects.domains.with_raw_response.get(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoft) -> None:
        domain = await async_client.pages.projects.domains.create(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )
        assert_matches_type(Optional[DomainCreateResponse], domain, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.create(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Optional[DomainCreateResponse], domain, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.create(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Optional[DomainCreateResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.create(
                project_name="this-is-my-project-01",
                account_id="",
                body={"name": "example.com"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.create(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={"name": "example.com"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoft) -> None:
        domain = await async_client.pages.projects.domains.list(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[object], domain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.list(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(AsyncSinglePage[object], domain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.list(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(AsyncSinglePage[object], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.list(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.list(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncKhulnasoft) -> None:
        domain = await async_client.pages.projects.domains.delete(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.delete(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(object, domain, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.delete(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(object, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.delete(
                domain_name="this-is-my-domain-01.com",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.delete(
                domain_name="this-is-my-domain-01.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.delete(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncKhulnasoft) -> None:
        domain = await async_client.pages.projects.domains.edit(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            body={},
        )
        assert_matches_type(Optional[DomainEditResponse], domain, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.edit(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Optional[DomainEditResponse], domain, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.edit(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Optional[DomainEditResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.edit(
                domain_name="this-is-my-domain-01.com",
                account_id="",
                project_name="this-is-my-project-01",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.edit(
                domain_name="this-is-my-domain-01.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.edit(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncKhulnasoft) -> None:
        domain = await async_client.pages.projects.domains.get(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.get(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.get(
            domain_name="this-is-my-domain-01.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.get(
                domain_name="this-is-my-domain-01.com",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.get(
                domain_name="this-is-my-domain-01.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.get(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

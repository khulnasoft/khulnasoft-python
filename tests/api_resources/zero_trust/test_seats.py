# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft.types.zero_trust import SeatEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Khulnasoft) -> None:
        seat = client.zero_trust.seats.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
            ],
        )
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Khulnasoft) -> None:
        response = client.zero_trust.seats.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = response.parse()
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Khulnasoft) -> None:
        with client.zero_trust.seats.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = response.parse()
            assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Khulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.seats.with_raw_response.edit(
                account_id="",
                body=[
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                        "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                        "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                        "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    },
                ],
            )


class TestAsyncSeats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncKhulnasoft) -> None:
        seat = await async_client.zero_trust.seats.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
            ],
        )
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.zero_trust.seats.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = await response.parse()
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.zero_trust.seats.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                    "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = await response.parse()
            assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncKhulnasoft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.seats.with_raw_response.edit(
                account_id="",
                body=[
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                        "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                        "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                        "seat_uid": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    },
                ],
            )

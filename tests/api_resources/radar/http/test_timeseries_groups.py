# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from khulnasoft import Khulnasoft, AsyncKhulnasoft
from tests.utils import assert_matches_type
from khulnasoft._utils import parse_datetime
from khulnasoft.types.radar.http import (
    TimeseriesGroupOSResponse,
    TimeseriesGroupBrowserResponse,
    TimeseriesGroupBotClassResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupDeviceTypeResponse,
    TimeseriesGroupTLSVersionResponse,
    TimeseriesGroupHTTPVersionResponse,
    TimeseriesGroupPostQuantumResponse,
    TimeseriesGroupHTTPProtocolResponse,
    TimeseriesGroupBrowserFamilyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bot_class(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.bot_class()
        assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_bot_class_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.bot_class(
            agg_interval="1h",
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_bot_class(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.bot_class()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_bot_class(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.bot_class() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_browser(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.browser()
        assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_browser_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.browser(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit_per_group=4,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_browser(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.browser()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_browser(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.browser() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_browser_family(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.browser_family()
        assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_browser_family_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.browser_family(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_browser_family(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.browser_family()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_browser_family(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.browser_family() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_device_type(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.device_type()
        assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_device_type_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.device_type(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_device_type(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.device_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_device_type(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.device_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_http_protocol(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.http_protocol()
        assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_http_protocol_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.http_protocol(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_http_protocol(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.http_protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_http_protocol(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.http_protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_http_version(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.http_version()
        assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_http_version_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.http_version(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_http_version(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.http_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_http_version(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.http_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.ip_version()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.ip_version(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_os(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.os()
        assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_os_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.os(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_os(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.os()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_os(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.os() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_post_quantum(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.post_quantum()
        assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_post_quantum_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.post_quantum(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_post_quantum(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.post_quantum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_post_quantum(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.post_quantum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tls_version(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.tls_version()
        assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_tls_version_with_all_params(self, client: Khulnasoft) -> None:
        timeseries_group = client.radar.http.timeseries_groups.tls_version(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
        )
        assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_tls_version(self, client: Khulnasoft) -> None:
        response = client.radar.http.timeseries_groups.with_raw_response.tls_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_tls_version(self, client: Khulnasoft) -> None:
        with client.radar.http.timeseries_groups.with_streaming_response.tls_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_bot_class(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.bot_class()
        assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_bot_class_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.bot_class(
            agg_interval="1h",
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_bot_class(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.bot_class()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_bot_class(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.bot_class() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupBotClassResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_browser(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.browser()
        assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_browser_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.browser(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit_per_group=4,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_browser(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.browser()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_browser(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.browser() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupBrowserResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_browser_family(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.browser_family()
        assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_browser_family_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.browser_family(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_browser_family(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.browser_family()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_browser_family(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.browser_family() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupBrowserFamilyResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_device_type(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.device_type()
        assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_device_type_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.device_type(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_device_type(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.device_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_device_type(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.device_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupDeviceTypeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_http_protocol(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.http_protocol()
        assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_http_protocol_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.http_protocol(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_http_protocol(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.http_protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_http_protocol(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.http_protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupHTTPProtocolResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_http_version(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.http_version()
        assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_http_version_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.http_version(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_http_version(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.http_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_http_version(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.http_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupHTTPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.ip_version()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.ip_version(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_os(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.os()
        assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_os_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.os(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_os(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.os()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_os(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.os() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupOSResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_post_quantum(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.post_quantum()
        assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_post_quantum_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.post_quantum(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_post_quantum(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.post_quantum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_post_quantum(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.post_quantum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupPostQuantumResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tls_version(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.tls_version()
        assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_tls_version_with_all_params(self, async_client: AsyncKhulnasoft) -> None:
        timeseries_group = await async_client.radar.http.timeseries_groups.tls_version(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
        )
        assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_tls_version(self, async_client: AsyncKhulnasoft) -> None:
        response = await async_client.radar.http.timeseries_groups.with_raw_response.tls_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_tls_version(self, async_client: AsyncKhulnasoft) -> None:
        async with async_client.radar.http.timeseries_groups.with_streaming_response.tls_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupTLSVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

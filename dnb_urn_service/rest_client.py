# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 University Münster.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Python API client wrapper for the DNB URN service API.

API documentation is available at
https://wiki.dnb.de/display/URNSERVDOK/URN-Service+API.
"""

import json
import requests

from .errors import DNBURNServiceError
from .request import DNBUrnServiceRequest

HTTP_OK = requests.codes['ok']
HTTP_CREATED = requests.codes['created']
HTTP_NO_CONTENT = requests.codes['no_content']


class DNBUrnServiceRESTClient(object):
    """DNB URN service API client wrapper."""

    def __init__(self, username, password, prefix, test_mode=False, url=None,
                 timeout=None):
        """Initialize the API client wrapper.

        :param username: DNB username.
        :param password: DNB password.
        :param prefix: URN prefix (or DNB_URN_PREFIX).
        :param test_mode: use test URL when True
        :param url: DNB URN service API base URL.
        :param timeout: Connect and read timeout in seconds. Specify a tuple
            (connect, read) to specify each timeout individually.
        """
        self.username = username
        self.password = password
        self.prefix = prefix

        if test_mode:
            self.api_url = "https://api.nbn-resolving.org/sandbox/v2/"
        else:
            self.api_url = url or "https://api.nbn-resolving.org/v2/"

        if not self.api_url.endswith('/'):
            self.api_url += '/'

        self.timeout = timeout

    def __repr__(self):
        """Create string representation of object."""
        return '<DNBUrnServiceRESTClient: {0}>'.format(self.username)

    def _create_request(self):
        """Create a new Request object."""
        return DNBUrnServiceRequest(
            base_url=self.api_url,
            username=self.username,
            password=self.password,
            timeout=self.timeout,
        )

    def get_urn(self, urn):
        """Get the URL where the resource pointed by the URN is located.

        :param urn: URN name of the resource.
        """
        request = self._create_request()
        resp = request.get("urns/urn/" + urn + "/my-urls")
        if resp.status_code == HTTP_OK:
            return resp.json()['items'][0]['url']
        else:
            raise DNBURNServiceError.factory(resp.status_code, resp.text)

    def post_urn(self, urn, data):
        """Post a new JSON payload to DNB."""
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
        }
        body = data
        request = self._create_request()
        resp = request.post("urns/urn/" + urn + "/urls", body=json.dumps(body), headers=headers)
        if resp.status_code == HTTP_CREATED:
            return resp.json()['urn']
        else:
            raise DNBURNServiceError.factory(resp.status_code, resp.text)

    def patch_urn(self, urn, data):
        """Patch a new JSON payload to DNB."""
        headers = {"content-type": "application/json"}
        body = data
        request = self._create_request()
        resp = request.patch("urns/urn/" + urn, body=json.dumps(body), headers=headers)
        if resp.status_code == HTTP_NO_CONTENT:
            return ""
        else:
            raise DNBURNServiceError.factory(resp.status_code, resp.text)

    def create_urn(self, url, urn, owner):
        """Create an urn.

        This URN will be public and can be deleted.
        If urn is not provided, there will be an error.
        :param url: URL where the urn will resolve.
        :param urn: URN (e.g. urn:nbn:de:hbz:6-1234)
        :param owner: ID of the owning organisation, obtained from DNB
        :return:
        """
        data = {
            "url": url,
            "owner": self.api_url + "organisations/id/" + owner,
            "priority": 10
        }

        return self.post_urn(urn, data)

    def create_successor(self, urn, successor):
        data = {"successor": self.api_url + "urns/urn/" + successor}

        return self.patch_urn(urn, data)

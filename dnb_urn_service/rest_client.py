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

import requests

HTTP_OK = requests.codes['ok']
HTTP_CREATED = requests.codes['created']


class DNBUrnServiceRESTClient(object):
    """DataCite MDS API client wrapper.
    Warning: The DataCite MDS API is being maintained but is no longer actively
    developed.
    """

    def __init__(self, username, password, prefix, test_mode=False, url=None,
                 timeout=None):
        """Initialize the API client wrapper.
        :param username: DataCite username.
        :param password: DataCite password.
        :param prefix: DOI prefix (or CFG_DATACITE_DOI_PREFIX).
        :param test_mode: use test URL when True
        :param url: DataCite API base URL.
        :param timeout: Connect and read timeout in seconds. Specify a tuple
            (connect, read) to specify each timeout individually.
        """
        self.username = username
        self.password = password
        self.prefix = prefix

        if test_mode:
            self.api_url = "https://mds.test.datacite.org/"
        else:
            self.api_url = url or "https://mds.datacite.org/"

        if not self.api_url.endswith('/'):
            self.api_url += '/'

        self.timeout = timeout

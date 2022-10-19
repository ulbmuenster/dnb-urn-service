# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 University Münster.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Test helpers."""

import os

from dnb_urn_service import DNBUrnServiceRESTClient


def get_client(username="DNB", password="pw", prefix="urn:nbn:"):
    """Create an API client."""
    client = DNBUrnServiceRESTClient(
        username=username,
        password=password,
        prefix=prefix,
        test_mode=True,
    )
    return client


def get_credentials():
    """Get credentials from environment."""
    username = os.environ["DNB_URN_USER"]
    password = os.environ["DNB_URN_PW"]
    prefix = os.environ["DNB_URN_PREFIX"]
    return username, password, prefix

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

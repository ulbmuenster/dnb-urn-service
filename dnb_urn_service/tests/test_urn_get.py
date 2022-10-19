# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 University Münster.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Tests for /urns/urn POST."""

import pytest
from helpers import get_client, get_credentials

from dnb_urn_service.errors import DNBURNServiceUserNotAuthenticatedError, DNBURNServiceUrnNotRegisteredError


def test_urn_get_401():
    """Test."""
    username, password, prefix = get_credentials()
    d = get_client(username=username, password=password, prefix=prefix)
    with pytest.raises(DNBURNServiceUserNotAuthenticatedError):
        d.get_urn("urn:nbn:de:hbz:6-63719399444")


def test_urn_get_404():
    """Test."""
    username, password, prefix = get_credentials()
    d = get_client(username=username, password=password, prefix=prefix)
    with pytest.raises(DNBURNServiceUrnNotRegisteredError):
        d.get_urn("urn:nbn:de:hbz:6-123")

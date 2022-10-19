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
import responses
from helpers import get_client


@responses.activate
def test_urn_post_200():
    assert True is True

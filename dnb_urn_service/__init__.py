# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 University Münster.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.


"""Python API wrapper for the DNB URN service API."""

from .rest_client import DNBUrnServiceRESTClient

__version__ = "0.1.5"

__all__ = ("__version__", "DNBUrnServiceRESTClient")

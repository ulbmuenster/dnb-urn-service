# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 University Münster.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Errors for the DNB URN service API."""


class HttpError(Exception):
    """Exception raised when a connection problem happens."""


class DNBURNServiceError(Exception):
    """Exception raised when the server returns a known HTTP error code."""

    @staticmethod
    def factory(err_code, *args):
        """Create exceptions through a Factory based on the HTTP error code."""
        return DNBURNServiceServerError


class DNBURNServiceServerError(DNBURNServiceError):
    """An internal server error happened on the DNB end. Try later.

    Base class for all 5XX-related HTTP error codes.
    """

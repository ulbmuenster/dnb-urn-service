#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 University Münster.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

# Quit on errors
set -o errexit

if [ -z "${DNB_URN_USER}" ] || [ -z "${DNB_URN_PW}" ] || [ -z "${DNB_URN_PREFIX}" ]; then
  echo "DNB_URN_USER, DNB_URN_PW or DNB_URN_PREFIX env var not set"
  exit 1
fi

# Quit on unbound symbols
set -o nounset

python -m pytest

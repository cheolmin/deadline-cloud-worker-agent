# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

from __future__ import annotations

from .config import DEADLINE_BOTOCORE_CONFIG, OTHER_BOTOCORE_CONFIG
from .logger import logger
from .retries import NoOverflowExponentialBackoff
from .shim import (
    DeadlineClient,
    Session,
)

from typing import Dict as dict
from typing import List as list
__all__ = [
    "DEADLINE_BOTOCORE_CONFIG",
    "DeadlineClient",
    "NoOverflowExponentialBackoff",
    "OTHER_BOTOCORE_CONFIG",
    "Session",
    "logger",
]

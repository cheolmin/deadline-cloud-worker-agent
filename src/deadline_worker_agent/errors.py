# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

from __future__ import annotations

from typing import Dict as dict
from typing import List as list

class ConfigurationError(Exception):
    """An exception raised when an error is encountered loading configuration"""

    pass


class PlatformInterruption(Exception):
    """A shutdown warning signal was emitted by the platform"""

    pass


class ServiceShutdown(Exception):
    """The render management service is issuing a shutdown command"""

    pass

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

"""AWS Deadline Cloud Worker Agent"""

from ._version import __version__  # noqa
from .installer import install
from .startup.config import Configuration
from .startup.entrypoint import entrypoint
from .worker import Worker

from typing import Dict as dict
from typing import List as list
__all__ = ["entrypoint", "install", "Worker", "Configuration"]

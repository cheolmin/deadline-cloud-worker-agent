# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

from __future__ import annotations
from enum import Enum


from typing import Dict as dict
from typing import List as list
class JobEntityType(str, Enum):
    JOB_ATTACHMENT_DETAILS = "jobAttachmentDetails"
    JOB_DETAILS = "jobDetails"
    STEP_DETAILS = "stepDetails"
    ENVIRONMENT_DETAILS = "environmentDetails"

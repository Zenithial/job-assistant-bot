from enum import Enum

class BotState(Enum):
    DEFAULT = 1
    WAIT_FOR_CV = 2
    JOB_DESCRIPTION = 3
    COMPARE_CV_TO_JOB_DESCRIPTION = 4
    
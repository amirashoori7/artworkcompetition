from enum import *

class Status(IntEnum):
    Partially_Submitted = -1
    Submitted_Successfully = 0
    Revision_Required = 1
    Rejected_Stage_0 = 2
    Accepted_Stage_0 = 3
    Waiting_For_Decision = 4
    Accepted_Stage_1 = 5
    Rejected_Stage_1 = 6
    Waiting_For_Artpost = 7
    Rejected_Stage_2 = 8
    Artpost_Recieved = 9
    Rejected_Stage_3 = 10
    Winner = 11

    @classmethod
    def statuslist(cls):
        return ((key.value, key.name.replace('_', ' ')) for key in cls)

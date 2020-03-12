from enum import IntEnum, Enum

class Province(Enum):
    Eastern_Cape = "EC"
    Free_State = "FS"
    Gauteng = "GT"
    KwaZulu_Natal = "KZW"
    Limpopo = "LP"
    Mpumalanga = "MP"
    North_West = "NW"
    Northern_Cape = "NC"
    Western_Cape = "WC"

    @classmethod
    def provincelist(cls):
        return((key.value, key.name.replace('_', ' ')) for key in cls)

class Status(IntEnum):
    Pending = -1 
    Submitted = 0
    Requires_Revision = 1
    Revised_work = 2
    Rejected_Stage_0 = 3
    Accepted_Stage_0 = 4 
    Waiting_For_Decision = 5
    Accepted_Stage_1 = 6
    Rejected_Stage_1 = 7
    Waiting_For_Artpost = 8
    Rejected_Stage_2 = 9
    Artpost_Recieved = 10
    Rejected_Stage_3 = 11
    Winner = 12

    @classmethod
    def statuslist(cls):
        return ((key.value, key.name.replace('_', ' ')) for key in cls)

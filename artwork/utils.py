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
    Swaziland_and_Lesotho = "Other"
    
    @classmethod
    def provincelist(cls):
        return((key.value, key.name.replace('_', ' ')) for key in cls)

class Status(IntEnum):
    Pending = -1 
    Submitted = 0
    Requires_Revision = 1
    Revised_work = 2
    Rejected_Entry = 3
    Accepted_Entry = 4 
    Waiting_For_GMMDC_Decision = 5
    Accepted_By_GMMDC = 6
    Rejected_By_GMMDC = 7
    Waiting_For_Artpost = 8
    Rejected_By_Judge2 = 9
    Artpost_Recieved = 10
    Rejected_At_Final_Stage = 11
    Winner = 12

    @classmethod
    def statuslist(cls):
        return ((key.value, key.name.replace('_', ' ')) for key in cls)

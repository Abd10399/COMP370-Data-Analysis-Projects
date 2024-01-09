from enum import Enum


class Nyc311ColumnName(Enum):
    Borough = "Borough"
    ComplaintType = "Complaint Type"
    OpenedDate = "Created Date"
    ClosedDate = "Closed Date"
    Status = "Status"

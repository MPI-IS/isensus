from enum import Enum


class Contract(Enum):

    """
    Enumeration for the type of contract 
    the user may have (as an employee).
    User's attribute 'contract' is expected
    to be an instance of the Contract enumeration.
    """

    guest = 0
    normal = 1
    stipend = 2

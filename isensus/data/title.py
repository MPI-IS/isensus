from enum import Enum


class Title(Enum):

    """
    Enumeration for the title 
    the user may have (as an employee).
    User's attribute 'title' is expected
    to be an instance of the Title enumeration.
    """

    phD = 0
    postdoc = 1
    group_leader = 2
    master = 3
    internship = 4
    hiwi = 5
    permanent = 6
    guest = 7

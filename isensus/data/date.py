import datetime


class Date:

    """ Class representing a date.

    Some of the User's attribute are expected to 
    be instance of Date (e.g. shadow_extension,
    contract_start, contract_end).
    
    Parameters
    ----------
    date: str
        should be in format YEAR-MONTH-DAY

    Raises
    ------
    ValueError:
        if the date is not provided in the expected
        format.

    """

    str_format: str = "%Y-%m-%d"

    def __init__(self, date: str):
        if date:
            self._date: datetime.datetime = self._from_string(date)
        else:
            self._date = None

    def get(self):
        return self._date

    def __repr__(self) -> str:
        if self._date is None:
            return ""
        return str(self)

    def __str__(self) -> str:
        if self._date:
            return datetime.datetime.strftime(self._date, self.str_format)
        else:
            return "Not set"

    @classmethod
    def _from_string(cls, date: str) -> datetime.datetime:
        if date is None or not date:
            return cls("")
        try:
            instance: datetime.datetime = datetime.datetime.strptime(
                date, cls.str_format
            )
        except ValueError:
            raise ValueError(str("date should be of format YEAR-MONTH-DAY"))
        return cls(instance)

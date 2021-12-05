import typing


class ListAttribute:
    """ Mother class for User's list attributes 
    
    Some attributes of instances of User have a list of 
    string values (e.g. a user can have several notes and warnings).
    ListAttribute is the mother class for such attributes. 
    An instance of ListAttribute stores all indexed values as a
    single string separated by a <br> separator. 
    """

    separator: str = "<br>"

    def __init__(self, content: str):
        self._items: typing.List[str] = content.split(self.separator)
        
    def get(self,index: int) -> str:
        """ Returns the item at the specified index,
        or raises an IndexError.

        Parameters
        ----------
        index: int
            index of the entry to return
        
        Raises
        ------
        IndexError
        """
        return self._items[index]
        
    def rm(self, index: int):
        """ Delete the value at the specified index

        Parameters
        ----------
        index: int
            index of the entry to remove

        Raises
        ------
        IndexError
        """
        del self._items[index]

    def __repr__(self) -> str:
        return self.separator.join(self._items)


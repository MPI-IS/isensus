import typing
import functools
from ..data.user import User
from . decorators import not_attr


class Warning:

    def __call__(self, user: User)->str:
        raise NotImplementedError("subclasses of Warning must implement "
                                  "a __call__ method [[User],str]")

class BoolsWarning(Warning):

    def __init__(self, attributes: typing.Sequence[str],not_attributes: typing.Sequence[str]):
        self._attributes = attributes
        self._not_attributes = attributes

    def __call__(self, user: User)->None:
        if any([getattr(user,attr) for
                attr in self._attributes]):
            return None
        if any([not getattr(user,attr)
                for attr in self._not_attributes]):
            return None
        if len(self._attributes)==1:
            attr_grammars = [self._attributes[0],
                             "attribute",
                             "is"]
        else:
            attr_grammars = [", ".join(self._attributes),
                             "attributes",
                             "are"]
        if len(self._not_attributes)==1:
            not_attr_grammars = [self._not_attributes[0],
                                 "attribute",
                                 "is"]
        else:
            not_attr_grammars = [", ".join(self._not_attributes),
                                 "attributes",
                                 "are"]
        formats = attr_grammars + not_attr_grammars
        return str("{} {} {} True, "
                   "but {} {} {} not".format(*formats))

    
form_not_sent = BoolWarnings(["ldap"],["forms_sent"])
no_mail_account_or_forwarder = BoolWarnings(["ldap"],["mail_account","forwarder"])
no_title = BoolWarnings(["ldap"],["title"])
no_contract_type = BoolWarnings(["ldap"],["contract"])
no_contract_end = BoolWarnings(["ldap"],["contract_end"])

_var = None
_locs = locals()
warnings = [_var for _var in locs.values()
            if inspect.isclass(_var)
            and issubclass(_var,Warning)

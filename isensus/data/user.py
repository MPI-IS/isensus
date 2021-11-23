import typing
import json
from dataclasses import dataclass
from .title import Title
from .contract import Contract
from .date import Date
from .warnings import Warnings
from .notes import Notes
from isensus import errors


@dataclass
class User:

    """Class encapsulating all the attributes of a user.

    Attributes
    ----------

      userid: str
          As set in ldap.
      firstname: str
          First name of user.
      lastname: str
          Last name of user.
      forms_sent: bool
          If true, the IT forms have been sent to the users.
      forms_received: bool
          If true, the signed IT forms have been received
          by the IT admin.
      ldap: bool
          If true account has been created in ldap.
      shadow_extension: Date
          If None, no shadow extension has been set in ldap.
          Otherwise: expiration date of the shadow extension.
      vaulted: bool
          If true, ldap account has been vaulted.
      mail_account: bool
          If true, a regular mail account has been created for the user.
      in_mailing_lists: bool
          If true, users has been added to the mailing lists
          he/she should be part of.
      forwarder: bool
          If true, a forwarder mail has been set for the user in the mailhost.
      website_privacy: bool
          If true, the security tab of the user webpage has been updated.
      website_alumni: bool
          If true the user has been set as alumni in the website.
      is_snipe_cleared: bool
          If true, no hardware is checked out to the user in is-snip.
      closure_mail_sent: bool
          User has been sent a mail informing him/her
          of the upcoming vaulting of his/her account.
      contract: Contract 
          Type of contract the user has with the institute.
      contract_start: Date
          Date of the start of the user's contract.
      contract_end: Date
          Date of the end of the users' contract.
      title: Title
          Title of the user (as MPG employee).
      employee_id: int 
          MPG employee id.
      warnings: Warnings
          List of arbitrary warnings set by the IT admin.
      notes: Notes
          List of arbitrary notes and reminders set by the IT admin.
    """

    userid: str = None
    firstname: str = None
    lastname: str = None
    ldap: bool = False
    vaulted: bool = False
    mail_account: bool = False
    in_mailing_lists: bool = False
    forwarder: bool = False
    shadow_extension: Date = Date(None)
    forms_sent: bool = False
    forms_received: bool = False
    website_privacy: bool = False
    website_alumni: bool = False
    is_snipe_cleared: bool = False
    closure_mail_sent: bool = False
    contract: Contract = None
    contract_start: Date = Date(None)
    contract_end: Date = Date(None)
    title: Title = None
    employee_id: int = None
    warnings: Warnings = Warnings("")
    notes: Notes = Notes("")

    @classmethod
    def get_type(cls, attribute: str) -> typing.Any:
        """ Returns the type of the attribute

        Parameters
        ----------
        attribute: str
            attribute's name
        
        Returns
        -------
        type: object 
            The type of the attribute.

        Raises
        ------
        UnknownAttributeError
        """
        if attribute not in cls.__annotations__.keys():
            raise errors.UnknownAttributeError(attribute)
        return cls.__annotations__[attribute]

    @classmethod
    def create_new(cls, userid, firstname, lastname):
        """ Creates a new instance of User

        Parameters
        ----------
        userid: str
            userid of the user, as set in ldap
        firstname: str
            first name of the user
        lastname: str
            last name of the user
        
        Returns
        -------
        user:
            New instance of users, with all attributes
            set to reasonable starting values.
        """
        instance = cls()
        instance.userid = userid
        instance.firstname = firstname
        instance.lastname = lastname
        return instance

    @classmethod
    def _user_from_json(cls, from_json: typing.Dict[str, typing.Any]):
        """
        Returns an instance of User from a (decoded) json dictionary.
        """
        # getting the type of each attributes (using the typing hints)
        types = cls.__annotations__
        # instantiating User
        user = cls()
        # adding attributes, casted to the correct type
        for attr, value in from_json.items():
            if value == "None":
                value = None
            if value is not None:
                if value and value[0] == "'":
                    value = value[1:]
                if value and value[-1] == "'":
                    value = value[:-1]
                setattr(user, attr, types[attr](value))
        # returning the instance
        return user

    @classmethod
    def from_json(cls, json_dump: typing.Dict[str, str]) -> typing.Dict[str, object]:
        """ Returns a dictionary of instances of User

        Returns a dictionary of instances of users (keys are the
        userids) generated from a json dump (that should have been
        generated using the to_json method of this class).

        Parameters
        ----------
        json_dump: str
            The string encoding the dictionary in json encoder
            format.

        Returns
        -------
        users: dict
            Dictionary with keys userid (str) and values
            related instance of User.
        """
        # "casting" to a dictionary which values are
        # instances of User.
        return {
            userid: cls._user_from_json(userdict)
            for userid, userdict in json_dump.items()
        }

    @classmethod
    def to_json(cls, users: typing.Dict[str, object]) -> str:
        """ Encode a user database dictionary into json encoder format

        Users being a dictionary which keys are userids and
        values corresponding instances of User, returns a json
        string dump.

        Parameters
        ----------
        users: dict
            Dictionary with userid as keys (str) and instances of User
            as values.
        """
        d = {userid: instance.to_dict() for userid, instance in users.items()}
        return json.dumps(d)

    def to_dict(self) -> typing.Dict[str, str]:
        """ Returns dictionary representation of the user

        Returns a dictionary corresponding to this
        instance of user with keys corresponding to
        attributes (as strings) and values to attribute's values casted
        to string (repr).

        Returns
        -------
        users: dict
            keys: attributes (as str), values: values of the attributes (as
            str)
        """
        attr_types = self.__class__.__annotations__
        return {attr: repr(getattr(self, attr)) for attr in attr_types.keys()}

    def to_string(self, nb_tabs: int = 1) -> str:
        """ String representation of the user

        Returns a string representation of the user suitable
        for display in a terminal. 

        Parameters
        ----------
        nb_tabs: int
            Number of tabulations to add before
            each attribute.

        Returns
        -------
            Multi-lines string representation of the user
        """
        tabs = "\t" * nb_tabs
        return "\n".join(
            [
                "".join([tabs, attr, "\t", value])
                for attr, value in self.__dict__.items()
            ]
        )

    def maybe_me(self, usertip: str) -> bool:
        """ Check if a usertip may correspond to this user

        Returns True if either userid, firstname
        or lastname starts with usertip, False 
        otherwise.

        Parameters
        ----------
        usertip: str
            End-user search string for users
        
        Returns
        -------
            True if the usertip match this user.
        """
        return any(
            (
                self.userid.startswith(usertip),
                self.firstname.startswith(usertip),
                self.lastname.startswith(usertip),
            )
        )

    @staticmethod
    def find_user(users: typing.Dict[str, object], usertip: str) -> object:
        """ Search for the user corresponding to the usertip

        Returns the user corresponding to the usertip (see 
        the maybe_me method). 

        Parameters
        ----------
        users: dict
            Database of user with userids as keys (str) and
            instances of User as values
        usertip: str
            End-user search string for users

        Returns
        -------
            The corresponding instance of User (i.e. user for 
        which either the userid, the firstname or the lastname
        starts with usertip)

        Raises
        ------
        UserNotFoundError:
            If no corresponding user is found.
        AmbiguousUserErrorL
            If more than one user is found.
        """

        candidates = [
            userid for userid, instance in users.items if instance.maybe_me(usertip)
        ]

        if not candidates:
            raise errors.UserNotFoundError(usertip)

        if len(candidates) > 1:
            raise errors.AmbiguousUserError(usertip, candidates)

        return users[candidates[0]]

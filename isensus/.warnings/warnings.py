import inspect


class Warnings:
    def __init__(self, config, user_data):
        self._config = config
        self._user_data = user_data


def _get_warnings(warnings_instance):
    """
    returns a list of the returned value of
    all private functions of warnings_instance
    """
    # all functions of this class
    warning_functions = inspect.getmembers(
        warnings_instance.__class__, predicate=inspect.isfunction
    )
    # all private functions of this class, with the
    # exclusion of __init__
    warning_functions = [
        wf
        for wf in warning_functions
        if not wf[0].startswith("__") and wf[0].startswith("_")
    ]
    warnings = []
    for _, function in warning_functions:
        warnings.append(function(warnings_instance))
    return [str(w) for w in warning if w is not None]


class CoreWarnings(Warnings):
    """
    Warnings for all users (alumni or not)
    """

    def __init__(self, config, user_data):
        super().__init__(config, user_data)
        expiration = self.user_data["expiration"]
        date = datetime.date(expiration.year, expiration.month, expiration.day)
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        self._expired = (date - now).days > 0

    def _not_set_as_alumni(self):
        if self._expired and not self._user_data["contract"] == "alumni":
            return str("contract expired but not set " "alumni")
        return []

    def get(self):
        """
        returns the list of warnings of the user
        """
        return get_warnings(self)


class ActiveWarnings(Warnings):

    """
    Warnings for "active" user (i.e. not alumni)
    """

    def __init__(self, config, user_data):
        super().__init__(config, user_data)

    def _attribute_not_set(self, attr):
        user_value = self._user_data[attr]
        if user_value is None:
            return "{} is not set".format(attr)
        if user_value == "false":
            return "{} is not set".format(attr)
        return None

    def _firstname_not_set(self):
        return self._attribute_not_set("firstname")

    def _lastname_not_set(self):
        return self._attribute_not_set("lastname")

    def _ldap_not_set(self):
        return self._attribute_not_set("ldap")

    def _forms_status(self):
        forms_sent = self._attribute_not_set("forms_sent")
        if forms_sent is not None:
            return forms_sent
        forms_received = self._attribute_not_set("forms_received")
        if forms_received is not None:
            return forms_received
        is_website = self._attribute_not_set("is_website")
        return is_website

    def _expiration_not_set(self):
        return self._attribute_not_set("expiration")

    def _contract_not_set(self):
        return self._attribute_not_set("contract")

    def _type_not_set(self):
        return self._attribute_not_set("type")

    def get(self):
        """
        returns the list of warnings of the user
        """
        # this execute all private functions of
        # this class, each returning either None
        # (no warning) or a string (warning message)
        if self._user_data["contract"] == "alumni":
            return []
        return _get_warnings(self)


class TransitionWarnings(Warnings):
    """
    Warnings for active users for which
    the contract will soon expire
    """

    def __init__(self, config, user_data, threshold_days=10):
        super().__init__(config, user_data)
        expiration = self.user_data["expiration"]
        date = datetime.date(expiration.year, expiration.month, expiration.day)
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        self._expire_in = (date - now).days
        self._threshold_days = threshold_days

    def _no_closure_mail(self):
        if not user_data["closure_mail"]:
            return str(
                "contract expires soon, " "but no closure contract has been sent"
            )
        return None

    def get(self):
        """
        returns the list of warnings of the user
        """
        if self._expire_in > self.threshold_days:
            return []
        return _get_warnings(self)


class AlumniWarnings(Warnings):
    """
    Warnings for "inactive" user (i.e alumni)
    """

    def __init__(self, config, user_data):
        super().__init__(config, user_data)

    def _not_vaulted(self):
        if not self._user_data["vaulted"]:
            return "user is not (ldap) vaulted"
        return None

    def _no_forwarder(self):
        if not self._user_data["forwarder"]:
            return str("user email has not been replaced " "by a forwarder")
        return None

    def _not_set_as_alumni(self):
        if not self._user_data["website_alumni"]:
            return str("user not set as alumni " "in the website")
        return None

    def _has_hardware(self):
        if self._user_data["hardware"]:
            return str("user still has some" "hardware")
        return None

    def _has_licenses(self):
        if self._user_data["licenses"]:
            return str("user still has some" "licenses")
        return None

    def _assets_in_is_snipe(self):
        if not self._user_data["is_snipe_cleared"]:
            return str("user may still have some " "assets deployed to in is-snipe")

    def get(self):
        """
        returns the list of warnings of the user
        """
        if not self._user_data["contract"] == "alumni":
            return []
        return _get_warnings(self)


def all_warnings(self, config, user_data):
    """
    returns the list of warnings (str)
    of the user
    """
    warnings_classes = list(Warnings.__subclasses__())
    instances = [wc(config, user_data) for wc in warning_classes]
    warnings = []
    for instance in instances:
        warnings.extend(instance.get())
    return warnings

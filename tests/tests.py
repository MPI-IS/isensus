import json
import pytest
import tempfile
import pathlib
import isensus
from isensus import commands


@pytest.fixture
def test_data_file(request, scope="function"):
    """
    Fixture creating a single user json datafile
    at a temporary path.
    
    Returns
    -------
    path: Path
      absolute path to the temporary file
    """
    data = {
        "bmarley": {"userid": "bmarley", "firstname": "Bob", "lastname": "Marley"},
        "bmarlow": {"userid": "bmarlow", "firstname": "Benjamin", "lastname": "Marlow"},
    }
    f = tempfile.NamedTemporaryFile()
    p: pathlib.Path = pathlib.Path(f.name)
    with open(p, "w") as w:
        json.dump(data, w)

    yield p

    f.close()


def test_create_command(test_data_file):
    """
    Test the create command
    """

    data_path = test_data_file

    firstname = "Esther"
    lastname = "Boolo"
    userid = "eboolo"

    commands["create"](userid, firstname, lastname, path=data_path)

    with isensus.Data(path=data_path) as users:
        assert userid in users.keys()
        assert users[userid].userid == str(userid)
        assert users[userid].firstname == firstname
        assert users[userid].lastname == lastname


def test_remove_command(test_data_file):
    """
    Test the remove command
    """

    data_path = test_data_file

    with isensus.Data(path=data_path) as users:
        assert "bmarley" in users.keys()

    commands["remove"]("bmarley", path=data_path)

    with isensus.Data(path=data_path) as users:
        assert "bmarley" not in users.keys()


def test_ambiguous_user(test_data_file):
    """
    Test an AmbiguousUserError is raised
    when usertip is under specified
    """

    data_path = test_data_file

    with pytest.raises(isensus.AmbiguousUserError):
        commands["remove"]("bmar", path=data_path)

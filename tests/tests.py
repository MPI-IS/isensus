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
    data = {"bmarley": {"userid": "bmarley", "firstname": "Bob", "lastname": "Marley"}}
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

        
def test_maybe_me():

    users = {
        "emarlon": isensus.User.create_new("emarlon","Etienne","Marlon"),
        "emarlone": isensus.User.create_new("emarlone","Elody","Marlon"),
        "amarlo": isensus.User.create_new("amarlo","Antony","Marlo"),
        "efarlo": isensus.User.create_new("efarlo","Etienne","Farlo")
    }

    usertip = "emarl"
    assert users["emarlon"].maybe_me(usertip)
    assert users["emarlone"].maybe_me(usertip)
    assert not users["amarlo"].maybe_me(usertip)
    assert not users["efarlo"].maybe_me(usertip)

    usertip = "etien"
    assert users["emarlon"].maybe_me(usertip)
    assert not users["emarlone"].maybe_me(usertip)
    assert not users["amarlo"].maybe_me(usertip)
    assert  users["efarlo"].maybe_me(usertip)

    usertip = "marlo"
    assert users["emarlon"].maybe_me(usertip)
    assert users["emarlone"].maybe_me(usertip)
    assert users["amarlo"].maybe_me(usertip)
    assert not users["efarlo"].maybe_me(usertip)


def test_find_user():

    users = {
        "emarlon": isensus.User.create_new("emarlon","Etienne","Marlon"),
        "emarlone": isensus.User.create_new("emarlone","Elody","Marlon"),
        "amarlo": isensus.User.create_new("amarlo","Antony","Marlo"),
        "efarlo": isensus.User.create_new("efarlo","Etienne","Farlo")
    }

    with pytest.raises(isensus.UserNotFoundError):
        isensus.User.find_user(users,"emu")

    with pytest.raises(isensus.AmbiguousUserError):
        isensus.User.find_user(users,"emarl")

    with pytest.raises(isensus.AmbiguousUserError):
        isensus.User.find_user(users,"etien")

    user = isensus.User.find_user(users,"Anton")
    assert user == users["amarlo"]

    user = isensus.User.find_user(users,"farl")
    assert user == users["efarlo"]

    
def test_notes_and_warnings(test_data_file):

    data_path = test_data_file

    notes = (
        "this is note 1",
        "this is note 2"
    )

    warnings = (
        "this is warning 1",
        "this is warning 2"
    )

    for note in notes:
        commands["set"]("bmarley","notes",note,path=data_path)
    for warning in warnings:
        commands["set"]("bmarley","warnings",warning,path=data_path)
    
    with isensus.Data(path=data_path) as users:

        user = isensus.User.find_user(users,"bmarley")

        assert user.notes.get(0) == notes[0]
        assert user.notes.get(1) == notes[1]
        assert user.warnings.get(0) == warnings[0]
        assert user.warnings.get(1) == warnings[1]

        with pytest.raises(IndexError):
            user.notes.get(3)
        
        with pytest.raises(IndexError):
            user.warnings.get(3)

        
        
        
    


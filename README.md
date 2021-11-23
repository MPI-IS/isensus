![unit tests](https://github.com/MPI-IS/isensus/actions/workflows/tests.yaml/badge.svg)
![documentation](https://github.com/MPI-IS/isensus/actions/workflows/docs.yaml/badge.svg)


# isensus

isensus, contraction between '(MPI-)IS' and 'census' is a tool for the IT systems admins of the Max Planck Institute for Intelligent System to track the status of their users.

It is no much more than a fancy todo list reading a database of users encapsulated in a JSON formated file.


## Requirements

`Python 3.8` or higher.

## Installation

After cloning the repository:

```bash
cd isensus
pip install .
```

or directly:

```bash
pip install isensus
```

## Tests

To run the tests:

```bash
git clone https://github.com/MPI-IS/isensus.git
cd isensus
python3 -m pytest ./tests/tests.py
```

## Documentation

See: [https://mpi-is.github.io/isensus/](https://mpi-is.github.io/isensus/)

To build the documentation:

```bash
pip install sphinx sphinx-bootstrap-theme
git clone https://github.com/MPI-IS/isensus.git
cd isensus
cd doc
make html
```

The html documentation will be built in the `build` folder.

## Author

Vincent Berenz, Max Planck Institute for Intelligent Systems

## License

BSD-3-Clause (see LICENSE).


## Copyright

© 2021, Max Planck Society

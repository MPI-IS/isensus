# -*- coding: utf-8 -*-
#

import sys, os, pathlib

###########################
# adding the isensus code #
###########################

root_source_folder = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_source_folder))


#######################
# project information #
#######################

project = "isensus"
copyright = "2021, Max Planck Society"
author = "Vincent Berenz"


###################
# project version #
###################

from isensus.version import __version__

version = "v{}".format(__version__)


##################
# sphinx modules #
##################

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "myst_parser",
]
templates_path = []
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"
exclude_trees = ["build"]
pygments_style = "sphinx"


##############
# html theme #
##############

html_theme = "sphinx_rtd_theme"
html_theme_options = {}
html_static_path = []
htmlhelp_basename = "roboball2ddoc"


#####################
# api documentation #
#####################


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


autoclass_content = "both"

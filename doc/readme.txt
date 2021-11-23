To write the autodoc files, in a terminal run:
sphinx-apidoc -f -o source/ ../isensus/

To generate the html files, in a terminal:
make html && firefox ./build/html/index.html

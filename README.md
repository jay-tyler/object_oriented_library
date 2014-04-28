object_oriented_library
=======================

For a CodeFellows "code challenge".

Three versions. 
1. object_oriented_library.py
    This is a version stripped of example output.
2. version_for_command_line_doctest.py
    This version has a test() function at the bottom that can be checked
    via the command line, using
    
    python -m doctest version_for_command_line_doctest.py
    
    Out of the output, two tests will fail, only because doctest doesn't expect 
    the usage of a nested representation for library. (I've implemented library 
    to print its contained shelves as well as books).
3. version_for_replit.py
    repl.it doesn't give access to a file structure for doctest, so this is 
    a refactored version of #2 above with a narrated output at bottom.

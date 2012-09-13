#!/usr/bin/python -i
# Set logging to "info" to find where the problem was, and then modified html_converter.py

import logging
import os
import sys

# optional readline support
import readline
import rlcompleter

library_files = os.path.abspath(os.path.join( os.path.dirname(__file__), ".."))
sys.path.append(library_files)

from converter import open_and_parse_file

readline.parse_and_bind("tab: complete")

log = logging.getLogger()
log.setLevel(20) # INFO

open_and_parse_file("input.html")

# Could compare output to expect1.json, 
# but would need to modify _parse_string to return the parsed json 
# rather than just print it.


The repos contains the python code used to generate JSON from HTML. This comes in two flavors

1. an google app engine app, under the app_engine folder
1. a command line python script, see usage examples below

Command line Script Usage
---------

Checkout out this repos

    cd python

Get help on the options

  python converter.py -h

Read a string for HTML

  python converter.py -s "<div>hi</div>"

Scrape the contens of a remote URL, turn into JSON fastFrag, writes to stdout

  python converter.py -rq "http://www.slate.com/"

Read from a file

  python converter.py -f <path/to/file>




fastFrag Utils for project fastFrag.
More about fastFrag syntax <https://github.com/gregory80/fastFrag>

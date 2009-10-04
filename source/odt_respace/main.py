#!/usr/bin/env python

import sys
from optparse import OptionParser
import os.path
import shutil


#  odt-respace to be run even if not installed or in PYTHONPATH
try:
    import odt_respace
except ImportError:
    project_path = os.path.join(os.path.dirname(__file__), '..')
    sys.path.append(os.path.join(project_path, 'source'))

from odt_respace.unzip import UnZip
from odt_respace.respace import Respace
from odt_respace.zip import Zip

def run():
    usage = """usage: %prog INFILE OUTFILE

This program changes the number of spaces between sentences from 1 to 2 in
a Open Document Word Processing *.odt file.
    """

    parser = OptionParser(usage)
# @todo?
    #parser.add_option("-s", "--styles", dest="styles",
            #help="Comma delimited set of text style-names\nDefaults to 'Default'")
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.error("Incorrect number of arguments; please supply file to convert from and to.")
    if not os.path.exists(args[0]):
        parser.error("Input file does not exist.")

    with UnZip(args[0]) as zip_content_dir:
        respacer = Respace(zip_content_dir)
        with open(os.path.join(zip_content_dir, 'content.new.xml'), 'w') as newcontent:
            newcontent.write(respacer.run())
        os.rename(os.path.join(zip_content_dir, 'content.new.xml'),
                os.path.join(zip_content_dir, 'content.xml'))
        zipper = Zip(zip_content_dir, args[1])
        zipper.zip()


if __name__ == '__main__':
    run()

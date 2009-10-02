import sys
from optparse import OptionParser
import os.path


#  odt-respace to be run even if not installed or in PYTHONPATH
try:
    import odt_respace
except ImportError:
    project_path = os.path.join(os.path.dirname(__file__), '..')
    sys.path.append(os.path.join(project_path, 'source'))

def run():
    usage = """usage: %prog [options] INFILE OUTFILE

This program changes the number of spaces between sentences from 1 to 2 in
a Open Document Word Processing *.odt file.
    """

# create parser
    parser = OptionParser(usage)
    parser.add_option("-s", "--styles", dest="styles",
            help="Comma delimited set of text style-names\nDefaults to 'Default'")
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.error("Incorrect number of arguments; please supply file to convert from and to.")
    if not os.path.exists(args[0]):
        parser.error("Input file does not exist.")


if __name__ == '__main__':
    run()

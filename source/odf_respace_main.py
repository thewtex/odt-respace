import sys
from optparse import OptionParser
import os.path

CONVERSION_PATHS = {'odt':'docx',
        'docx':'odt'}

#  posac to be run even if not installed or in PYTHONPATH
try:
    import posac
except ImportError:
    project_path = os.path.join(os.path.dirname(__file__), '..')
    sys.path.append(os.path.join(project_path, 'source'))

def run():
    usage = """usage: %prog [options] FILENAME

This program converts files to/from the OASIS OpenDocument Format from/to
Microsoft Office OpenXML format.

At this time only word processing (*.docx, *.odt) are supported.
    """

# create parser
    parser = OptionParser(usage)
    parser.add_option("-o", "--output", dest="output_file",
            help="Output filename", metavar="FILENAME")
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error("Incorrect number of arguments; please supply file to convert.")
    if not os.path.exists(args[0]):
        parser.error("Input file does not exist.")

# decide what we are converting to
# @todo maybe in the future make it an option to force a conversion path
    converting_to = ''
    if args[0][-3:] in CONVERSION_PATHS:
        converting_to = CONVERSION_PATHS[args[0][-3:]]
    elif args[0][-4:] in CONVERSION_PATHS:
        converting_to = CONVERSION_PATHS[args[0][-4:]]
    else:
        parser.error("Unrecognized or unimplemented input file format.")

# define output file
    output_file = ''
    if options.output_file:
        output_file = option.output_file
    else:
        output_file = args[0].rpartition('.')[0] + '.' + converting_to
        

if __name__ == '__main__':
    run()

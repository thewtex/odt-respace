import os
import unittest
import sys
import tempfile

import odt_respace.main

tests_dir = os.path.dirname(__file__)

class TestMain(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

    def tearDown(self):
        for file in os.listdir(self.tempdir):
            os.remove(file)
        os.rmdir(self.tempdir)

    def testNoInput(self):
        argv = [sys.argv[0],]
        sys.argv = argv
        try:
            odt_respace.main.run()
        except SystemExit as e:
            if e.code is 2:
                return
            raise 
        self.fail("Did not catch no input file.")

    def testInputDoesNotExist(self):
        argv = [sys.argv[0],]
        argv.append('screwyfile.blah')
        argv.append('notherfile.bash')
        sys.argv = argv
        try:
            odt_respace.main.run()
        except SystemExit as e:
            if e.code is 2:
                return
            raise 
        self.fail("Did not catch non-existent input file.")


    def testOdtInput(self):
        test_file = os.path.join(tests_dir, 'data',
                'lorem_ipsum_oo_3.1.1_odf_1.1.odt')
        argv = [sys.argv[0],]
        argv.append(test_file)
        argv.append('lorem_ipsum_oo_3.1.1_odf_1.1_double_spaced.odt')
        sys.argv = argv
        odt_respace.main.run()



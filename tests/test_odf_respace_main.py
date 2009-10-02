import os
import unittest
import sys
import tempfile

import posac.posac_main

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
            posac.posac_main.run()
        except SystemExit as e:
            if e.code is 2:
                return
            raise 
        self.fail("Did not catch no input file.")

    def testInputDoesNotExist(self):
        argv = [sys.argv[0],]
        argv.append('screwyfile.blah')
        sys.argv = argv
        try:
            posac.posac_main.run()
        except SystemExit as e:
            if e.code is 2:
                return
            raise 
        self.fail("Did not catch non-existent input file.")


    def testOdtInput(self):
# @todo finish this test
        test_file = os.path.join(tests_dir, 'data',
                'lorem_ipsum_oo_3.1.1_odf_1.1.odt')
        argv = [sys.argv[0],]
        argv.append(test_file)
        sys.argv = argv
        posac.posac_main.run()

    def testDocxInput(self):
# @todo finish this test
        test_file = os.path.join(tests_dir, 'data',
                'lorem_ipsum_ms_word_2007.docx')
        argv = [sys.argv[0],]
        argv.append(test_file)
        sys.argv = argv
        posac.posac_main.run()


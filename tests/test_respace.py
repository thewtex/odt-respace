import os
import unittest
import sys
import tempfile

from odt_respace.respace import Respace
from odt_respace.unzip import UnZip

tests_dir = os.path.dirname(__file__)

class TestRespace(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

    def tearDown(self):
        for file in os.listdir(self.tempdir):
            os.remove(file)
        os.rmdir(self.tempdir)

    
    def testRespaceDefault1_1(self):
        test_file = os.path.join(tests_dir, 'data',
                'lorem_ipsum_oo_3.1.1_odf_1.1.odt')
        with UnZip(test_file) as zip_content_dir:
            respacer = Respace(zip_content_dir)
            respaced_content = respacer.run()
            self.assertEqual(respaced_content.count('<text:s/>'), 74)

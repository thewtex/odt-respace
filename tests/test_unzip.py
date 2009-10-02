import os
import unittest

from posac.posac_zipping.unzip import UnZip

tests_dir = os.path.dirname(__file__)

class TestUnZip(unittest.TestCase):

    def testOdtUnZip(self):
        zip_contents = [[['META-INF', 'Thumbnails', 'Configurations2'], 
                            ['settings.xml', 'meta.xml', 'styles.xml', 'content.xml',
                                'layout-cache', 'mimetype']],
                        [[], ['manifest.xml']],
                        [ [] , ['thumbnail.png'] ],             
                        [ ['images', 'toolbar', 'menubar', 'progressbar',
                            'popupmenu', 'floater', 'accelerator', 'statusbar']
                            , [] ],
                        [ ['Bitmaps'] , [] ],                   
                        [ [] , [] ],                            
                        [ [] , [] ],                            
                        [ [] , [] ],                            
                        [ [] , [] ],                            
                        [ [] , [] ],                            
                        [ [] , [] ],                            
                        [ [] , ['current.xml'] ],               
                        [ [] , [] ]
                            ]

        test_file = os.path.join(tests_dir, 'data',
                'lorem_ipsum_oo_3.1.1_odf_1.1.odt')
        with UnZip(test_file) as zip_content_dir:
            count = 0
            for root, dirs, files in  os.walk(zip_content_dir):
                self.assertEqual(dirs, zip_contents[count][0])
                self.assertEqual(files, zip_contents[count][1])
                count +=1

    def testDocxUnZip(self):
        zip_contents = [[ ['docProps', 'word', '_rels'] ,
            ['[Content_Types].xml'] ],
            [ [] , ['core.xml', 'app.xml'] ],
            [ ['theme', '_rels'] , ['styles.xml', 'webSettings.xml',
                'fontTable.xml', 'settings.xml', 'document.xml'] ],
            [ [] , ['theme1.xml'] ],
            [ [] , ['document.xml.rels'] ],
            [ [] , ['.rels'] ]]
        test_file = os.path.join(tests_dir, 'data',
                'lorem_ipsum_ms_word_2007.docx')
        with UnZip(test_file) as zip_content_dir:
            count = 0
            for root, dirs, files in  os.walk(zip_content_dir):
                self.assertEqual(dirs, zip_contents[count][0])
                self.assertEqual(files, zip_contents[count][1])
                count +=1

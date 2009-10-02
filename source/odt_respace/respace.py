# -*- coding: utf-8 -*-

import os
import re

class Respace():
    """Respace the data in the ODT content.xml."""

    def __init__(self, odt_dir):
        """Pass in directory with unzipped contents of the odt file.
        The directory should contain a file called *content.xml*."""
        self.odt_dir = odt_dir

    def run(self):
        with open(os.path.join(self.odt_dir, 'content.xml'), 'r') as file:
            content = file.read()

            respaced_content = re.sub(r'\.((?:“|”|"|&apos;|\')\s+|\s+)(?=(?:“|”|"|&apos;|\')\S|\S)',
                r'.\1<text:s/>',
                content)

        return respaced_content


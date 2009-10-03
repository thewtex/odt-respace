import os
import tempfile
from zipfile import ZipFile

class UnZip():
    """Unzip the given file into a temporary directory."""
    def __init__(self, input_file):
        self.input_file = input_file

    def unzip(self):
        self.zip_file = ZipFile(self.input_file, 'r')
        self.tempdir = tempfile.mkdtemp()
        self.zip_file.extractall(self.tempdir)
        return self.tempdir

    def cleanup(self):
        self.zip_file.close()
        for root, dirs, files in os.walk(self.tempdir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.tempdir)

    def __enter__(self):
        return self.unzip()

    def __exit__(self, *args):
        self.cleanup()
        return False

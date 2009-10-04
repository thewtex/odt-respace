import os
from zipfile import ZipFile, ZIP_DEFLATED

class Zip():
    """Zip up all the contents of a directory into the output file."""
    def __init__(self, input_directory, output_file):
      self.input_directory = input_directory
      self.output_file = output_file

    def zip(self):
      try:
        zip_file = ZipFile(self.output_file, 'w', ZIP_DEFLATED)
        for root, dirs, files in os.walk(self.input_directory, topdown=True):
          dir_prefix = root[len(os.path.commonprefix([self.input_directory, root]))+1:]
          if len(dirs) is 0 and len(files) is 0:
            zip_file.write(root, dir_prefix[:-1])
          else:
            for name in files:
              zip_file.write(os.path.join(root, name), os.path.join(dir_prefix, name))

      finally:
        zip_file.close()


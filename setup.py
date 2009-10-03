from distutils.core import setup

setup(name='odt-respace',
        description = 'Put two spaces after every sentence in an Open Document ODT file.',
        author = 'Matt McCormick (thewtex)',
        author_email = 'matt@mmmccormick.com',
        url = 'http://github.com/thewtex/odt-respace',
        license = 'Public Domain',
        packages = ['odt_respace'],
        package_dir = {'odt_respace': 'source/odt_respace'},
        scripts = ['source/scripts/odt-respace']
        )

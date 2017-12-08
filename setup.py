import versioneer
from setuptools import (setup, find_packages)


setup(name     = 'python_package_template',
      version  = versioneer.get_version(),
      cmdclass = versioneer.get_cmdclass(),
      author   = 'ADD AUTHOR',

      packages    = find_packages(),
      description = 'ADD DESCRIPTION',
      include_package_data = True,
)

from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'tensorflow-gpu==1.1.0'
]

setup(name='{{project_name}}',
      version='0.1',
      install_requires=REQUIRED_PACKAGES,
      packages=find_packages(),
      include_package_data=True)

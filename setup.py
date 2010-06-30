from distutils.core import setup

PACKAGE_NAME = 'howbig'

VERSION = '0.1.0'

setup(
    name=PACKAGE_NAME,
    author='Jonas Obrist',
    version=VERSION,
    scripts=['bin/howbig'],
)
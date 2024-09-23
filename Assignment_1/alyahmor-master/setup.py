#! /usr/bin/python
from setuptools import setup
from io import open
# to install type:
# python setup.py install --root=/


setup (name='alyahmor', version='0.1.5',
      description='Alyahmor Arabic Morphological Genrator for Python',
      author='Taha Zerrouki',
      author_email='taha. zerrouki@gmail .com',
      url='http://github.com/linuxscout/alyahmor/',
      license='GPL',
      package_dir={'alyahmor': 'alyahmor',},
      packages=['alyahmor'],
      include_package_data=True,
      install_requires=[ 'libqutrub>=1.0',
                        'pyarabic>=0.6.2',
                        "arramooz-pysqlite>=0.1",
      ],         
      package_data = {
        'alyahmor': ['doc/*.*', 'data/*.*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Natural Language :: Arabic',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Linguistic',
          ],
    );


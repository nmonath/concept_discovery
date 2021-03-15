#!/usr/bin/env python

from distutils.core import setup

setup(name='concept_disc',
      version='0.01',
      packages=['concept_disc'],
      install_requires=[
          "nltk",
          "absl-py",
          "python-dateutil",
	  "numpy",
          "scipy", "tqdm", "ipython", "cython", "higra", "scispacy",
          "sent2vec @ git+git://github.com/nmonath/sent2vec.git"
      ],
      package_dir={'kdcovid': 'concept_disc'}
      )

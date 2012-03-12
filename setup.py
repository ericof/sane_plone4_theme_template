# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name="yourtheme",
      version="0.0",
      description="A Plone theme",
      author="",
      author_email="",
      url="",
      install_require=["five.grok"],
      packages=['yourtheme'],
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.1",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: JavaScript",
          "Programming Language :: Python",
      ],
      license="GPL2",
      include_package_data=True,
      entry_points="""
        # -*- Entry points: -*-

        [z3c.autoinclude.plugin]
        target = plone
        """,
)

---
id: 30
title: Installing Sphinx
date: 2011-09-05T03:06:06+00:00
author: nadiahkristensen
layout: post
guid: http://nadiah.org/blog/?p=30
permalink: /2011/09/05/installing-sphinx/
rumputhijau_meta_box_input_image:
  - ""
restapi_import_id:
  - 596b21e75fcf8
original_post_id:
  - "30"
categories:
  - coding
---
Many times I have found someone's log of an installation of some new software incredibly useful, so here's my log from installing [Sphinx](http://sphinx.pocoo.org/) a while ago.

  1. First I followed the instructions [in the Sphinx tutorial here](http://www.sphinx-doc.org/en/1.5/tutorial.html), namely: 
      1. Installed using sphinx-quickstart
      2. sphinx-build -b html sourcedir builddir
      3. make html
    This gave me a basic html page with no content
    
  1. I Created a python program with some rst in the docstrings, called [intercept.py](https://s3.amazonaws.com/nadiah.org/toolfiles/intercept.py), which went into the source directory
  1. I added these lines to ./source/index.rst:  
       1. `.. automodule:: intercept`
       1. `:members:` 
  1. I also added the following lines to ./source/conf.py: 
          * `sys.path.insert(0, os.path.abspath('.'))`: So it could find intercept.py
          * `extensions = ['sphinx.ext.autodoc','sphinx.ext.pngmath']`: So maths would work
  1. I ran make html and got much of the documentation into the html file, but ... 
  1. I got an error about "LaTeX Error: File \`utf8x.def' not found." So I installed texlive-latex-extra as per [the directions on stackoverflow](http://stackoverflow.com/questions/3952787/sphinx-ext-pngmath-raise-an-error-when-i-try-a-simple-expression)
  1. I had to modify the intercept.py file before it would rerun it  properly.
  1. It couldn't find dvipng so I installed it
  1. Then success! A "make html" worked and the file in build/html/index.html now has what it needs</ol> 

A best-practice example of how to use Sphinx can be found [on github here](https://github.com/mitsuhiko/werkzeug/tree/master/docs).

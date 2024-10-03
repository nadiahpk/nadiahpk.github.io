#!/bin/bash

set -e
set -x

rm -fr $GEM_HOME/*

git rm -f Gemfile.lock || true
rm -f Gemfile.lock

gem install github-pages
gem install jekyll jekyll-paginate bundler sassc
bundle install

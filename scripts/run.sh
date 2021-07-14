#!/bin/sh

# bundle exec jekyll serve

rm _site/* -r --force
bundle exec jekyll serve --increment

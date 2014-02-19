#! /bin/bash

# Update the repo
git checkout master
git pull

# Build the theme
make html

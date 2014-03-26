#! /bin/bash

# Update the repo
git checkout master
git pull -q --ff-only

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
make publish

# Disable venv
deactivate

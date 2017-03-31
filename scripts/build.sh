#! /bin/bash

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi

source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build the site
# make rsync_copy first calls make publish, which builds using publishconf.py
make rsync_copy

# make sure the build succeeded before continuing, otherwise script exits 0

if [ $? -eq 0 ]
then
  deactivate
else
  deactivate
  exit 1
fi

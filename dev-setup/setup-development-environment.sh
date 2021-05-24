#!/bin/bash
# set up a minimal virtualenv for scikit-learn development in the current directory
# (C) 2021 Norbert Preining
# Public Domain
#
# Change the github_user to your username under which there is a fork
# of the scikit-learn repository

set -e
set -o pipefail

# setup and activate a virtual environment

venv_name=sklearn-dev-setup
github_user=scitkit-devsprint-japan

if [ -x "$(command -v pyenv)" ] ; then
  # use pyenv
  if pyenv virtualenvs | grep -q $venv_name ; then
    echo "There is already a pyenv virtualenv $venv_name, using it!"
  else
    pyenv virtualenv $venv_name
  fi
  pyenv activate $venv_name
else
  # use plain venv
  if [ -d $venv_name.venv ] && [ -x $venv_name.venv/bin/activate ] ; then
    echo "There seems to be already a venv in $venv_name.venv, using it!"
  else
    python -m venv $venv_name.venv
  fi
  source $venv_name.venv/bin/activate
fi


# update pip
pip install -U pip

# install packages necessary to dev-install scikit-learn
pip install wheel numpy scipy

# install scikit learn deps
pip install cython pytest pytest-cov flake8 mypy

# clone scikit-learn fork
git clone git@github.com:$github_user/scikit-learn.git

# cd into the newly checked out directory
cd scikit-learn

# add upstream remote
git remote add upstream git://github.com/scikit-learn/scikit-learn.git

# install scikit-learn for development
pip install --no-build-isolation --editable .

# install further useful packages
pip install pandas matplotlib

# test installed version
python -c "import sklearn; sklearn.show_versions()"

# checkout a feature branch
git checkout -b some-feature

# hack away!
echo "No hack away for a better scikit-learn!"


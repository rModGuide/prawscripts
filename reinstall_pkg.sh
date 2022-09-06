#!/bin/bash

python3 setup.py sdist bdist_wheel
pip3 install --force-reinstall ./dist/*.whl

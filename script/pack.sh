#!/bin/bash
pushd $PWD
cd `dirname $0`

cd ../
python setup.py sdist bdist_wheel

popd
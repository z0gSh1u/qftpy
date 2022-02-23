#!/bin/bash
pushd $PWD
cd `dirname $0`

cd ../test

python utils.test.py

# Add more later.

popd
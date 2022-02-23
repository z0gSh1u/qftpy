#!/bin/bash
pushd $PWD
cd `dirname $0`

cd ../docs
make clean
make singlehtml
touch .nojekyll

popd
@ECHO OFF

pushd %cd%
cd %~dp0

cd ../docs
call make clean
call make singlehtml
echo > .nojekyll

popd
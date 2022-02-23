@ECHO OFF

pushd %cd%
cd %~dp0

cd ../test

call python utils.test.py
REM Add more later.

popd
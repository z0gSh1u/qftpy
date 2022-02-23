@ECHO OFF

pushd %cd%
cd %~dp0

cd ../
python setup.py sdist bdist_wheel

popd
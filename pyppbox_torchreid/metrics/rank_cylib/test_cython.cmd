@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python test_cython.py


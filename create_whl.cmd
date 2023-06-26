@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python -m pip install --upgrade pip
pip install wheel build
python -m build --wheel
pause

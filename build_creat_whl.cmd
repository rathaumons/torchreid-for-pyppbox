@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python -m pip install --upgrade pip
pip install build
call pyppbox_torchreid\metrics\rank_cylib\build.cmd
call pyppbox_torchreid\metrics\rank_cylib\test_cython.cmd
python -m build --wheel --skip-dependency-check --no-isolation
pause
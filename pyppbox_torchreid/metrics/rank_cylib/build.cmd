@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python setup.py build_ext --inplace
ren "rank_cy*.pyd" "rank_cy.pyd"

@echo off
title Run/Python checker
python --version 2>NUL
if errorlevel 1 goto errorNoPython
start main.py
exit

goto :EOF

:errorNoPython
echo/
echo Error^: Python not installed
echo Install python via this link: https://www.python.org
pause


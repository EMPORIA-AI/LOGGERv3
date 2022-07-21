@echo off
:main
cls
q server.py routes\*.py objects\*.py common\__init__.py
rem python -m cProfile -s ncalls server.py | list /s
rem hypercorn server.py
pause
if errorlevel 1 goto end
goto main
:end

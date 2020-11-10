@echo off
set /p Input=Input scriptname: 
cmd /k py parser.py parse %Input%
exit
@echo off
setlocal

goto :MAIN

:FUNC
echo ARG1: %~1 ARG2: %~2
goto :eof

:MAIN
call :FUNC hello1 world1
call :FUNC hello2 world2

echo Back from func

@echo off
setlocal


call :SayHello
echo Back in main script
goto :eof

:SayHello
echo Hello!
exit /b

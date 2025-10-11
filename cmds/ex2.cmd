@echo off
setlocal


call :FuncA Hello
call :FuncB World

echo Back in main script
goto :eof

echo should be skipped

:FuncA
echo FuncA called with: %~1
exit /b

:FuncB
echo FuncB called with: %~1
exit /b

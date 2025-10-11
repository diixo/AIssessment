@echo off
setlocal


:: Jump to main entry point
goto :MAIN

:: --------------------
:FuncA
echo [FuncA] arg: %~1, arg: %~2
exit /b

:: --------------------
:FuncB
echo [FuncB] arg: %~1, arg: %~2
exit /b

:: -------- Entry point
:MAIN
echo === start MAIN ===

call :FuncA Hello1 world1
call :FuncB Hello2 world2

echo === finish MAIN ===

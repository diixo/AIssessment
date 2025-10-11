@echo off
setlocal


:: Jump to main entry point
goto :MAIN

:: --------------------
:FuncA
echo [FuncA] arg: %~1
exit /b

:: --------------------
:FuncB
echo [FuncB] arg: %~1
exit /b

:: -------- Entry point
:MAIN
echo === start MAIN ===

call :FuncA Hello
call :FuncB World

echo === finish MAIN ===

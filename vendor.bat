@echo on
F:
cd  F:\Info\Python\vendors
if "%~2"=="" (
C:\Python27\python F:\Info\Python\vendors\vendor.py -v %1 
) else (
	C:\Python27\python F:\Info\Python\vendors\vendor.py -v %1 -a %2
)


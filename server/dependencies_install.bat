@ECHO off
setLocal
rem dependencies_install.bat - One stop installer for the required libraries for this application.
SET header=------------------------------------------------
SET tagger=*****

:INIT
rem Checking if python is properly installled and its path is appropriately set.
ECHO %tagger% CHECKING PYTHON AVAILABIITY! %tagger%
ECHO %header%
ECHO.
python.exe --version >NUL 2>&1
IF ERRORLEVEL 1 GOTO MISSINGPYTHON
ECHO %tagger% Detected Python Version: %tagger%
FOR /F "tokens=*" %%a IN ('python --version') DO SET pyVersion=%%a
GOTO UPDATEPIP
GOTO EXITBATCH

:UPDATEPIP
rem Update PIP if needed
ECHO.
ECHO %tagger% UPDATING PIP! %tagger%
ECHO %header%
python -m pip install --upgrade pip
IF ERRORLEVEL 1 GOTO UPDATEFAILED
GOTO INSTALLLIBRARIES

:INSTALLLIBRARIES
rem Installing the dependent libraries
ECHO.
ECHO %tagger% INSTALLING NUMPY! %tagger%
ECHO %header%
pip install -U numpy
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% NUMPY library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING SCIPY! %tagger%
ECHO %header%
pip install -U scipy
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% SCIPY library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING MATPLOTLIB! %tagger%
ECHO %header%
pip install -U matplotlib
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% MATPLOTLIB library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING PANDAS! %tagger%
ECHO %header%
pip install -U pandas
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% PANDAS library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING STATSMODELS! %tagger%
ECHO %header%
pip install -U statsmodels
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% STATSMODELS library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING OPENBLENDER ! %tagger%
ECHO %header%
pip install -U OpenBlender
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% OPENBLENDER library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING WORDCLOUD! %tagger%
ECHO %header%
pip install -U wordcloud
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% WORDCLOUD library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING SEABORN! %tagger%
ECHO %header%
pip install -U seaborn
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% SEABORN library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING PILLOW! %tagger%
ECHO %header%
pip install pillow
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% PILLOW library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING DJANGO! %tagger%
ECHO %header%
pip install django
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% DJANGO library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING GOOGLE-COLAB! %tagger%
ECHO %header%
pip install google-colab
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% GOOGLE-COLAB library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING FILES! %tagger%
ECHO %header%
pip install files
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% FILES library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING GOOGLE-API-PYTHON-CLIENT! %tagger%
ECHO %header%
pip install --upgrade google-api-python-client
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% GOOGLE-API-PYTHON-CLIENT library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING GEOS! %tagger%
ECHO %header%
pip install geos
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% GEOS library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING DJANGO-CORS-HEADERS! %tagger%
ECHO %header%
pip install django-cors-headers
python -m pip install django-cors-headers
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% DJANGO-CORS-HEADERS library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING IMAGE-IO! %tagger%
ECHO %header%
pip install imageio
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% IMAGE-IO library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING DJANGO-REST-FRAMEWORK! %tagger%
ECHO %header%
conda install -c conda-forge djangorestframework
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% DJANGO-REST-FRAMEWORK library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING PROJ! %tagger%
ECHO %header%
conda install -c conda-forge proj
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% PROJ library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING PROJ-DATA! %tagger%
ECHO %header%
conda install -c conda-forge proj-data
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% PROJ-DATA library %tagger%
	GOTO INSTALLATIONERROR
)

ECHO.
ECHO %tagger% INSTALLING BASEMAP! %tagger%
ECHO %header%
conda install -c anaconda basemap
conda install -c conda-forge basemap
IF ERRORLEVEL 1 (
	ECHO Failed to install %tagger% BASEMAP library %tagger%
	GOTO INSTALLATIONERROR
)
GOTO EXITBATCH

:MISSINGPYTHON
rem Python is not found. Showing message and exiting the batch execution.
ECHO.
ECHO %tagger% MISSING PYTHON! %tagger%
ECHO %header%
ECHO Python.exe either not installed or PATH is not set.
ECHO Manually install python and execute this batch file again.
ECHO %header%
GOTO EXITBATCH

:UPDATEFAILED
rem update of PIP failed.
ECHO.
ECHO %tagger% PIP UPDATE FAILED! %tagger%
ECHO %header%
ECHO 'pip' update failed. Do you want to continue with Installing the libraries?
SET /P option=Press 'Y' for YES and 'N' for NO:
IF %input% EQU Y (
	ECHO %tagger% Initiating the installation of dependent libraries. %tagger%
	GOTO INSTALLLIBRARIES
) ELSE IF %input% EQU N (
	ECHO %tagger% Terminating the installation of dependent libraries. %tagger%
	GOTO EXITBATCH
) ELSE (
	ECHO %tagger% Incorrect Option. Please select proper option[Y or N].
	GOTO UPDATEFAILED
)
GOTO EXITBATCH

:INSTALLATIONERROR
rem Installation of libraries failed. Showing message and reqesting for retry.
ECHO.
ECHO If the installation is not successful, check if version is greater than 3.0 or not.
ECHO or simply install python and try again.
ECHO.
GOTO RETRY

:RETRY
rem Requesting User for attempting again with the installation of the libraries. Show apt messages. Also accept input from user.
ECHO %header%
ECHO ERROR occured while installing dependent libraries.
ECHO Would you prefer re-attempting on the dependency installation?
SET /P input=Press 'Y' for YES and 'N' for NO:
IF %input% EQU Y (
	ECHO %tagger% Re-initiating the installation of dependent libraries. %tagger%
	GOTO INSTALLLIBRARIES
) ELSE IF %input% EQU N (
	ECHO %tagger% Terminating the installation of dependent libraries. %tagger%
	GOTO EXITBATCH
) ELSE (
	ECHO %tagger% Incorrect Option. Please select proper option[Y or N].
	GOTO RETRY
)
GOTO EXITBATCH


:EXITBATCH
ECHO %tagger% Exiting batch execution %tagger%
pause
endlocal

call docker build -t nono %WORKSPACE_CICD%\container
call docker run -v %WORKSPACE_CICD%:/home -it nono bash


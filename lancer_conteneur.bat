call docker build -t nono %WORKSPACE_CICD%\container
call docker run -p 127.0.0.1:5000:5000 -v %WORKSPACE_CICD%:/home -it nono bash


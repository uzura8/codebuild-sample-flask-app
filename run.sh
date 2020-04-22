docker build -t codebuild-sample-flask-app .
docker stop codebuild-sample-flask-app_con
docker rm codebuild-sample-flask-app_con
docker run -it --name codebuild-sample-flask-app_con codebuild-sample-flask-app:latest /bin/bash

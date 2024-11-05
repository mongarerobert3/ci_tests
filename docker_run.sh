docker run -d \
    --name jenkins-python \
    -p 8080:8080 \
    -v jenkins-data:/var/jenkins_home \
    -v /D:/Job/ci_tests/./ci_testing/ci_tests/test.py \
    -v /var/run/docker.sock:/var/run/docker.sock \
    jenkins
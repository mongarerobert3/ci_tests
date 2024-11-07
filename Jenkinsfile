pipeline {
    agent any
    environment {
        // Define the Slack credential ID
        SLACK_CREDENTIAL_ID = 'robert-mnj5732'
        // Define the Slack channel where notifications will be sent
        SLACK_CHANNEL = 'testing'
    }
    stages {
        stage('Setup environment') {
            steps {
                // Setup a virtual environment and install dependencies
                script {
                    sh 'pip install -r ./ci_testing/requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
                        // Run tests, if they fail, this will throw an exception
                        sh 'pytest ./ci_testing/tests/test.py'
                    } catch (Exception e) {
                        // Explicitly mark the build as failed
                        currentBuild.result = 'FAILURE'
                        throw e // Rethrow the exception to stop the pipeline
                    }
                }
            }
        }
    }
    post {
        failure {
            // This block will only run if the pipeline fails
            slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'\nConsole output: ${env.BUILD_URL}console")
        }
    }
}

pipeline {
    agent any
    stages {
        stage('Checkout') {
                    steps {
                        // Get the latest code from the source control
                        checkout scm
                    }
                }

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
            // Run the unit tests with the unittest module or pytest
            script {
                try {
                    sh 'pytest ./ci_testing/tests/test.py'
                } catch (Exception e) {
                    // If tests fail, mark the build as failed
                    currentBuild.result = 'FAILURE'
                    throw e // Re-throw the exception to stop the pipeline
                }
            }
        }
    }
    }
    post {
        failure {
            // This will run only if the pipeline fails
            slackSend (
                channel: 'testing',
                color: 'danger',
                message: "Unit tests failed in Jenkins build ${env.BUILD_NUMBER}: ${env.BUILD_URL}"
            )
        }
    }
}

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
            // Sends a notification to the specified Slack channel if a test fails
            slackSend(channel: 'testing', color: 'danger', message: "TESTS FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}")

            // Send detailed log output to Slack (optional)
            slackSend(channel: 'testing', color: 'warning', message: "${env.BUILD_URL}consoleText")

            mail to: 'mongarerobert3@gmail.com',
            subject: "Failed Pipeline: ${env.JOB_NAME} build ${env.BUILD_NUMBER}",
            body: "Something is wrong with the build ${env.BUILD_URL}"
        }
    }
}
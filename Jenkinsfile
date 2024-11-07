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
                sh 'pytest ./ci_testing/tests/test.py || echo "Tests failed!" > test-failure.log'
            }
        }
    }
    post {
        failure {
            // Send a notification to Slack on test failure
            slackSend(
                channel: env.SLACK_CHANNEL,
                color: 'danger',
                message: "TEST FAILURE: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                tokenCredentialId: env.SLACK_CREDENTIAL_ID,
                attachments: [
                    [
                        "fallback": "Test failure log",
                        "text": "Test failure details available",
                        "file": "test-failure.log"
                    ]
                ]
            )
        }
    }
}

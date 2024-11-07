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
            emailext (
                subject: "FAILED: Unit tests in Jenkins build ${env.BUILD_NUMBER}",
                body: "Unit tests failed in Jenkins build ${env.BUILD_NUMBER}. Please check the build logs at: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'mongarerobert3@gmail.com'
            )
        }
    }
}

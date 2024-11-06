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
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
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
        always {
            // Clean up the workspace to be used for the next run
            cleanWs()
        }
    }
}
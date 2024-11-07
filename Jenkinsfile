pipeline {
    agent any
    
    // Define the stages of the pipeline
    stages {
        // Stage for checking out the latest code from the source control
        stage('Checkout') {
            steps {
                // Checkout the code from the source control management (SCM) configured in Jenkins
                checkout scm
            }
        }

        // Stage to set up the environment and install necessary dependencies
        stage('Setup environment') {
            steps {
                // Use a script block to install the dependencies from requirements.txt
                script {
                    // Install Python dependencies listed in the requirements.txt file
                    sh 'pip install -r ./ci_testing/requirements.txt'
                }
            }
        }

        // Stage to run unit tests
        stage('Test with Coverage') {
            steps {
                sh 'coverage run -m pytest ./ci_testing/tests/test.py' // Running tests with coverage
                sh 'coverage html -d coverage_html' // Generating HTML coverage report
            }
        }

    }

    post {
        always {
            // Archive the generated HTML coverage report
            archiveArtifacts artifacts: 'coverage_html/**/*', fingerprint: true
        }
    }
}

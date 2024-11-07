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

        // Stage to run unit tests with coverage
        stage('Test with Coverage') {
            steps {
                // Run pytest with coverage
                sh 'coverage run -m pytest ./ci_testing/tests/test.py'
                
                // Generate the HTML coverage report in the 'coverage_html' directory
                sh 'coverage html -d coverage_html'
                sh 'ls -R coverage_html'
            }
        }
    }

    post {
        always {
            // Archive the HTML coverage report
            archiveArtifacts artifacts: 'coverage_html/**/*', fingerprint: true
        }
    }
}

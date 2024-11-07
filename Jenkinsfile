pipeline {
    agent any

    stages {
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
        stage('Run Tests with Coverage') {
            steps {
                sh '''
                # Create an environment variable for the coverage report directory
                COVERAGE_DIR=coverage_report

                # Run tests with coverage
                coverage run -m pytest

                # Generate HTML report
                coverage html -d $COVERAGE_DIR

                # Fail the build if code coverage is below a certain threshold, e.g., 80%
                coverage report --fail-under=80
                '''
            }
        }
    }

    post {
        always {
            // Archive the coverage report for Jenkins to display
            archiveArtifacts artifacts: 'coverage_report/**/*'
        }
    }
}
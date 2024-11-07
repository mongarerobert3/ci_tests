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
        stage('Test with Coverage') {
            steps {
                sh 'coverage run -m pytest ./ci_testing/tests/test.py'
                sh 'coverage html -d coverage_html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'coverage_html/**/*', fingerprint: true
            // Optional: If you are using a plugin like Cobertura, you can publish the coverage report
            // cobertura coberturaReportFile: 'coverage.xml'
        }
    }
}
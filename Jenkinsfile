// Jenkinsfile

pipeline {
    agent any // This pipeline can run on any available agent
    
    stages {
        stage('Checkout') {
            steps {
                // Get the latest code from the repository
                git 'https://github.com/mongarerobert3/ci_tests'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                // Use a virtualenv or a similar tool to setup your Python environment
                script {
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                // Execute the unit tests, the pipeline will fail if any test fails
                script {
                    sh 'pytest ./ci_testing/tests/test.py'
                }
            }
        }
    }
    
    post {
        always {
            // Clean up after the pipeline runs
            cleanWs()
        }
        success {
            // Actions to perform on success
            echo 'Tests passed successfully!'
        }
        failure {
            // Actions to perform if the pipeline fails
            echo 'Tests failed. Check the logs for details.'
        }
    }
}
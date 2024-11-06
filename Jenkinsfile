pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Retrieves the most recent code from the repository
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                // Install necessary dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Execute Python tests
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            // Post-actions like cleaning up, sending notifications, etc.
        }
        failure {
            // Actions to perform if the pipeline fails
            // e.g., send an email to the development team
        }
    }
}
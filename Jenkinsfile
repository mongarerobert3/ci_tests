pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt' // Adjust for your project
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest tests'  // Adjust for your project test directory
                }
            }
        }
    }

    post {
        success {
            // Actions to perform if the pipeline is successful
            echo 'The pipeline succeeded!'
        }
        failure {
            // Actions to perform if the pipeline fails
            echo 'The pipeline failed!'
        }
    }
}

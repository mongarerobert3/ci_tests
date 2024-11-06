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
                    // Ensure Python and pip are installed
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python3 python3-pip'  // Install Python3 and pip

                    // Install dependencies from requirements.txt
                    sh 'pip3 install -r requirements.txt'  // Ensure pip3 is used for Python3
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest tests'  // Run tests
                }
            }
        }
    }

    post {
        success {
            echo 'The pipeline succeeded!'
        }
        failure {
            echo 'The pipeline failed!'
        }
    }
}

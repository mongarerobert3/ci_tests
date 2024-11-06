pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest ci_tests'
            }
        }
    }
    post {
        always {
            junit '**/TEST-*.xml' // This step collects test reports
        }
    }
}
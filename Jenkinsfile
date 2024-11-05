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
                sh 'pytest /var/jenkins_home/workspace/ci_testing/test.py'
            }
        }

    }
    post {
        always {
            junit '**/TEST-*.xml' // This step collects test reports
        }
    }
}





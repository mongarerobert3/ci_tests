pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


    }
    post {
        always {
            junit '**/TEST-*.xml' // This step collects test reports
        }
    }
}





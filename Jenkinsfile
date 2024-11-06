pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run your tests
                    sh 'python -m unittest discover -s . -p test*.py'
                }
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Jenkins Build Success: ${currentBuild.fullDisplayName}",
                body: "The Jenkins build ${currentBuild.fullDisplayName} has successfully completed.",
                to: 'mongarerobert3@gmail.com' // Add your email address
            )
        }
        failure {
            emailext(
                subject: "Jenkins Build Failed: ${currentBuild.fullDisplayName}",
                body: "The Jenkins build ${currentBuild.fullDisplayName} has failed.",
                to: 'mongarerobert3@gmail.com' // Add your email address
            )
        }
    }
}

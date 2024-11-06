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
                script {
                    // Ensure Python runs from the correct directory
                    dir('ci_testing/ci_tests') {
                        // Ensure we're in the correct directory, and run unittest
                        sh '''
                            # Ensure that we can discover and run the tests
                            python -m unittest discover -s . -p "test*.py"
                        '''
                    }
                }
            }
        }
    }
    post {
        failure {
            emailext(
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' failed.</p>
                         <p>Check console output at '<a href="${env.BUILD_URL}">${env.BUILD_URL}</a>'</p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'mongarerobert3@gmail.com'
            )
        }
    }
}
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
                    // Ensure we're in the correct directory (ci_testing/ci_tests)
                    dir('ci_testing/ci_tests') {
                        // Run unittest with XML output
                        sh '''
                            python -m unittest discover -s . -p "test*.py" > result.xml
                        '''
                    }
                }
            }
        }
    }
    post {
        failure {
            emailext(
                subject: "FAILED: ${currentBuild.fullDisplayName}",
                body: """<p>Something went wrong with the build:</p>
                 <p>Job: ${env.JOB_NAME}<br>
                 Build Number: ${env.BUILD_NUMBER}<br>
                 Console Output: <a href="${env.BUILD_URL}console">Console Output</a></p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'mongarerobert3@gmail.com',
                from: 'courtewampedsoftwares@gmail.com'
            )
        }
    }
}

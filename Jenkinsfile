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
        success {
            emailext(
                subject: "Jenkins Build Success: ${currentBuild.fullDisplayName}",
                body: "The Jenkins build ${currentBuild.fullDisplayName} has successfully completed.",
                to: 'mongarerobert3@gmail.com', // Add your email address
                from: 'Turing-Test@gmail.com'
            )
        }
        failure {
            emailext(
                subject: "Jenkins Build Failed: ${currentBuild.fullDisplayName}",
                body: "The Jenkins build ${currentBuild.fullDisplayName} has failed.",
                to: 'mongarerobert3@gmail.com', // Add your email address
                from: 'Turing-Test@gmail.com'
            )
        }
    }

}
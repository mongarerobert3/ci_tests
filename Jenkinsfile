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
                        // Run unittest with XML output
                        sh '''
                            python -m unittest discover -s ci_tests -p "test*.py"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            junit '**/result.xml'  // Collect the XML test report
        }
    }
}

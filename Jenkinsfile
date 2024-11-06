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

    
}

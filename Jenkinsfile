pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        checkout scm
                        echo 'Checkout successful'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        echo "Checkout failed: ${e.getMessage()}"
                        throw e
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
                        // Ensure we're in the correct directory (ci_testing/ci_tests)
                        dir('ci_testing/ci_tests') {
                            // Run unittest with XML output
                            sh '''
                                python -m unittest discover -s . -p "test*.py" > result.xml
                            '''
                            echo 'Tests ran successfully'
                        }
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        echo "Test execution failed: ${e.getMessage()}"
                        throw e
                    }
                }
            }
        }
    }

    post {
        failure {
            mail to: 'youremail@example.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}"
        }
    }
}


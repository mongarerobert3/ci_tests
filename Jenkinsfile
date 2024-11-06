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
            emailext(
                subject: "FAILED: ${currentBuild.fullDisplayName}",
                body: """<p>Something went wrong with the build:</p>
                 <p>Job: ${env.JOB_NAME}<br>
                 Build Number: ${env.BUILD_NUMBER}<br>
                 Console Output: <a href="${env.BUILD_URL}console">Console Output</a></p>""",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                to: 'youremail@example.com'
            )
        }
    }
}



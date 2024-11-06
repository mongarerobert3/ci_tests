pipeline {
    agent any
    triggers {
        // Trigger on push to specific branches or file patterns
        pollSCM('H/5 * * * *', filter: 'H/5 * * * *', ignorePostCommitHooks: false)
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
        success {
            emailext(
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' was successful.</p>
                         <p>Check console output at '<a href="${env.BUILD_URL}">${env.BUILD_URL}</a>'</p>""",
                to: 'mongarerobert3@gmail.com'
            )
        }
        failure {
            emailext(
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' failed.</p>
                         <p>Check console output at '<a href="${env.BUILD_URL}">${env.BUILD_URL}</a>'</p>""",
                to: 'failure-email@example.com'
            )
        }
        unstable {
            emailext(
                subject: "UNSTABLE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' is unstable.</p>
                         <p>Check console output at '<a href="${env.BUILD_URL}">${env.BUILD_URL}</a>'</p>""",
                to: 'unstable-email@example.com'
            )
        }
        aborted {
            emailext(
                subject: "ABORTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' was aborted.</p>
                         <p>Check console output at '<a href="${env.BUILD_URL}">${env.BUILD_URL}</a>'</p>""",
                to: 'aborted-email@example.com'
            )
        }
    }
}
pipeline {
    agent any
    options {
        // Set a quiet period of 1 hour
        quietPeriod(60)
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Selective Tests') {
            steps {
                // Use a script to determine which tests to run based on changes
                script {
                    def affectedTests = sh(
                        script: 'python -m pytest --collect-only | grep affected_test',
                        returnStdout: true
                    ).trim()
                    sh "python -m pytest ${affectedTests}"
                }
            }
        }
        // Other stages...
    }
    post {
        always {
            junit '**/TEST-*.xml'
        }
        failure {
            script {
                // Send rich notifications with links to the failed stage
                emailext (
                    subject: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' failed",
                    body: """<p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' failed at stage '${env.STAGE_NAME}'.</p>
                             <p>Check console output at '<a href="${env.BUILD_URL}">${env.BUILD_URL}</a>'</p>""",
                    to: 'dev-team@example.com'
                )
                // Send notifications to Slack
                slackSend (color: 'danger', message: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' failed at stage '${env.STAGE_NAME}'. Check console output at ${env.BUILD_URL}")
            }
        }
    }
}
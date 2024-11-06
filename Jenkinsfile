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
                // Running tests in the ci_tests folder, ensuring test discovery for the 'test.py' file
                sh 'python -m unittest discover -s ci_tests -p "test.py"'
            }
        }
    }

    post {
        always {
            // Collecting the test results, ensure your test framework generates the XML reports
            junit '**/TEST-*.xml'  // Adjust the pattern if your test reports are generated with different names
        }
    }
}

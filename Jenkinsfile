pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Eb1n-Babu/Jenkins-demo-v2'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_hello.py'
            }
        }
    }

    post {
        success {
            echo '✅ Build and tests passed!'
        }
        failure {
            echo '❌ Build or tests failed.'
        }
    }
}
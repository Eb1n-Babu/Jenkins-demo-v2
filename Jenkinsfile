pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                git 'https://github.com/Eb1n-Babu/Jenkins-demo-v2.git'
            }
        }

        stage('Build') {
            steps {
                // Set up a Python virtual environment
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install pytest'
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest
                sh '. venv/bin/activate && pytest tests/test_app.py'
            }
        }
    }

    post {
        success {
            echo '✅ Build and tests passed successfully!'
        }
        failure {
            echo '❌ Build or tests failed.'
        }
    }
}
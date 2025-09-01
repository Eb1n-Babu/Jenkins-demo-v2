pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Explicitly checkout the 'main' branch
                git branch: 'main', url: 'https://github.com/Eb1n-Babu/Jenkins-demo-v2.git'
            }
        }
        stage('Build') {
            steps {
                // Set up a Python virtual environment (Windows-compatible)
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install pytest'
            }
        }
        stage('Test') {
            steps {
                // Run tests using pytest (Windows-compatible)
                bat 'venv\\Scripts\\activate && pytest tests/test_app.py'
            }
        }
    }
    post {
        success {
            echo 'Build and tests passed successfully!'
        }
        failure {
            echo 'Build or tests failed.'
        }
    }
}
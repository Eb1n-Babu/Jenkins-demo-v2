pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the 'main' branch explicitly
                git branch: 'main', url: 'https://github.com/Eb1n-Babu/Jenkins-demo-v2.git'
            }
        }
        stage('Build') {
            steps {
                // Use full path to python executable (adjust path as needed)
                bat '"C:\\Users\\ebinb\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'

                bat 'venv\\Scripts\\activate && venv\\Scripts\\pip.exe install pytest'
            }
        }
        stage('Test') {
            steps {
                // Run tests using pytest
                bat 'venv\\Scripts\\activate && venv\\Scripts\\pytest.exe test_app.py'
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

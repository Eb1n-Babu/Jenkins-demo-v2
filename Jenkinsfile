pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Eb1n-Babu/Jenkins-demo-v2.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }
        stage('Publish Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
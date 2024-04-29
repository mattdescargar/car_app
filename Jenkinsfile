pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mattdescargar/car_app.git'
            }
        }
        stage('Build Docker Image') {
            agent {
                docker { image 'python:3' }
            }
            steps {
                script {
                    docker.build('my-docker-image:latest', '.')
                }
            }
        }
        stage('Install dependencies') {
            agent {
                docker { image 'my-docker-image:latest' }
            }
            steps {
                script {
                    sh 'pip --version'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        // Add other stages as needed
    }
    post {
        success {
            echo 'Build successful! Deploying...'
        }
        failure {
            echo 'Build failed! Check logs for details.'
        }
    }
}

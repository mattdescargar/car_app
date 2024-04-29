pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mattdescargar/car_app.git'
            }
        }
        stage('Build Docker Image') {
            agent any
            steps {
                container('python:3') {
                    script {
                        docker.build('my-docker-image:latest', '.')
                    }
                }
            }
        }
        stage('Install dependencies') {
            agent any
            steps {
                container('my-docker-image:latest') {
                    script {
                        sh 'pip --version'
                        sh 'pip install -r requirements.txt'
                    }
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

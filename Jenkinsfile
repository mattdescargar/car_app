pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mattdescargar/car_app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('my-docker-image:latest', '-f path/to/your/Dockerfile .')
                }
            }
        }
        stage('Install dependencies') {
            steps {
                script {
                    docker.image('my-docker-image:latest').inside {
                        sh 'pip --version'
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }
        // Add other stages as needed
    }
    post {
        always {
            // Your post-build actions
        }
        success {
            echo 'Build successful! Deploying...'
        }
        failure {
            echo 'Build failed! Check logs for details.'
        }
    }
}

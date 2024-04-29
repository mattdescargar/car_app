pipeline {
    agent {
        docker {
            image 'python:3'
            args '-u root' // Ensure we can install packages as root
        }
    }
    environment {
        DJANGO_SETTINGS_MODULE = 'car_project.settings'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mattdescargar/car_app.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip --version' // Verify pip is available
                sh 'pip install --upgrade pip' // Ensure pip is up to date
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Static code analysis') {
            steps {
                sh 'flake8 .'
            }
        }
        stage('Build') {
            steps {
                sh 'python manage.py collectstatic --noinput'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python manage.py migrate'
                sh 'python manage.py runserver'
            }
        }
    }
    post {
        always {
            junit 'reports/**/*.xml'
            archiveArtifacts artifacts: 'reports/**/*.xml'
        }
        success {
            echo 'Build successful! Deploying...'
        }
        failure {
            echo 'Build failed! Check logs for details.'
        }
    }
}

pipeline {
    agent any
    environment {
        PYTHON_HOME = tool name: 'Python3.9', type: 'hudson.plugins.python.PythonInstallation'
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
                sh "${PYTHON_HOME}/bin/pip install -r requirements.txt"
            }
        }
        stage('Run tests') {
            steps {
                sh "${PYTHON_HOME}/bin/python manage.py test"
            }
        }
        stage('Static code analysis') {
            steps {
                sh "${PYTHON_HOME}/bin/flake8 ."
            }
        }
        stage('Build') {
            steps {
                sh "${PYTHON_HOME}/bin/python manage.py collectstatic --noinput"
            }
        }
        stage('Deploy') {
            steps {
                sh "${PYTHON_HOME}/bin/python manage.py migrate"
                sh "${PYTHON_HOME}/bin/python manage.py runserver"
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

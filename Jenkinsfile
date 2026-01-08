pipeline {
    agent {
        docker { 
            image 'python:3.10-slim' 
        }
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Install requirements...'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Unit tests') {
            steps {
                echo 'Start pytest...'
                sh 'pytest --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Lint') {
            steps {
                echo 'Using Flake8...'
                sh 'pip install flake8'
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
            }
        }
    }

    post {
        success {
            echo 'Success!'
        }
        failure {
            echo 'Error :/'
        }
    }
}
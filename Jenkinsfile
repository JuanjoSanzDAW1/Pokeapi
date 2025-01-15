pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'file:///home/juan/dev/poke-api-project'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}


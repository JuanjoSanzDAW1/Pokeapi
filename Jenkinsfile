pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {

                git branch: 'main',
                    url: 'https://github.com/JuanjoSanzDAW1/Pokeapi.git',
                    credentialsId: 'c15beb58-e0cf-4866-b778-7d6f884aaf05'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pokeapi-image .'
            }
        }
        stage('Run Tests') {
            steps {

                sh 'docker run --rm pokeapi-image pytest --junitxml=report.xml'
            }
        }
    }
    post {
        always {

            junit 'report.xml'
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t devops-collab .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                bat 'docker run -d -p 5000:8080 devops-collab'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning the repository...'
                git 'https://github.com/SanketYalawar/devops-collab-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t devops-collab .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run -d -p 5000:8080 devops-collab'
            }
        }
    }
}

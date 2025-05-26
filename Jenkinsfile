pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/SanketYalawar/devops-collab-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-collab .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8080:8080 devops-collab'
            }
        }
    }
}

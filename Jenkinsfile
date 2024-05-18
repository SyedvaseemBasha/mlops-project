pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDS = credentials('docker-hub-credentials')
    }
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("mlops-project:latest")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image("mlops-project:latest").inside {
                        sh 'python -m unittest discover -s tests'
                    }
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'DOCKER_HUB_CREDS') {
                        docker.image("mlops-project:latest").push('latest')
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f kubernetes_deployment.yaml'
                }
            }
        }
    }
}

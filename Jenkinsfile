pipeline {
    agent any

    environment {
        IMAGE_NAME = "c270_project"
        CONTAINER_NAME = "calculator"
        PORT = "5050"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/23024801-Clement/C270_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Tests Inside Docker') {
            steps {
                sh "docker run --rm ${IMAGE_NAME} pytest test_calculator.py"
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS') {
                        sh "docker stop ${CONTAINER_NAME} || true"
                        sh "docker rm ${CONTAINER_NAME} || true"
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo "[SUCCESS] Build, Test & Deployment Completed!"
        }
        failure {
            echo "[ERROR] Build, Test, or Deployment Failed! Check logs."
        }
    }
}

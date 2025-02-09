pipeline {
    agent any

    environment {
        IMAGE_NAME = "c270_project"
        CONTAINER_NAME = "calculator"
        PORT = "5050"
    }

    stages {
        stage("Checkout Code") {
            steps {
                git branch: 'master', url: 'https://github.com/23024801-Clement/C270_Project.git'
            }
        }

        stage("Build Docker Image") {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage("Run Tests Inside Docker") {
            steps {
                script {
                    def testResult = sh(script: "docker run --rm ${IMAGE_NAME} pytest test_calculator.py", returnStatus: true)
                    if (testResult != 0) {
                        error "Tests failed! Stopping deployment."
                    }
                }
            }
        }

        stage("Stop Old Container") {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS') {
                        sh '''
                        if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
                            docker stop ${CONTAINER_NAME}
                            docker rm ${CONTAINER_NAME}
                        fi
                        '''
                    }
                }
            }
        }

        stage("Deploy Container") {
            steps {
                sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo "SUCCESS"
        }
        failure {
            echo "ERROR"
        }
    }
}

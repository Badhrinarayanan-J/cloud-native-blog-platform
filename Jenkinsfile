pipeline {
    agent any

    environment {
        FRONTEND_IMAGE = "badhrinarayanan26/frontend"
        BACKEND_IMAGE  = "badhrinarayanan26/backend"
        IMAGE_TAG      = "latest"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh 'docker build -t ${FRONTEND_IMAGE}:${IMAGE_TAG} .'
                }
            }
        }

        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t ${BACKEND_IMAGE}:${IMAGE_TAG} .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Frontend Image') {
            steps {
                sh 'docker push ${FRONTEND_IMAGE}:${IMAGE_TAG}'
            }
        }

        stage('Push Backend Image') {
            steps {
                sh 'docker push ${BACKEND_IMAGE}:${IMAGE_TAG}'
            }
        }

    }

    post {
        always {
            sh 'docker logout || true'
            cleanWs()
        }
    }
}

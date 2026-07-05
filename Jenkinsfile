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
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Verify Project Structure') {
            steps {
                sh '''
                echo "Current Directory:"
                pwd

                echo "Repository Files:"
                ls -R
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh '''
                    docker build -t ${FRONTEND_IMAGE}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh '''
                    docker build -t ${BACKEND_IMAGE}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Verify Docker Images') {
            steps {
                sh '''
                docker images
                '''
            }
        }

        /*
        Uncomment this stage after creating
        Docker Hub credentials named:
        dockerhub-creds

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                    docker push ${FRONTEND_IMAGE}:${IMAGE_TAG}
                    docker push ${BACKEND_IMAGE}:${IMAGE_TAG}

                    docker logout
                    '''
                }
            }
        }
        */

    }

    post {

        success {
            echo '======================================='
            echo 'Pipeline completed successfully!'
            echo 'Frontend image built successfully.'
            echo 'Backend image built successfully.'
            echo '======================================='
        }

        failure {
            echo '======================================='
            echo 'Pipeline failed.'
            echo 'Check the Console Output.'
            echo '======================================='
        }

        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
    }
}

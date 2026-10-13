pipeline {
    agent any

    environment {
        APP_NAME = 'new-app-nti'
        REPO_URL = 'https://github.com/drift3/nti-jenkins-k8s.git'
        KUBECONFIG = '/var/jenkins_home/kubeconfig'
        KUBECTL = '/var/jenkins_home/tools/kubectl'
    }

    stages {
        stage('Getting Repo files') {
            steps {
                git branch: 'main',
                    url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${APP_NAME}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        set +x
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" --password-stdin

                        docker tag "${APP_NAME}:${BUILD_NUMBER}" \
                            "$DOCKER_USERNAME/${APP_NAME}:${BUILD_NUMBER}"

                        docker push "$DOCKER_USERNAME/${APP_NAME}:${BUILD_NUMBER}"

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        set -eu

                        IMAGE="$DOCKER_USERNAME/$APP_NAME:$BUILD_NUMBER"

                        sed "s|IMAGE_PLACEHOLDER|$IMAGE|g" \
                            k8s/deployment.yaml > deployment.yaml

                        "$KUBECTL" apply -f deployment.yaml
                        "$KUBECTL" apply -f k8s/service.yaml

                        "$KUBECTL" rollout status deployment/"$APP_NAME" \
                            --timeout=120s

                        "$KUBECTL" get pods -l app="$APP_NAME"
                        "$KUBECTL" get service "$APP_NAME"
                    '''
                }
            }
        }
    }
}

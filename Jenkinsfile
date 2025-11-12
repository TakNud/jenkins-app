pipeline {
    agent any

    environment {
        GIT_REPO_URL    = "https://github.com/TakNud/jenkins-app.git"
        GIT_BRANCH      = "main"
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        DOCKER_IMAGE    = "almogso/jenkins-docker-example"
        APP_PORT        = "5000"
    }

    // triggers {
    //     githubPush()
    // }
    stages {
        // stage('Clone Repository (git CLI)') {
        //     steps {
        //         echo "Cloning public repository with git CLI..."
        //         git branch: "${GIT_BRANCH}", url: "${GIT_REPO_URL}"
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image from..."
                sh """
				  pwd
				  ls
                  docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo "Logging in to Docker Hub..."
                sh """
                  echo "${DOCKERHUB_CREDS_PSW}" | docker login -u "${DOCKERHUB_CREDS_USR}" --password-stdin
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image..."
                sh """
                  docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                  docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                  docker push ${DOCKER_IMAGE}:latest
                """
            }
        }

        stage('Run Container') {
            steps {
                echo "Running container from latest image..."
                sh """
                  docker stop my-jenkins-app || true
                  docker rm my-jenkins-app || true

                  docker run -d --name my-jenkins-app -p ${APP_PORT}:${APP_PORT} ${DOCKER_IMAGE}:latest
                """
            }
        }
        stage('Docker Logs') {
            steps {
                sh """
                  docker logs my-jenkins-app
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful. App available on port 8080 of the Jenkins server."
        }
        failure {
            echo "❌ Build failed. Check the logs."
        }
    }
}

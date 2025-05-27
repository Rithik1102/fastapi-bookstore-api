pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Build') {
            steps {
                echo "Setting up Python virtual environment..."
                
                bat ".\\%VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                echo "Running automated tests..."
                bat ".\\%VENV_DIR%\\Scripts\\activate && pytest tests"
            }
        }

        stage('Code Quality') {
            steps {
                echo "Running flake8 for code quality..."
                bat ".\\%VENV_DIR%\\Scripts\\activate && pip install flake8 && flake8 app"
            }
        }

        stage('Security') {
            steps {
                echo "Running Trivy scan on Docker image..."
                bat "docker build -t fastapi-bookstore ."
                bat "trivy image --severity HIGH,CRITICAL fastapi-bookstore"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying with Docker Compose..."
                bat "docker-compose up -d"
            }
        }

        stage('Release') {
            steps {
                echo "Tagging release and pushing to Git..."
                script {
                    def version = "v1.${env.BUILD_NUMBER}"
                    bat "git config --global user.email \"you@example.com\""
                    bat "git config --global user.name \"Your Name\""
                    bat "git tag ${version}"
                    bat "git push origin ${version}"
                }
            }
        }

        stage('Monitoring') {
            steps {
                echo "Health check endpoint..."
                bat "curl http://localhost:8000/health || echo 'App not healthy!'"
            }
        }
    }
}

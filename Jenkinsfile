pipeline {
    agent any

    environment {
        // Ensure python and pip are in PATH, if not, add absolute path here
        PYTHON = "C:\\Users\\rithi\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
        PIP = "C:\\Users\\rithi\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                bat "${env.PIP} install --upgrade pip"
                bat "${env.PIP} install -r requirements.txt"
                echo 'Build complete.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Run pytest, adjust if you use unittest or other test framework
                bat "${env.PYTHON} -m pytest test_main.py"
            }
        }

        

        stage('Security') {
            steps {
                echo 'Running security scan with Bandit...'
                bat "${env.PIP} install bandit"
                bat "bandit -r ."
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Example: build Docker image and run container
                bat "docker build -t fastapi-bookstore-api:latest ."
                bat "docker stop bookstore-container || echo 'No container running'"
                bat "docker rm bookstore-container || echo 'No container to remove'"
                bat "docker run -d -p 8000:8000 --name bookstore-container fastapi-bookstore-api:latest"
            }
        }

        stage('Release') {
            steps {
                echo 'Release stage: Tagging repository (example)'
                bat 'git tag -a v1.0.${BUILD_NUMBER} -m "Release build ${BUILD_NUMBER}"'
                bat 'git push origin --tags'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring stage (example placeholder)'
                // Configure monitoring/alerts as needed outside Jenkins or with plugins
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

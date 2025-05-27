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
                bat '''
                chcp 65001
                "C:\\Users\\rithi\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\bandit.exe" -r . > bandit_report.txt
                type bandit_report.txt
                '''
            }
        }


        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                bat '''
                docker build -t fastapi-bookstore-api:latest .

                docker stop bookstore-container 2>nul || echo No container running
                docker rm bookstore-container 2>nul || echo No container to remove

                docker run -d -p 8000:8000 --name bookstore-container fastapi-bookstore-api:latest
                '''
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

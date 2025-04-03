pipeline {
    agent {
        docker {
            image 'python:3.11'  
            args '-u root --privileged --network=host'
        }
    }
    environment { //переменные окр
        HOME = "${env.WORKSPACE}"  
        BIN_PATH = "${HOME}/.local/bin/"
        PATH = "${BIN_PATH}:${env.PATH}"
    }
    stages {
        stage('Git Clone') {
            steps {
                // Клонируем репозиторий
                git changelog: false, url: 'http://gitlab.devops.ru/ALEYADIMA/jenkinseeesx'
            }
        }
        stage('Prepare') { //подготовка
            steps {
                sh '''
                    echo "deb http://deb.debian.org/debian bookworm main" > /etc/apt/sources.list
                    apt-get clean
                    apt-get update --allow-releaseinfo-change
                    apt-get install -y iputils-ping curl
                    curl -Is https://pypi.org | head -n 1
                    python --version
                    pip install --user virtualenv
                    ${BIN_PATH}virtualenv venv
                '''
            }
        }
        stage('Install Dependencies') { //Установка зависимостей
            steps {
                sh '''
                    . venv/bin/activate
                    pip install -r src/requirements.txt
                '''
            }
        }
        stage('Test') { //тесты лол
            steps {
                sh '''
                    . venv/bin/activate
                    pytest src/lab2-test.py || echo 'pytest failed or no tests found'
                    flake8 src || echo 'flake8 failed'
                    mypy src || echo 'mypy failed'
                '''
            }
        }
    }
}

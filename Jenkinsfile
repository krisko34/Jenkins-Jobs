pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
             docker run -it slackmessager python main.py -n "x" -num 5 -nea 4 -url "google.com"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

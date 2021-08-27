pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'pythondocker_app'
                    reuseNode true
                }
            }
            steps {
                sh 'python --version'
            }
        }
    }
}

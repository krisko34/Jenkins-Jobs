pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                     docker {
                         image 'pythondocker_app'
                    }
            }
            }
        }
            stage('Test') {
                steps {
                    sh 'python --version'
                }
            }
        
    }
}

pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('main') {
      steps {
        sh 'python main.py'
      }
    }
  }
}
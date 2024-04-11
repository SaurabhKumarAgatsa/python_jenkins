pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Setup') {
      steps {
        sh 'python3 -m venv env' // Create a virtual environment
        sh 'source env/bin/activate' // Activate the virtual environment
        sh 'pip install -r requirements.txt' // Install dependencies
      }
    }
    stage('main') {
      steps {
        sh 'python3 main.py'
      }
    }
  }
}

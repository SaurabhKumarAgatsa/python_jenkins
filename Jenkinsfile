pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('main') {
      steps {
        sh 'python3 main.py'
      }
    }
  }
}








// pipeline {
//   agent any
//   stages {
//     stage('version') {
//       steps {
//         sh 'python3 --version'
//       }
//     }
//     stage('main') {
//       steps {
//         sh 'python3 main.py'
//       }
//     }
//   }
// }
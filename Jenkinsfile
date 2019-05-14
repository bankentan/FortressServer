pipeline {
  agent {
    docker {
      image 'nginx'
    }

  }
  stages {
    stage('num1') {
      parallel {
        stage('num1') {
          steps {
            sh '''mkdir -p /tmp/tan
echo "I am num1" >/tmp/tan/ken.txt'''
          }
        }
        stage('num1.1') {
          steps {
            sh 'echo "I am num1.1" >/tmp/tan/ken.txt'
          }
        }
      }
    }
    stage('num2') {
      steps {
        echo 'I am nginx'
      }
    }
  }
}
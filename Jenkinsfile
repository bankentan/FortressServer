pipeline {
  agent any
  stages {
    stage('num1') {
      steps {
        echo 'I am a num1'
      }
    }
    stage('num2') {
      steps {
        sh '''mkdir -p /tmp/tan
echo \'tanyongjia\' >/tmp/tan/ken.txt'''
      }
    }
    stage('num3') {
      steps {
        mail(subject: 'is ok', body: 'test ok', bcc: 'ok ', cc: 'ok', charset: 'utf8', to: 'tanyongjia2007@126.com')
      }
    }
  }
  environment {
    ken = 'tanyongjia'
  }
}
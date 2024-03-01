pipeline {
    agent any

    environment {
        QA_SERVER = 'https://qa.application.com/'
        CT_SERVER = 'http://ct.application.com/'
    }

    
    stages {
        stage('Initialize') {
            steps {
                sh 'echo "PATH= ${PATH}"'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh '/home/drashti/Documents/Android_Automation/robot-files/python/pytest/Tests/Mobile/setup_and_run.sh'
            }
        }


        stage('Run Robot Tests') {
            steps {
                script {
                    sh 'python3 /home/drashti/Documents/Android_Automation/robot-files/python/pytest/Tests/Mobile/test_Flipkart.py'
                }
            }
        }
    }
    
    post {
        always {
            script {
                step([
                    outputPath          : '/home/drashti/Documents/Android_Automation/robot-files/python/pytest/Tests/Mobile/',
                    outputFileName      : '**/output.xml',
                    reportFileName      : '**/report.html',
                    logFileName         : '**/log.html',
                    disableArchiveOutput: false,
                    passThreshold       : 50,
                    unstableThreshold   : 40,
                    otherFiles          : "**/*.png,**/*.jpg",
                ])
            }
        }
    }
}
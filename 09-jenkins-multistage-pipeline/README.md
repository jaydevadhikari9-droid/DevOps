# Exercise 9 - Jenkins Multi-Stage Pipeline

## Objective
Build, test, deploy, and verify a sample Python Flask application using a Jenkins pipeline.

## Application
The home endpoint returns:

`Hello, Jenkins Multi-Stage Pipeline!`

## Files
- `app.py` - Flask application
- `requirements.txt` - Python dependencies
- `test_app.py` - Unit test
- `Jenkinsfile` - Jenkins pipeline definition
- `evidence/` - Screenshots and verification results

## Pipeline stages
Build, Test, Deploy, Run Application, and Test Application.

## Deployment
The pipeline deploys the application to a mock deployment directory in the Jenkins workspace.

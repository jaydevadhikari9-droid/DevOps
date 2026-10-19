\# Exercise 7: Jenkins CI/CD Pipeline



\## Objective

Create and execute a Jenkins declarative pipeline with Checkout, Build, Test, and Deploy stages.



\## Tools Used

\- Jenkins

\- Docker Desktop

\- PowerShell

\- Git and GitHub



\## Pipeline Stages

1\. \*\*Checkout\*\* — starts the pipeline.

2\. \*\*Build\*\* — prints a successful build message.

3\. \*\*Test\*\* — prints a successful test message.

4\. \*\*Deploy\*\* — prints a successful deployment message.



\## Verification

The Jenkins console output confirms that all four stages completed and ends with `Finished: SUCCESS`.



\## Evidence

Screenshots are stored in the `evidence/` directory:

\- `jenkins-dashboard.png.png`

\- `pipeline-build-success.png.png`

\- `console-output.png.png`



\## Result

The Jenkins pipeline executed successfully. Note that the Build, Test, and Deploy stages currently demonstrate pipeline flow using messages; they do not yet build, test, or deploy a real application.




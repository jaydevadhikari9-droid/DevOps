\# Exercise 8: Creating a Hello World Jenkins Job



\## Objective

Create and run a Jenkins Freestyle job that executes a shell script and prints `Hello, Jenkins!`.



\## Prerequisites

\- Jenkins running at `http://localhost:8080`

\- Git installed

\- Existing GitHub repository: \[DevOps](https://github.com/jaydevadhikari9-droid/DevOps)



\## Script



The `hello-world.sh` file contains:



```bash

\#!/bin/bash

echo "Hello, Jenkins!"

```



\## Jenkins Job Configuration



\- \*\*Job name:\*\* HelloWorld

\- \*\*Job type:\*\* Freestyle project

\- \*\*Source Code Management:\*\* Git

\- \*\*Repository URL:\*\* `https://github.com/jaydevadhikari9-droid/DevOps.git`

\- \*\*Branch:\*\* `\*/main`

\- \*\*Build step:\*\* Execute shell



Build command:



```bash

cd 07-jenkins-ci

bash hello-world.sh

```



The command uses the existing script in the repository. In Jenkins, the job checks out the repository into its workspace before running the build step.



\## Execution



1\. Open Jenkins at `http://localhost:8080`.

2\. Open the `HelloWorld` job.

3\. Select \*\*Build Now\*\*.

4\. Open the latest build and select \*\*Console Output\*\*.



\## Expected Result



```text

Hello, Jenkins!

Finished: SUCCESS

```



\## Evidence



See `evidence/hello-world-success.png` for the successful Jenkins Console Output screenshot.



\## Result



The Jenkins Freestyle job successfully executed the shell script and printed the expected message.


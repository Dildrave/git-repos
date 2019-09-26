# GIT-REPOS

## Introduction

Git-Repos is a simple python based tool which will display a users *public* repositories
This has been currently tested in Linux environment (Ubuntu 18.04) 

## Requirements (Tested)

* python 3.7

## Guide

#### 1 Install requests

```pip install requests```

#### 2 Install flask

```pip install flask```

#### 3 Export Environment variable

```export FLASK_APP=git-repos.py```

#### 4 Create GitHub OAuth App

In you Github account go to **Setting -> Developer Settings -> OAuth Apps -> New OAuth App**

Enter the follwing in the fileds

```
Application Name: GIT-REPOS
Homepage URL: http://localhost:8080
Application Description: sample app
Authorization callback URL: http://localhost:8080/oauth/redirect
```

#### 5 Get client credentials

Rename the file ```client.example.json``` to ```client.json``` and paste the **Client ID** and **Client Secret** copied from the OAuth App

#### 6 Run tool

```flask run --port 8080```

Now navigating to ```http://localhost:8080``` which will redirect to the github authentication page

**More on:**https://uselessspot.wordpress.com/2019/09/24/oauth-2-0-retrieve-a-your-github-repo-details/

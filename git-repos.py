from flask import Flask, request, redirect, render_template
import requests
from pprint import pprint
import json

app = Flask(__name__)

# read client.json to obtain client details
with open('client.json', 'r') as client_data:
    client_data=client_data.read()
client_data = json.loads(client_data)

client_id = client_data['client_id']
client_secret = client_data['client_secret']
redirect_uri = "http://localhost:8080/oauth/redirect"



@app.route('/', methods=['get'])
def home():
    URL = "https://github.com/login/oauth/authorize?client_id=" + client_id + "&redirect_uri=" + redirect_uri
    return redirect(URL)

# redirects to git oauth and renders the template.html
@app.route('/oauth/redirect', methods=['get'])
def start():
    
    code = request.args.get('code')

    GITHUB_OAUTH_URL = "https://github.com/login/oauth/access_token"
    headers = {'accept': 'application/json'}
    params = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    
    response = requests.post(url = GITHUB_OAUTH_URL, headers = headers, params = params)
    access_token = json.loads(response.text)['access_token']
    
    user = get_user(access_token)
    repo_names = get_user_repos_names(user, access_token)

    return render_template("template.html", user = user, repo_names = repo_names)


# return current users name
def get_user(access_token):
    GITHUB_USER_URL = 'https://api.github.com/user'
    headers = {'Authorization': 'token ' + access_token}
    response = requests.get(GITHUB_USER_URL, headers = headers)

    user = json.loads(response.text)['login']
    return user


# retrun list public of repos of the current user
def get_user_repos_names(user, access_token):
    GITHUB_USER_REPO_URL = 'https://api.github.com/user/repos'
    headers = {'Authorization': 'token ' + access_token}
    response = requests.get(GITHUB_USER_REPO_URL, headers = headers)

    repos = json.loads(response.text)
    repo_names = []
    for repo in repos:
        repo_names.append(repo['name'])
    return repo_names
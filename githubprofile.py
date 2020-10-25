import requests
import json


def githubProfile():
    parsedData = []
    req = requests.get('https://api.github.com/users/' + username)
    jsonList = []
    jsonList.append(json.loads(req.content))
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    return parsedData


username = input("enter your github username: ")
print(githubProfile())

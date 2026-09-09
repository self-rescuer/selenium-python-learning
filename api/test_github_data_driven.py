import pytest
import requests
import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path=os.path.join(current_dir,"test_data.json")

with open(data_path,encoding='utf-8') as f:
    test_data = json.load(f)

users=test_data['users']
usernames=[user['username']for user in users]

@pytest.mark.parametrize("username",usernames)
def test_get_user_by_username(username):
    response=requests.get(f"https://api.github.com/users/{username}")
    assert response.status_code==200
    data=response.json()

    assert data['login']==username

    assert 'id' in data
    assert'public_repos' in data

    assert data['id']>0
    assert data['public_repos']>=0


import pytest
import requests
BASE_URL='https://api.github.com'

@pytest.fixture
def base_url():
    return BASE_URL

def test_get_user_info(base_url):
    username='octocat'
    response=requests.get(BASE_URL+'/users/'+username)
    assert response.status_code == 200

    data=response.json()

    assert 'login' in data
    assert 'name' in data
    assert 'id' in data
    assert 'email' in data


    assert data['login'] == username

    assert isinstance(data['name'],str)
    assert isinstance(data['id'],int)
    assert isinstance(data['public_repos'],int)

    assert data['id']>0
    assert data['public_repos']>=0


def test_get_user_repos(base_url):
    username='octocat'
    response=requests.get(BASE_URL+'/users/'+username+'/repos')
    assert response.status_code==200
    repos=response.json()

    assert isinstance(repos,list)
    assert len(repos)>0
    for repo in repos:
        assert 'name' in repo
        assert len(repo['name'])>0

def test_get_nonexistent_user(base_url):
    username='this-user-should-not-exist-123456789'
    response=requests.get(BASE_URL+'/users/'+username)
    assert response.status_code==404

    data=response.json()
    assert data['message']=='Not Found'
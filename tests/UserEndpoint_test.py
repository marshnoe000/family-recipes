from conftest import client


def testRegister(client):
    response = client.post("/user/register",
                           json=dict(username="username", password="password", email="email", name="name"))
    assert response.status_code == 201

    response = client.post("/user/register",
                           json=dict(username="username", password="password", email="email", name="name"))
    assert response.status_code == 500

    response = client.post("/user/register",
                           json=dict(username="", password="password", email="email", name="name"))
    assert response.status_code == 400


def testGetUser(client):
    addedUsernames = ['user1', 'user2', 'user3']
    missingUsernames = ['user4', 'user5']

    for username in addedUsernames:
        client.post("/user/register",
                    json=dict(username=username, password="password", email="email", name="name"))

    for username in addedUsernames:
        response = client.get(f"/user/{username}")

        assert response.status_code == 200

    for username in missingUsernames:
        response = client.get(f"/user/{username}")

        assert response.status_code == 404


def testDeleteUser(client):
    addedUsernames = ['user1', 'user2', 'user3']
    for username in addedUsernames:
        client.post("/user/register",
                    json=dict(username=username, password="password", email="email", name="name"))

    for username in addedUsernames:
        response = client.delete(f"/user/{username}")

        assert response.status_code == 204

    for username in addedUsernames:
        response = client.delete(f"/user/{username}")

        assert response.status_code == 404


def testLogin(client):
    response = client.post("/user/register",
                           json=dict(username="username", password="password", email="email", name="name"))
    assert response.status_code == 201

    loginResponse = client.post("/user/login", json=dict(username="username", password="password"))
    assert loginResponse.status_code == 200

    loginResponse = client.post("/user/login", json=dict(username="username", password="wrongPassword"))
    assert loginResponse.status_code == 401

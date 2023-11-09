from conftest import client


def testRegister(client):
    response = client.post("/user/register",
                           json=dict(username="username", password="password", email="email", name="name"))
    assert response.status_code == 201

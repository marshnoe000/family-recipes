from conftest import client


def testCreateGroupSuccess(client):
    response = client.post(
        "/group", json=dict(name="new-group", description="A new group"))

    assert response.status_code == 201
    assert "id" in response.get_json()


def testCreateGroupBadRequestError(client):
    response = client.post(
        "/group", json=dict(description="A new group"))

    assert response.status_code == 400
    json = response.get_json()
    assert json["error"] == "BadRequestError"


def testGetGroupSuccess(client):
    name = "new-group"
    description = "A new group"

    target = client.post(
        "/group", json=dict(name="new-group", description="A new group"))
    id = target.get_json()["id"]

    response = client.get(f"/group/{id}")
    assert response.status_code == 200
    group = response.get_json()["data"]
    assert group["groupId"] is not None
    assert group["name"] == name
    assert group["description"] == description
    assert group["dateCreated"] is not None
    assert "members" not in group


def testGetGroupNotFoundError(client):
    response = client.get("/group/10000")
    assert response.status_code == 404
    json = response.get_json()
    assert json["error"] == "NotFoundError"


def testGetGroupWithMembersSuccess(client):
    name = "new-group"
    description = "A new group"

    target = client.post(
        "/group", json=dict(name="new-group", description="A new group"))
    id = target.get_json()["id"]
    addUrl = f"/group/{id}/users"
    expectedMembers = ["user1", "user2", "user3", "user4", "user5"]
    for user in expectedMembers:
        client.post(addUrl, json=dict(username=user))

    response = client.get(f"/group/{id}?members=true")
    assert response.status_code == 200
    group = response.get_json()["data"]
    assert group["groupId"] is not None
    assert group["name"] == name
    assert group["description"] == description
    assert group["dateCreated"] is not None
    assert type(group["members"]) is list
    assert len(group["members"]) == len(expectedMembers)
    assert type(group["members"][0]) is str
    for actual in group["members"]:
        assert actual in expectedMembers

    response = client.get(f"/group/{id}?members=TRUE")
    assert response.status_code == 200
    group = response.get_json()["data"]
    assert group["groupId"] is not None
    assert group["name"] == name
    assert group["description"] == description
    assert group["dateCreated"] is not None
    assert type(group["members"]) is list
    assert len(group["members"]) == len(expectedMembers)
    assert type(group["members"][0]) is str
    for actual in group["members"]:
        assert actual in expectedMembers

    response = client.get(f"/group/{id}?members=1")
    assert response.status_code == 200
    group = response.get_json()["data"]
    assert group["groupId"] is not None
    assert group["name"] == name
    assert group["description"] == description
    assert group["dateCreated"] is not None
    assert type(group["members"]) is list
    assert len(group["members"]) == len(expectedMembers)
    assert type(group["members"][0]) is str
    for actual in group["members"]:
        assert actual in expectedMembers


def testGetGroupMembersSuccess(client):
    expectedMembers = ["user1", "user2", "user3", "user4", "user5"]
    for user in expectedMembers:
        client.post("/group/1/users", json=dict(username=user))

    response = client.get("/group/1/users")
    assert "data" in response.get_json()
    data = response.get_json()["data"]
    for actual in data:
        assert actual in expectedMembers

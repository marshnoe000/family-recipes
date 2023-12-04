from conftest import client
import time


def testCreatePost(client):
    response = client.post("/post", json=dict(id="id", author="author", groupId="groupId",
                                              content="content", dateCreated="dateCreated", likes="likes",
                                              recipeId="recipeId", tags=["tags", "tags", "tags"]))
    assert response.status_code == 201
    assert "id" in response.get_json()


def testGetSinglePost(client):
    postId = "id"
    author = "author"
    groupId = "groupId"
    content = "content"
    recipeId = "recipeId"
    tags = ["tags"]
    response = client.post("/post", json=dict(id=postId, author=author, groupId=groupId,
                                              content=content,
                                              recipeId=recipeId, tags=tags))

    postId = response.get_json()['id']
    response = client.get(f"/post/{postId}?embedRecipe=false")
    assert response.status_code == 200

    post = response.get_json()['data']
    assert post['id'] == postId
    assert post['author'] == author
    assert post['groupId'] == groupId
    assert post['content'] == content
    assert post['dateCreated'] is not None
    assert post['likes'] == 0
    assert post['recipeId'] == recipeId
    assert post['tags'] == tags


# not the most useful test...
def testGetUserFeed(client):
    targetUser = "user1"
    client.post("/user/register", json=dict(username=targetUser, password="pass",
                                       email="email", name="name"))
    subscribedGroups = [client.post("/group", json=dict(name=f"group{i}")).get_json()['id']
                        for i in range(1, 4)]
    for id in subscribedGroups:
        client.post(f"/group/{id}/users", json=dict(username=targetUser))

    client.post("/recipe", json=dict(title="recipe")).get_json()
    for id in range(1, 6):
        for _ in range(2):
            client.post("/post", json=dict(author=f"poster{id}", content="a post",
                                           groupId=id, recipeId=1))

        # terrible, but sleep so feed can be sorted on timestamp
        time.sleep(1.0)

    feed = client.get(f"/feed/{targetUser}").get_json()['data']

    assert len(feed) == len(subscribedGroups) * 2
    assert feed[0]['groupId'] == subscribedGroups[-1]
    assert feed[-1]['groupId'] == subscribedGroups[0]

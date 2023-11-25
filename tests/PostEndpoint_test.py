from conftest import client


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
    response = client.get(f"/post/id/{postId}")
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

# API Reference
---

## Errors
todo error responses

## Posts
### Object
```
Post: {
    id: int,
    author: string,
    recipeId: int,
    groupId: int,
    content: string,
    dateCreated: string?,
    likes: int,
    tags: string
}

```
`tags` is a comma-separated list

### Endpoints
```sh
POST /post

request: {
    author: string, <required>
    recipeId: int,  <required>
    groupId: int,   <required>
    content: string,
    tags: string
}

response: {
    status: int,
    data: Post
}
```
Creates a new post with the given information

```sh
GET /post/id/:id

request: {}

response: {
    status: int,
    data: Post
}
```
Fetches post with id `:id`

```sh
GET /post/u/:username

request: {}

response: {
    status: int,
    data: Array<Post>
}
```
Fetches all posts authored by `:username`

```sh
GET /post/g/:groupId

request: {}

response: {
    status: int,
    data: Array<Post>
}
```
Fetches all posts attached to group specified by `:groupId`

```sh
DELETE /post/id/:id

request: {}

response: {
    status: int
    data: {
        rowsAffected: int
    }
}
```
Deletes post with id `:id`


---



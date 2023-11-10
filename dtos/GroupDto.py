class GroupDto(dict):
    def __init__(self, groupId, name, description, dateCreated):
        super().__init__(
            groupId=groupId,
            name=name,
            description=description,
            dateCreated=dateCreated
        )

    def fromJson(json: dict) -> 'GroupDto':
        return GroupDto(
            json.get('groupId'),
            json.get('name'),
            json.get('description'),
            json.get('dateCreated'),
        )

    def __str__(self):
        return f"group{super().__str__()}"

    def __getattr__(self, attr: str):
        return self[attr]

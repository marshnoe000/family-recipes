from libsql_client import ResultSet


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

    def fromResultSet(rs: ResultSet, forceArray=False):
        if len(rs) == 0:
            return None

        if len(rs) == 1 and not forceArray:
            row = rs[0]
            return GroupDto(row[0], row[1], row[2], row[3])

        groups = [GroupDto(row[0], row[1], row[2], row[3]) for row in rs]
        return groups

    def __str__(self):
        return f"group{super().__str__()}"

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value
